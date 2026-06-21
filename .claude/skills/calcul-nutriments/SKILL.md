---
name: calcul-nutriments
description: Calcule le mélange de nutriments Masterblend (Gecko Grow) à peser pour une ou plusieurs tours du Tower Garden, à partir de l'EC initial mesurée. Utiliser quand l'utilisateur demande la recette/dose/quantité de nutriments, combien de grammes de Masterblend / sulfate de magnésium / nitrate de calcium ajouter, ou comment ajuster l'EC d'un réservoir de tour.
---

# Calcul des nutriments des tours

Ce skill calcule, pour chaque tour, les grammes de Part 1 (Masterblend), Part 2
(sulfate de magnésium) et Part 3 (nitrate de calcium) à peser pour passer de l'EC
**initiale mesurée** à l'EC **désirée** de la tour.

Toute la logique est dans `outils/calcul_nutriments.py`. **Ne pas réimplémenter le
calcul** : appeler le script.

## Données utilisées

- `data/tours.csv` — volume (gallons) et `ec_desire_ms_cm` de chaque tour.
- `data/recette_nutriments.csv` — recette Masterblend (ratio 2:1:2, g/L pleine force, ordre).
- `data/parametres_recette.csv` — `ec_pleine_force` (calibration), `litres_par_gallon`, plage de pH.

L'**EC initiale n'est PAS stockée** : elle est fournie en argument au moment du calcul.

## Marche à suivre

1. Demander à l'utilisateur l'**EC initiale mesurée** de chaque tour concernée
   (et quelles tours), s'il ne l'a pas déjà donnée.
2. Lancer le script avec des paires `TOUR EC_INITIAL` :

   ```
   py outils/calcul_nutriments.py T1 0.45
   py outils/calcul_nutriments.py T1 0.45 T2 0.50 T3 0.62
   ```

3. Présenter le tableau retourné (grammes par part et par tour).
4. Rappeler l'ordre de mélange : dissoudre **Part 1 + Part 2** d'abord, puis ajouter
   **Part 3 en dernier**, et ajuster le pH dans la plage 5,5–6,5.
5. Le script régénère aussi l'image `docs/feuille_calcul_nutriments.svg`.

## Notes

- Si `ΔEC ≤ 0` (EC initiale déjà ≥ désirée), il n'y a rien à ajouter — l'expliquer
  plutôt que de proposer une dose.
- `ec_pleine_force` (dans `parametres_recette.csv`) est une **calibration** : après le
  premier mélange à pleine force, mesurer l'EC réelle et mettre à jour cette valeur
  pour rendre les calculs exacts.
- Réservoir Tower Garden = **20 gallons US** (75,7 L). La conversion `litres_par_gallon`
  est fixée à 3.78541 (gallon US) dans `parametres_recette.csv`.
- Accepte la virgule ou le point pour l'EC (`0,45` ou `0.45`).
