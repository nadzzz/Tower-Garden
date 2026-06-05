# Strategie d'optimisation

L'objectif est d'utiliser les 3 tours pour produire ce que tu consommes vraiment, avec une rotation qui evite les surplus d'un seul coup.

## Roles proposes par tour

### Tour 1 - Feuilles rapides et aromates

Cette tour sert a garder une production reguliere de salades et d'herbes.

Cultures prioritaires :

- laitues;
- roquette;
- moutarde;
- coriandre;
- basilic;
- ciboulette;
- persil.

Strategie : planter par petites vagues. Par exemple, 2 a 4 nouveaux emplacements de laitue toutes les 2 semaines au lieu de remplir toute la tour d'un coup.

### Tour 2 - Feuilles productives et grimpantes legeres

Cette tour sert aux cultures qui donnent longtemps et se recoltent feuille par feuille, avec une zone disponible pour les cultures grimpantes legeres.

Cultures prioritaires :

- kale;
- bette a carde;
- pak-choi;
- epinard;
- oignon a botteler;
- pois mange-tout;
- haricots.

Strategie : garder moins de plants, mais les maintenir productifs longtemps. Utiliser le support pour 1 a 3 cultures grimpantes legeres, sans laisser les grimpantes ombrager toute la tour.

### Tour 3 - Fruits et supports

Cette tour sert aux cultures plus longues et plus gourmandes en espace. Elle fait partie des 2 tours avec supports pour plantes grimpantes.

Cultures prioritaires :

- tomate cerise;
- concombre;
- piments;
- pois mange-tout;
- haricots.

Strategie : limiter le nombre de plants fruitiers pour eviter l'ombre et la competition. Mieux vaut 1 tomate bien conduite que 4 plants qui se nuisent.

## Score de decision

Pour choisir quoi planter, donner une note de 1 a 5 a chaque critere :

- consommation personnelle;
- rendement attendu;
- vitesse de recolte;
- compatibilite avec la tour;
- support disponible pour les cultures grimpantes;
- plaisir culinaire;
- rarete ou cout a l'achat.

Score simple :

`score = consommation + rendement + vitesse + compatibilite + support + plaisir + rarete`

Les cultures avec les scores les plus hauts passent en premier dans `planning/plan_cycle_courant.csv`.

## Regles pratiques

- Garder toujours une partie de la tour 1 en succession rapide.
- Eviter de planter toutes les laitues le meme jour.
- Reserver les plants fruitiers et grimpants aux 2 tours avec supports.
- Noter les recoltes meme approximativement; les donnees imparfaites sont deja utiles.
- Apres 4 semaines, comparer ce qui a ete recolte avec ce qui a ete mange.

## Premier plan recommande

- 35 a 45 % des emplacements : laitues, roquette, moutarde, pak-choi.
- 20 a 30 % : kale, bette a carde, epinard, oignons.
- 15 a 25 % : aromates.
- 10 a 20 % : fruits et cultures longues sur tours avec supports.

Ce ratio peut changer si ton objectif est plus "salades quotidiennes" ou plus "production estivale de fruits".
