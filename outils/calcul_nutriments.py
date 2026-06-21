"""Calcul des melanges de nutriments Masterblend (Gecko Grow) pour les tours.

UNITES : l'EC est exprimee en uS/cm (mode EC du compteur VIVOSUN - bouton MODE).
Tu peux aussi entrer des ppm avec l'option --ppm (conversion via ppm_facteur).
En interne, le calcul travaille en mS/cm (1 mS/cm = 1000 uS/cm).

L'EC ACTUELLE est fournie sur la ligne de commande au moment du calcul, avec le
numero de tour. Le reste (volume, EC desiree, recette, calibration, eau de base)
vient des fichiers data/.

Selon l'ecart avec la cible, le programme dit :
  - AJOUTER des nutriments (grammes de chaque part), si l'EC est sous la cible ;
  - DILUER (retirer X L et remplacer par de l'eau fraiche), si l'EC depasse ;
  - RIEN, si on est dans la tolerance.

Usage :
    py outils/calcul_nutriments.py T1 1100
    py outils/calcul_nutriments.py T1 1100 T2 1650 T3 2150
    py outils/calcul_nutriments.py --ppm T1 550 T2 825 T3 1075

Modele d'ajout : ratio fixe Masterblend:SulfateMg:NitrateCa = 2:1:2 (par masse).
    grammes = g_par_litre_pleine_force * litres * (EC_cible - EC_actuelle) / EC_pleine_force
Modele de dilution :
    litres_a_retirer = volume * (EC_actuelle - EC_cible) / (EC_actuelle - EC_eau_de_base)

Sortie : tableau console + image docs/feuille_calcul_nutriments.svg
"""
import csv, os, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data")
TOL_US = 30.0  # uS/cm : en deca, on considere la tour "dans la cible"

def load_csv(name):
    with open(os.path.join(D, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def load_params():
    p = {}
    for r in load_csv("parametres_recette.csv"):
        v = r["valeur"]
        p[r["parametre"]] = float(v) if v.replace(".", "").isdigit() else v
    return p

def parse_args(argv, tours, params):
    ppm = False
    if argv and argv[0] == "--ppm":
        ppm = True
        argv = argv[1:]
    if len(argv) < 2 or len(argv) % 2 != 0:
        ids = ", ".join(t["tour_id"] for t in tours)
        sys.exit("Usage : py outils/calcul_nutriments.py [--ppm] <TOUR> <EC_ACTUELLE> [...]\n"
                 "  EC en uS/cm (mode EC du compteur). Ajoute --ppm si tu lis en ppm.\n"
                 "  Exemple : py outils/calcul_nutriments.py T1 1100\n"
                 f"  Tours disponibles : {ids}")
    factor = params["ppm_facteur"]
    by_id = {t["tour_id"].upper(): t for t in tours}
    pairs = []
    for i in range(0, len(argv), 2):
        tid = argv[i].upper()
        if tid not in by_id:
            sys.exit(f"Tour inconnue : {argv[i]}. Disponibles : {', '.join(by_id)}")
        try:
            val = float(argv[i + 1].replace(",", "."))
        except ValueError:
            sys.exit(f"EC actuelle invalide : {argv[i+1]} (nombre attendu)")
        ec_us = val / factor if ppm else val   # ppm -> uS/cm
        pairs.append((tid, ec_us))
    return pairs, ppm

def compute(pairs):
    comps = load_csv("recette_nutriments.csv")
    params = load_params()
    EC_REF = params["ec_pleine_force"]       # mS/cm a pleine force
    LpG = params["litres_par_gallon"]
    base_us = params["eau_base_uS"]
    by_id = {t["tour_id"].upper(): t for t in load_csv("tours.csv")}
    rows = []
    for tid, ec_i_us in pairs:
        t = by_id[tid]
        litres = float(t["volume_gallons"]) * LpG
        ec_d_us = float(t["ec_desire_ms_cm"]) * 1000
        diff = ec_d_us - ec_i_us
        action, grammes, litres_dil = "ok", {}, 0.0
        if diff > TOL_US:
            action = "ajouter"
            dEC = diff / 1000.0
            grammes = {c["composant"]: float(c["g_par_litre_pleine_force"]) * litres * dEC / EC_REF
                       for c in comps}
        elif -diff > TOL_US:
            action = "diluer"
            denom = ec_i_us - base_us
            litres_dil = litres * (ec_i_us - ec_d_us) / denom if denom > 0 else float("inf")
        rows.append(dict(tour=t["tour_id"], gallons=float(t["volume_gallons"]), litres=litres,
                         ec_i_us=ec_i_us, ec_d_us=ec_d_us, action=action, g=grammes,
                         litres_dil=litres_dil))
    return comps, params, rows

def action_text(r):
    if r["action"] == "ajouter":
        g = r["g"]
        return (f"Ajouter  MB {g['masterblend']:.1f} g  |  SulfMg {g['sulfate_magnesium']:.1f} g  "
                f"|  NitrCa {g['nitrate_calcium']:.1f} g")
    if r["action"] == "diluer":
        return f"Diluer : retirer {r['litres_dil']:.1f} L et remplacer par de l'eau fraiche"
    return "Dans la cible : ne rien faire"

# ---------------------------------------------------------------- console
def print_table(comps, params, rows, ppm):
    src = "ppm -> uS/cm" if ppm else "uS/cm"
    print(f"\nLecture entree en {src} | EC pleine force = {params['ec_pleine_force']} mS/cm | "
          f"eau de base = {params['eau_base_uS']:.0f} uS/cm\n")
    for r in rows:
        print(f"{r['tour']}  EC actuel {r['ec_i_us']:.0f}  ->  cible {r['ec_d_us']:.0f} uS/cm")
        print(f"     {action_text(r)}")
    print(f"\nOrdre d'ajout : dissoudre Part 1 + Part 2, puis Part 3 en dernier. "
          f"pH {params['ph_cible_min']:.1f}-{params['ph_cible_max']:.1f}.")
    print("Re-mesurer apres coup et relancer si on n'est pas dans la cible.\n")

# ---------------------------------------------------------------- SVG image
def esc(s):
    return html.escape(str(s))

def svg(comps, params, rows):
    W = 940
    H = 470 + len(rows) * 70 + 200
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="Segoe UI, Arial, sans-serif">']
    s.append(f'<rect width="{W}" height="{H}" fill="#f7faf5"/>')
    s.append('<rect x="0" y="0" width="940" height="92" fill="#2e7d32"/>')
    s.append('<text x="40" y="46" fill="#ffffff" font-size="30" font-weight="700">'
             'Feuille de calcul des nutriments — Tower Garden</text>')
    s.append('<text x="40" y="76" fill="#d7f0d2" font-size="17">'
             'Masterblend (Gecko Grow) • ratio 2:1:2 • EC en µS/cm • ajout ou dilution selon l’écart</text>')

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
             'Action par tour</text>')
    s.append(f'<text x="40" y="{y+26}" font-size="15" fill="#555">'
             f'Réservoir {rows[0]["gallons"]:.0f} gal US = {rows[0]["litres"]:.1f} L • EC en µS/cm • '
             f'pleine force = {params["ec_pleine_force"]:.2f} mS/cm • eau de base = {params["eau_base_uS"]:.0f} µS/cm</text>')
    ty = y + 50
    cols = [("Tour", 70), ("EC actuel\n(µS)", 110), ("EC cible\n(µS)", 110), ("À faire", 510)]
    x0 = 40
    s.append(f'<rect x="{x0}" y="{ty}" width="800" height="56" fill="#2e7d32"/>')
    cx = x0
    for name, w in cols:
        parts = name.split("\n")
        for j, p in enumerate(parts):
            anchor = "middle" if name != "À faire" else "start"
            tx = cx + (w/2 if anchor == "middle" else 16)
            s.append(f'<text x="{tx}" y="{ty+(24 if len(parts)==1 else 22)+j*18}" '
                     f'font-size="14" font-weight="700" fill="#fff" text-anchor="{anchor}">{esc(p)}</text>')
        cx += w
    ry = ty + 56
    rh = 70
    colmap = {"ajouter": "#eef6ea", "diluer": "#fdecea", "ok": "#eef2f7"}
    for r in rows:
        s.append(f'<rect x="{x0}" y="{ry}" width="800" height="{rh}" fill="{colmap[r["action"]]}" stroke="#e0e8db"/>')
        s.append(f'<text x="{x0+35}" y="{ry+rh/2+6}" font-size="20" font-weight="700" fill="#222" text-anchor="middle">{esc(r["tour"])}</text>')
        s.append(f'<text x="{x0+125}" y="{ry+rh/2+6}" font-size="18" fill="#222" text-anchor="middle">{r["ec_i_us"]:.0f}</text>')
        s.append(f'<text x="{x0+235}" y="{ry+rh/2+6}" font-size="18" fill="#222" text-anchor="middle">{r["ec_d_us"]:.0f}</text>')
        verb = {"ajouter": "AJOUTER", "diluer": "DILUER", "ok": "OK"}[r["action"]]
        vcol = {"ajouter": "#2e7d32", "diluer": "#c62828", "ok": "#5b6b7a"}[r["action"]]
        s.append(f'<text x="{x0+306}" y="{ry+30}" font-size="15" font-weight="700" fill="{vcol}">{verb}</text>')
        if r["action"] == "ajouter":
            g = r["g"]
            detail = f'MB {g["masterblend"]:.1f} g • SulfMg {g["sulfate_magnesium"]:.1f} g • NitrCa {g["nitrate_calcium"]:.1f} g'
        elif r["action"] == "diluer":
            detail = f'retirer {r["litres_dil"]:.1f} L → remplacer par eau fraîche'
        else:
            detail = "dans la tolérance, ne rien faire"
        s.append(f'<text x="{x0+390}" y="{ry+30}" font-size="15" fill="#333">{esc(detail)}</text>')
        ry += rh

    fy = ry + 30
    s.append(f'<rect x="40" y="{fy}" width="860" height="120" rx="10" fill="#ffffff" stroke="#cde0c6"/>')
    s.append(f'<text x="62" y="{fy+30}" font-size="18" font-weight="700" fill="#2e7d32">Formules</text>')
    s.append(f'<text x="62" y="{fy+58}" font-size="15" fill="#333">'
             'Ajout : grammes = g/L (pleine force) × litres × (EC cible − EC actuel) ÷ EC pleine force</text>')
    s.append(f'<text x="62" y="{fy+82}" font-size="15" fill="#333">'
             'Dilution : litres à retirer = volume × (EC actuel − EC cible) ÷ (EC actuel − EC eau de base)</text>')
    s.append(f'<text x="62" y="{fy+106}" font-size="14" fill="#666">'
             'Sulfate Mg = moitié du Masterblend • Nitrate Ca = égal au Masterblend</text>')
    s.append(f'<text x="40" y="{H-22}" font-size="13" fill="#999">'
             'Généré par outils/calcul_nutriments.py — EC actuelle fournie en argument (µS/cm, ou --ppm).</text>')
    s.append('</svg>')
    out = os.path.join(ROOT, "docs", "feuille_calcul_nutriments.svg")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(s))
    return out

if __name__ == "__main__":
    tours = load_csv("tours.csv")
    params0 = load_params()
    pairs, ppm = parse_args(sys.argv[1:], tours, params0)
    comps, params, rows = compute(pairs)
    print_table(comps, params, rows, ppm)
    path = svg(comps, params, rows)
    print(f"Image generee : {os.path.relpath(path, ROOT)}")
