# Routine d'entretien

Les cibles pH, EC, temperature et lumiere par tour sont definies dans
`docs/guide_implantation_interieur.md` section 4 (bandes EC : T1 1.2-1.5, T2 1.6-1.9,
T3 2.0-2.4). Les tours fonctionnent a l'annee : cette routine se poursuit en continu, pas
seulement pendant le cycle de demarrage de 12 semaines.

## Chaque jour ou presque

- Observer les plants faibles, jaunis ou trop ombrages.
- Verifier que les plants fruitiers sont bien supportes.
- Recolter les feuilles exterieures au besoin.

## Chaque semaine

- Ajouter les recoltes dans `data/recoltes.csv`.
- Ajouter la consommation dans `data/consommation.csv` si tu veux mesurer l'autonomie alimentaire.
- Verifier les emplacements libres dans `data/emplacements.csv`.
- Planifier les prochains semis dans `planning/plan_cycle_courant.csv`.

## Chaque cycle

- Archiver l'ancien plan dans `archives/`.
- Garder les cultures qui ont donne un bon ratio effort/recolte.
- Reduire les cultures peu consommees ou trop volumineuses.
- Ajuster `data/preferences.csv` selon ce que tu as reellement mange.

