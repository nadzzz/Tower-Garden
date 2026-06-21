---
name: calcul-nutriments
description: Calcule l'ajustement de nutriments Masterblend (Gecko Grow) d'une ou plusieurs tours du Tower Garden à partir de l'EC mesurée — grammes à ajouter (Part 1/2/3) si on est sous la cible, ou litres à diluer si on dépasse. Utiliser quand l'utilisateur demande la recette/dose/quantité de nutriments, combien de Masterblend / sulfate de magnésium / nitrate de calcium ajouter, comment diluer, ou comment ajuster l'EC d'un réservoir de tour.
---

# Calcul des nutriments des tours

Ce skill calcule, pour chaque tour, comment passer de l'EC **actuelle mesurée** à
l'EC **cible** de la tour :
- si l'EC est **sous** la cible → grammes de Part 1 (Masterblend), Part 2 (sulfate de
  magnésium) et Part 3 (nitrate de calcium) à ajouter ;
- si l'EC **dépasse** la cible → litres à retirer et remplacer par de l'eau fraîche.

Toute la logique est dans `outils/calcul_nutriments.py`. **Ne pas réimplémenter le
calcul** : appeler le script.

## Données utilisées

- `data/tours.csv` — volume (gallons) et `ec_desire_ms_cm` de chaque tour.
- `data/recette_nutriments.csv` — recette Masterblend (ratio 2:1:2, g/L pleine force, ordre).
- `data/parametres_recette.csv` — `ec_pleine_force` (calibration), `eau_base_uS`,
  `ppm_facteur`, `litres_par_gallon`, plage de pH.

L'**EC actuelle n'est PAS stockée** : elle est fournie en argument au moment du calcul.

## Unités (important)

- Le compteur est un **VIVOSUN TDS&EC** : privilégier le **mode EC (µS/cm)** via le
  bouton MODE. Les cibles sont alors directement T1=1100, T2=1650, T3=2150 µS/cm.
- 1 mS/cm = 1000 µS/cm. Le script travaille en interne en mS/cm.
- Si l'utilisateur lit en **ppm**, ajouter l'option `--ppm` : le script convertit avec
  `ppm_facteur` (0,5 pour ce compteur → µS/cm = ppm ÷ 0,5).

## Marche à suivre

1. Demander l'**EC mesurée** de chaque tour concernée (de préférence en µS/cm) si elle
   n'est pas déjà donnée.
2. Lancer le script avec des paires `TOUR EC` :

   ```
   py outils/calcul_nutriments.py T1 1100
   py outils/calcul_nutriments.py T1 1100 T2 1650 T3 2150
   py outils/calcul_nutriments.py --ppm T1 550 T2 825 T3 1075
   ```

3. Présenter l'action par tour (ajouter X g, ou diluer X L, ou « dans la cible »).
4. Pour un ajout, rappeler l'ordre : dissoudre **Part 1 + Part 2**, puis **Part 3 en
   dernier**, et ajuster le pH à 5,5–6,5.
5. Le script régénère l'image `docs/feuille_calcul_nutriments.svg`.

## Notes

- Procéder **par itérations** : doser/diluer, bien brasser, re-mesurer, relancer avec la
  nouvelle lecture jusqu'à être dans la cible.
- `ec_pleine_force` = **2,48 mS/cm**, calibré le 2026-06-21 (VIVOSUN) : ~51 µS/cm par
  gramme de Masterblend dans 75,7 L. La remesurer si on change de sel ou d'eau.
- `eau_base_uS` (≈241) = EC de l'eau fraîche du robinet, sert au calcul de dilution.
- Si la dilution dépasse ~50 % du réservoir, suggérer plutôt de **vider et refaire un
  mélange neuf** (plus simple) : lancer le script avec l'EC de l'eau fraîche comme
  EC actuelle pour obtenir la recette de départ.
- Réservoir Tower Garden = **20 gallons US** (75,7 L), fixé via `litres_par_gallon`
  = 3.78541.
- Accepte la virgule ou le point pour l'EC.
