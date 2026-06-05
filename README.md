# Tower Garden - Gestion personnelle

Ce projet sert a gerer 3 tours Tower Garden, l'inventaire des semences, les plantations, les recoltes et l'optimisation pour la consommation personnelle.

## Structure

- `data/semences.csv` : inventaire des semences disponibles.
- `data/tours.csv` : description des 3 tours et capacite de planification.
- `data/emplacements.csv` : grille des emplacements de plantation par tour.
- `data/plantations.csv` : suivi des semis, transplantations, et statuts.
- `data/recoltes.csv` : suivi des recoltes par culture.
- `data/consommation.csv` : besoins personnels et quantites consommees.
- `data/preferences.csv` : priorites de culture pour optimiser ce que tu manges vraiment.
- `data/parametres_culture.csv` : pH, EC, humidite, temperature et lumiere par semence.
- `planning/plan_cycle_courant.csv` : plan de plantation actif.
- `docs/strategie_optimisation.md` : methode pour choisir quoi planter.
- `docs/routine_entretien.md` : routine de suivi hebdomadaire.
- `docs/unites_parametres_culture.md` : explication des unites et de la conversion lux/lumens.
- `docs/sources_parametres_culture.md` : references utilisees pour les fourchettes de culture.
- `archives/` : anciens cycles, photos, exports ou notes.

## Utilisation suggeree

1. Verifier `data/tours.csv` pour confirmer quelles 2 tours ont des supports pour plantes grimpantes.
2. Remplir `data/preferences.csv` avec tes priorites et tes besoins hebdomadaires.
3. Planifier le cycle dans `planning/plan_cycle_courant.csv`.
4. A chaque plantation, ajouter une ligne dans `data/plantations.csv`.
5. A chaque recolte, ajouter une ligne dans `data/recoltes.csv`.
6. Une fois par semaine, comparer `recoltes.csv` et `consommation.csv` pour ajuster les prochaines plantations.

## Principe d'optimisation

L'objectif est de reserver les emplacements aux cultures qui maximisent :

- la consommation personnelle reelle;
- la frequence de recolte;
- la valeur culinaire;
- la compatibilite avec une tour hydroponique;
- la presence d'un support pour les cultures grimpantes;
- la diversite, pour eviter 18 laitues en meme temps.
