# Unites des parametres de culture

Les valeurs de `data/parametres_culture.csv` sont des cibles pratiques pour culture hydroponique en tour. Elles servent a planifier et comparer les cultures, pas a remplacer l'observation des plants.

## Colonnes

- `ph_min`, `ph_max`, `ph_optimal` : pH de la solution nutritive.
- `ec_min_ms_cm`, `ec_max_ms_cm`, `ec_optimal_ms_cm` : conductivite electrique en mS/cm.
- `humidite_min_pct`, `humidite_max_pct`, `humidite_optimale_pct` : humidite relative de l'air.
- `temp_min_c`, `temp_max_c`, `temp_optimale_c` : temperature de l'air en degres Celsius.
- `lumiere_min_h`, `lumiere_max_h`, `lumiere_optimale_h` : photoperiode recommandee par jour.
- `lux_min`, `lux_max`, `lux_optimal` : intensite lumineuse approximative en lux.

## Colonnes de delais et de hauteur (data/semences.csv)

- `jours_germination` : jours estimes entre le semis et la levee.
- `jours_semis_transplant` : jours entre le semis et le moment ou le plant est pret a
  transferer en tour (inclut la germination).
- `jours_transplant_recolte` : jours entre le transfert et la premiere recolte.
- `cycle_estime_jours` : cycle total semis -> premiere recolte
  (= `jours_semis_transplant` + `jours_transplant_recolte`).
- `hauteur_cm_estimee` : hauteur adulte approximative en cm (sur tour, avec support pour les
  grimpants).
- `port_preference` : niveau conseille selon la hauteur (bas <= 30 cm, milieu 31-70, haut > 70),
  utilise pour le placement par hauteur (voir guide section 12).
- `graines_par_cube` : nombre de graines a semer par cube de laine de roche. Regle : plus la
  graine est grosse, moins on en met. Gros fruits (tomate, piment, courge) = 1 ; concombre,
  pois, haricots = 1-2 ; brassicas et laitues pommees = 1-2 ; epinard = 2-3 ; herbes fines et
  roquette/melange = 6-8 ; ciboulette = 20-30 ; oignon a botteler = 10-12. Eclaircir apres
  levee si plusieurs plantules dans un cube destine a un plant unique.

Ces valeurs sont des estimations aeroponiques ; l'aeroponie peut etre ~10-20 % plus rapide que
le sol. Le plan calcule `date_transfert_estimee` = date de semis + `jours_semis_transplant` et
`date_recolte_prevue` = date de semis + `cycle_estime_jours`.

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

