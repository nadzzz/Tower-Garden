# Unites des parametres de culture

Les valeurs de `data/parametres_culture.csv` sont des cibles pratiques pour culture hydroponique en tour. Elles servent a planifier et comparer les cultures, pas a remplacer l'observation des plants.

## Colonnes

- `ph_min`, `ph_max`, `ph_optimal` : pH de la solution nutritive.
- `ec_min_ms_cm`, `ec_max_ms_cm`, `ec_optimal_ms_cm` : conductivite electrique en mS/cm.
- `humidite_min_pct`, `humidite_max_pct`, `humidite_optimale_pct` : humidite relative de l'air.
- `temp_min_c`, `temp_max_c`, `temp_optimale_c` : temperature de l'air en degres Celsius.
- `lumiere_min_h`, `lumiere_max_h`, `lumiere_optimale_h` : photoperiode recommandee par jour.
- `lux_min`, `lux_max`, `lux_optimal` : intensite lumineuse approximative en lux.

## Lumens et lux

Les lumens mesurent la lumiere totale produite par une lampe. Les lux mesurent les lumens recus par une surface.

Formule :

`lux = lumens / metres_carres`

Donc :

`lumens necessaires = lux_cible * surface_eclairee_m2`

Exemple : pour viser 20 000 lux sur 0,5 m2, il faut environ 10 000 lumens utiles sur la canopee.

## Notes importantes

- Pour les plantes, le PPFD et le DLI sont plus precis que les lumens, mais les lux restent utiles avec un luxmetre simple.
- Les jeunes plants demandent souvent une EC plus basse que les plants matures.
- Dans une tour avec reservoir partage, viser un compromis stable est souvent meilleur qu'un optimum parfait pour une seule culture.
- Les cultures fruitieres aiment generalement plus de lumiere et une EC plus haute que les laitues.
- Les laitues, roquettes, coriandre et epinards souffrent plus vite de la chaleur.

