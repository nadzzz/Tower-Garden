"""Calcul des melanges de nutriments Masterblend (Gecko Grow) pour les tours.

L'EC INITIAL n'est PAS stocke : il est fourni sur la ligne de commande au moment
du calcul, avec le numero de tour. Tout le reste (volume, EC desire, recette) vient
des fichiers data/.

Usage :
    py outils/calcul_nutriments.py T1 0.45
    py outils/calcul_nutriments.py T1 0.45 T2 0.50 T3 0.62   (plusieurs tours)

Modele : ratio fixe Masterblend:SulfateMg:NitrateCa = 2:1:2 (par masse).
    grammes = g_par_litre_pleine_force * litres * (EC_desire - EC_initial) / EC_pleine_force

Sortie : tableau console + image docs/feuille_calcul_nutriments.svg
"""
import csv, os, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")

def load_csv(name):
    with open(os.path.join(D, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_params():
    p = {}
    for r in load_csv("parametres_recette.csv"):
        v = r["valeur"]
        p[r["parametre"]] = float(v) if v.replace(".", "").isdigit() else v
    return p

def parse_args(argv, tours):
    """argv = [T1, 0.45, T2, 0.50, ...] -> [(tour_id, ec_initial), ...]"""
    if len(argv) < 2 or len(argv) % 2 != 0:
        ids = ", ".join(t["tour_id"] for t in tours)
        sys.exit(f"Usage : py outils/calcul_nutriments.py <TOUR> <EC_INITIAL> [<TOUR> <EC_INITIAL> ...]\n"
                 f"Exemple : py outils/calcul_nutriments.py T1 0.45\n"
                 f"Tours disponibles : {ids}")
    by_id = {t["tour_id"].upper(): t for t in tours}
    pairs = []
    for i in range(0, len(argv), 2):
        tid = argv[i].upper()
        if tid not in by_id:
            sys.exit(f"Tour inconnue : {argv[i]}. Disponibles : {', '.join(by_id)}")
        try:
            ec = float(argv[i + 1].replace(",", "."))
        except ValueError:
            sys.exit(f"EC initial invalide : {argv[i+1]} (attendu un nombre, ex. 0.45)")
        pairs.append((tid, ec))
    return pairs

def compute(pairs):
    comps = load_csv("recette_nutriments.csv")
    params = load_params()
    EC_REF = params["ec_pleine_force"]
    LpG = params["litres_par_gallon"]
    by_id = {t["tour_id"].upper(): t for t in load_csv("tours.csv")}
    rows = []
    for tid, ec_i in pairs:
        t = by_id[tid]
        litres = float(t["volume_gallons"]) * LpG
        ec_d = float(t["ec_desire_ms_cm"])
        dEC = max(0.0, ec_d - ec_i)
        grammes = {c["composant"]: float(c["g_par_litre_pleine_force"]) * litres * dEC / EC_REF
                   for c in comps}
        rows.append(dict(tour=t["tour_id"], nom=t["nom"], gallons=float(t["volume_gallons"]),
                         litres=litres, ec_i=ec_i, ec_d=ec_d, dEC=dEC, g=grammes))
    return comps, params, rows

# ---------------------------------------------------------------- console
def print_table(comps, params, rows):
    print(f"\nEC pleine force (calibration) = {params['ec_pleine_force']} mS/cm | "
          f"{params['litres_par_gallon']} L/gallon\n")
    hdr = f"{'Tour':<5}{'Gal':>5}{'Litres':>8}{'EC ini':>8}{'EC cible':>10}{'dEC':>7}"
    for c in comps:
        hdr += f"{c['part_etiquette']:>12}"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        line = f"{r['tour']:<5}{r['gallons']:>5.0f}{r['litres']:>8.1f}{r['ec_i']:>8.2f}{r['ec_d']:>10.2f}{r['dEC']:>7.2f}"
        for c in comps:
            line += f"{r['g'][c['composant']]:>12.1f}"
        print(line)
    print("\nColonnes Part 1/2/3 = grammes a peser.")
    print("Ordre : dissoudre Part 1 + Part 2, puis ajouter Part 3 en dernier. "
          f"pH {params['ph_cible_min']:.1f}-{params['ph_cible_max']:.1f}.\n")

# ---------------------------------------------------------------- SVG image
def esc(s):
    return html.escape(str(s))

def svg(comps, params, rows):
    W = 940
    H = 470 + len(rows) * 54 + 200
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif">']
    s.append(f'<rect width="{W}" height="{H}" fill="#f7faf5"/>')
    s.append('<rect x="0" y="0" width="940" height="92" fill="#2e7d32"/>')
    s.append('<text x="40" y="46" fill="#ffffff" font-size="30" font-weight="700">'
             'Feuille de calcul des nutriments — Tower Garden</text>')
    s.append('<text x="40" y="76" fill="#d7f0d2" font-size="17">'
             'Masterblend (Gecko Grow) • ratio 2:1:2 • dosage proportionnel à la hausse d’EC</text>')

    y = 128
    s.append(f'<rect x="40" y="{y}" width="860" height="186" rx="10" fill="#ffffff" stroke="#cde0c6"/>')
    s.append(f'<text x="62" y="{y+34}" font-size="20" font-weight="700" fill="#2e7d32">Recette de base (étiquette)</text>')
    lines = [
        "1. Dissoudre le Part 1 (Masterblend) ET le Part 2 (sulfate de magnésium) dans l’eau tiède.",
        "2. Ajouter le Part 3 (nitrate de calcium) EN DERNIER, une fois les deux premiers bien dissous.",
        f"Plage de pH (hydroponie) : {params['ph_cible_min']:.1f} – {params['ph_cible_max']:.1f}.",
        "Ne jamais mélanger les concentrés secs ensemble (risque de blocage des nutriments).",
    ]
    for i, ln in enumerate(lines):
        s.append(f'<text x="62" y="{y+66+i*26}" font-size="16" fill="#333">{esc(ln)}</text>')
    cy = y + 150
    chips = [("Part 1 – Masterblend", "0,64 g/L", "#2e7d32"),
             ("Part 2 – Sulfate Mg", "0,32 g/L", "#00796b"),
             ("Part 3 – Nitrate Ca", "0,64 g/L", "#ef6c00")]
    cx = 62
    for name, val, col in chips:
        s.append(f'<rect x="{cx}" y="{cy-22}" width="258" height="34" rx="17" fill="{col}"/>')
        s.append(f'<text x="{cx+16}" y="{cy+1}" font-size="15" fill="#fff" font-weight="600">{esc(name)} : {esc(val)} (pleine force)</text>')
        cx += 270

    y = 350
    s.append(f'<text x="40" y="{y}" font-size="22" font-weight="700" fill="#2e7d32">'
             'Grammes à peser par tour</text>')
    s.append(f'<text x="40" y="{y+26}" font-size="15" fill="#555">'
             f'Réservoir {rows[0]["gallons"]:.0f} gallons = {rows[0]["litres"]:.1f} L • '
             f'calibration EC pleine force = {params["ec_pleine_force"]:.2f} mS/cm</text>')
    ty = y + 50
    cols = [("Tour", 70), ("EC\ninitial", 90), ("EC\ncible", 90), ("ΔEC", 80),
            ("Part 1\nMasterblend", 170), ("Part 2\nSulfate Mg", 150), ("Part 3\nNitrate Ca", 150)]
    x0 = 40
    s.append(f'<rect x="{x0}" y="{ty}" width="800" height="56" fill="#2e7d32"/>')
    cx = x0
    for name, w in cols:
        parts = name.split("\n")
        for j, p in enumerate(parts):
            s.append(f'<text x="{cx+w/2}" y="{ty+(24 if len(parts)==1 else 22)+j*18}" '
                     f'font-size="14" font-weight="700" fill="#fff" text-anchor="middle">{esc(p)}</text>')
        cx += w
    ry = ty + 56
    rh = 54
    palette = ["#eef6ea", "#ffffff", "#fff5e9"]
    for k, r in enumerate(rows):
        s.append(f'<rect x="{x0}" y="{ry}" width="800" height="{rh}" fill="{palette[k%3]}" stroke="#e0e8db"/>')
        vals = [r["tour"], f'{r["ec_i"]:.2f}', f'{r["ec_d"]:.2f}', f'{r["dEC"]:.2f}',
                f'{r["g"]["masterblend"]:.1f} g', f'{r["g"]["sulfate_magnesium"]:.1f} g',
                f'{r["g"]["nitrate_calcium"]:.1f} g']
        cx = x0
        for (name, w), v in zip(cols, vals):
            weight = "700" if name.startswith(("Tour", "Part")) else "400"
            s.append(f'<text x="{cx+w/2}" y="{ry+rh/2+6}" font-size="17" font-weight="{weight}" '
                     f'fill="#222" text-anchor="middle">{esc(v)}</text>')
            cx += w
        ry += rh

    fy = ry + 36
    s.append(f'<rect x="40" y="{fy}" width="860" height="118" rx="10" fill="#ffffff" stroke="#cde0c6"/>')
    s.append(f'<text x="62" y="{fy+32}" font-size="18" font-weight="700" fill="#2e7d32">Formule</text>')
    s.append(f'<text x="62" y="{fy+62}" font-size="16" fill="#333">'
             'grammes = g/L (pleine force) × litres × (EC désiré − EC initial) ÷ EC pleine force</text>')
    s.append(f'<text x="62" y="{fy+90}" font-size="15" fill="#666">'
             'Sulfate Mg = moitié du Masterblend • Nitrate Ca = égal au Masterblend • '
             'ΔEC ≤ 0 → rien à ajouter.</text>')
    s.append(f'<text x="40" y="{H-22}" font-size="13" fill="#999">'
             'Généré par outils/calcul_nutriments.py — EC initial fourni en argument.</text>')
    s.append('</svg>')
    out = os.path.join(ROOT, "docs", "feuille_calcul_nutriments.svg")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(s))
    return out

if __name__ == "__main__":
    tours = load_csv("tours.csv")
    pairs = parse_args(sys.argv[1:], tours)
    comps, params, rows = compute(pairs)
    print_table(comps, params, rows)
    path = svg(comps, params, rows)
    print(f"Image generee : {os.path.relpath(path, ROOT)}")
