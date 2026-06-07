# Tower Garden - Gestion personnelle

Ce projet sert a gerer 3 tours Tower Garden, l'inventaire des semences, les plantations, les recoltes et l'optimisation pour la consommation personnelle.

## Structure

- `data/semences.csv` : inventaire des semences (avec delais de croissance par etape, hauteur estimee et port conseille).
- `data/tours.csv` : description des 3 tours et capacite de planification.
- `data/emplacements.csv` : grille des 84 ports de tour, peuplee en miroir du plan projete (culture prevue, statut, lien plantation_id).
- `data/plantations.csv` : suivi des semis, transplantations, et statuts.
- `data/recoltes.csv` : suivi des recoltes par culture.
- `data/consommation.csv` : besoins personnels et quantites consommees.
- `data/preferences.csv` : priorites de culture pour optimiser ce que tu manges vraiment.
- `data/parametres_culture.csv` : pH, EC, humidite, temperature et lumiere par semence.
- `planning/plan_cycle_courant.csv` : plan de plantation actif.
- `planning/calendrier_implantation_12_semaines.csv` : calendrier guide du cycle interieur.
- `planning/checklist_lundi_vendredi.csv` : routine de validation lundi/vendredi.
- `planning/plan_ensemencement.csv` : semis, quantites et dates de transfert estimees.
- `planning/ponderation_cultures.csv` : poids des criteres de decision.
- `planning/scores_cultures.csv` : scores par culture pour orchestrer les choix.
- `docs/strategie_optimisation.md` : methode pour choisir quoi planter.
- `docs/routine_entretien.md` : routine de suivi hebdomadaire.
- `docs/unites_parametres_culture.md` : explication des unites et de la conversion lux/lumens.
- `docs/sources_parametres_culture.md` : references utilisees pour les fourchettes de culture.
- `docs/guide_implantation_interieur.md` : guide pratique pour le cycle interieur.
- `archives/` : anciens cycles, photos, exports ou notes.

## Flux des fichiers (eviter la duplication)

Trois fichiers se ressemblent ; chacun a un role distinct :

- `planning/plan_cycle_courant.csv` : **le plan** (source de verite de la planification).
  Il dit quelle culture va dans quel emplacement, a quelle vague. Les cultures y sont
  regroupees par bande EC compatible avec chaque tour (voir le guide section 4).
- `data/plantations.csv` : **le journal reel** des semis et transplantations. On y ajoute
  une ligne quand l'action est vraiment faite (dates et statut reels). La colonne
  `tour_id`/`emplacement_id` donne le **lieu courant** du plant ; tant qu'il germine, ce lieu
  est la mini-serre (voir codes de lieu ci-dessous), et le spot de tour prevu est rappele dans
  `notes` (« prevu T1-N7-P1 »).
- `data/emplacements.csv` : **grille des 84 ports de tour** (3 x 7 x 4), peuplee comme **miroir
  du plan projete**. Pour chaque port : `culture_planifiee`, `statut`
  (`en_germination` si un plant lui est deja attribue, `planifie` pour une vague a venir,
  `reserve` sinon) et `plantation_id` qui **relie** le port au plant correspondant de
  `plantations.csv`. En cas de doute, `plan_cycle_courant.csv` fait foi.

### Codes de lieu (lieu courant dans `plantations.csv`)

- `GERM` = **mini-serre de germination** (bac a couvercle dome sur tapis chauffant), avec deux
  zones : `GERM-TIEDE` (cote tapis : fruits et basilic) et `GERM-FRAIS` (le reste).
- `T1`/`T2`/`T3` + `emplacement_id` (ex. `T2-N7-P1`) = une fois transplante en tour.

Au transfert : passer `statut` a `en_tour`, mettre `tour_id`/`emplacement_id` au vrai port,
remplir `date_transplantation`, et mettre a jour le `statut` du port dans `emplacements.csv`.

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
