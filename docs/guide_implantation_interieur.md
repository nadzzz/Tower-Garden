# Guide d'implantation interieur - Tower Garden

Cycle de demarrage guide : du lundi 8 juin 2026 au vendredi 28 aout 2026.

Ce calendrier de 12 semaines sert a prendre la routine en main. Ce n'est pas la duree de
vie du systeme : les 3 tours fonctionnent a l'annee. Apres la semaine 12, la meme routine
(lundi/vendredi/fin de semaine) se poursuit en continu avec succession permanente (voir la
section 11).

Disponibilites prevues :

- lundi : grosses decisions et travaux principaux;
- vendredi : mesures, validation et ajustements;
- fin de semaine : observation courte, recolte legere, ajout d'eau.

## 1. Avant de semer

Preparer :

- cubes de laine de roche;
- etiquettes;
- eau ajustee a pH 5.8-6.2;
- plateau de semis;
- lumiere douce apres germination;
- carnet ou fichiers de suivi.

Temps estime le 8 juin : 90 a 120 minutes.

Regle importante : les cubes doivent rester humides, mais jamais detrempes. S'ils sont trop mouilles, les racines manquent d'air.

## 2. Semis

Semer selon `planning/plan_ensemencement.csv`.

Semis principaux du 8 juin :

- laitues;
- roquette;
- basilics;
- coriandre;
- pak-choi;
- kale;
- bette a carde;
- pois mange-tout;
- tomates cerises;
- piments;
- concombres Marketmore;
- courge test.

Semis de succession :

- 15 juin : vague 2 de laitues, roquette, basilic, coriandre, pak-choi;
- 22 juin : vague 3 de laitues et roquette.

## 3. Conditions de transfert

Ne transferer en tour que si toutes ces conditions sont reunies :

- racines visibles sous ou autour du cube;
- plant non etiole;
- plant ferme, pas couche;
- 2 vraies feuilles pour laitues, roquette, pak-choi;
- plant vigoureux pour tomates, concombres, piments et courge;
- tour stabilisee depuis quelques heures avec pH et EC dans la cible.

Si un plant est douteux, reporter au prochain lundi ou vendredi. Un transfert retarde est souvent meilleur qu'un plant stresse.

## 4. Cibles par tour

Chaque tour a un seul reservoir, donc une seule EC et un seul pH pour toutes les cultures
qu'elle porte. Les cultures sont regroupees par bande EC compatible pour eviter de sur- ou
sous-nourrir une partie de la tour.

### T1 - Feuilles rapides et aromates douces (bande EC basse, sans support)

- pH : 6.0
- EC : 1.2-1.5 mS/cm
- lumiere : 12-16 h/jour
- intensite : 12 000-25 000 lux
- temperature : idealement 18-22 C

Cultures : laitues, roquette, basilic, coriandre, persil, moutarde. T1 doit rester douce :
ces cultures souffrent vite d'une EC trop forte.

### T2 - Feuilles productives et grimpantes legeres (bande EC moyenne, support)

- pH : 6.2
- EC : 1.6-1.9 mS/cm
- lumiere : 14-16 h/jour
- intensite : 20 000-35 000 lux
- temperature : idealement 16-22 C

Cultures : pois mange-tout, kale, bette a carde, pak-choi, ciboulette, oignon a botteler.
T2 utilise les supports pour les pois. Garder les pois attaches sans serrer. La bette accepte
le haut de la bande EC (~1.8-2.0).

### T3 - Fruits et supports (bande EC haute, support)

- pH : 6.0-6.2
- EC : 2.0-2.4 mS/cm
- lumiere : 14-16 h/jour
- intensite : 30 000-60 000 lux
- temperature : idealement 21-27 C

Cultures : tomate cerise, concombre, piments, courge (test), haricots si desire. Eviter une
photoperiode au-dela de 16 h, qui peut causer une chlorose de lumiere continue sur tomate.
T3 doit rester peu dense : garder au moins 40 % des emplacements libres pour donner lumiere
et air aux tomates, concombres et piments.

## 5. Quoi faire si les conditions sortent des cibles

### pH trop bas

Action :

- corriger doucement avec pH up;
- attendre que la solution circule;
- revalider avant de transferer des plants.

Ne pas faire de correction brutale.

### pH trop haut

Action :

- corriger doucement avec pH down;
- attendre circulation complete;
- revalider.

### EC trop basse

Action :

- ajouter nutriments graduellement;
- viser le bas de la fourchette pour jeunes plants;
- revalider apres circulation.

### EC trop haute

Action :

- diluer avec eau pH ajustee;
- revalider;
- surveiller les laitues, qui reagissent vite a une EC trop forte.

### Lumiere insuffisante

Signes :

- plantules longues et faibles;
- feuilles pale;
- plants qui penchent vers la lampe;
- peu de fleurs sur fruits.

Action :

- rapprocher ou augmenter les lampes;
- allonger la photoperiode dans la plage cible;
- reduire densite, surtout dans T3.

### Temperature trop haute

Signes :

- laitues molles;
- roquette plus amere;
- coriandre qui monte vite;
- humidite excessive.

Action :

- augmenter ventilation;
- eloigner legerement lampes;
- recolter plus jeune les feuilles sensibles.

### Humidite trop haute

Action :

- augmenter circulation d'air;
- eviter feuillage trop dense;
- retirer feuilles mortes.

## 6. Pollinisation manuelle

Faire surtout le vendredi, puis verifier le lundi.

### Tomates

- choisir des fleurs ouvertes;
- vibrer doucement la grappe florale;
- repeter 2-3 fois par semaine si beaucoup de fleurs.

### Piments

- tapoter doucement les fleurs ouvertes;
- un petit pinceau sec peut aider;
- eviter de mouiller les fleurs.

### Concombres

- identifier une fleur male : tige fine, pas de mini-concombre a la base;
- identifier une fleur femelle : mini-concombre derriere la fleur;
- transferer le pollen de la fleur male vers la fleur femelle avec pinceau ou contact direct.

### Courge test

- meme principe que le concombre;
- si la courge prend trop d'espace ou fait trop d'ombre, la retirer.

## 7. Routine du lundi

Temps typique : 45 a 90 minutes.

Faire :

- lire `planning/calendrier_implantation_12_semaines.csv`;
- mesurer pH et EC;
- verifier temperature, humidite et lumiere;
- semer ou transferer selon le calendrier;
- tailler legerement tomates, concombres et basilics;
- guider pois, tomates et concombres;
- mettre a jour les statuts dans `planning/plan_cycle_courant.csv`.

## 8. Routine du vendredi

Temps typique : 30 a 60 minutes.

Faire :

- mesurer pH et EC;
- verifier niveau d'eau;
- inspecter racines et feuilles;
- valider reprise des plants transferes;
- polliniser si fleurs presentes;
- recolter legerement;
- noter les recoltes dans `data/recoltes.csv`.

## 9. Routine de fin de semaine

Temps typique : 15 a 30 minutes.

Faire seulement :

- observation rapide;
- ajout d'eau si necessaire;
- recolte legere;
- noter un probleme si quelque chose change vite.

Eviter les gros changements la fin de semaine, sauf urgence.

## 10. Decisions rapides

Si moins de 4 portions de salade par semaine :

- utiliser une reserve T1 pour laitue ou roquette.

Si plus de 7 portions sont consommees :

- augmenter les semis de succession de 2 cubes.

Si les pois sont tres apprecies :

- utiliser 1 ou 2 reserves T2 pour pois, seulement si le support et la lumiere sont suffisants.

Si T3 devient dense :

- retirer la courge en premier;
- tailler concombres ensuite;
- garder tomates et jalapenos comme priorite.

Si une culture echoue :

- noter la cause probable;
- remplacer par laitue, roquette, basilic ou pak-choi selon la tour.

## 11. Apres la semaine 12 - conduite a l'annee

Le calendrier de 12 semaines est un guide de demarrage, pas une fin. Les tours restent en
production toute l'annee. Une fois la routine maitrisee :

- continuer la succession sans arret : des qu'un emplacement se libere, resemer selon la
  bande EC de la tour (T1 feuilles/aromates, T2 feuilles robustes/pois, T3 fruits);
- les cultures longues (tomate cerise, cayenne, habanero) fructifient apres la semaine 12;
  c'est normal, les garder en production tant qu'elles donnent;
- caler les cultures de saison fraiche (pois, coriandre, epinard) sur les periodes moins
  chaudes; en ete interieur, recolter plus jeune et surveiller la montaison;
- en hiver, maintenir la photoperiode cible avec les lampes (les jours courts ne suffisent
  pas) et surveiller une eau de reservoir plus froide;
- a chaque fin de cycle, archiver le plan dans `archives/` et ajuster `data/preferences.csv`
  et `planning/scores_cultures.csv` selon ce qui a ete reellement mange.

