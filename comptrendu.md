#  Projet 2 : Jeu de la vie
## Carnet de bord

----
:::info
Noms des participants :
* Mathieu Jacques
* Titouan Lefeur
* Timeo Ripaul
* Hugo
:::


Tout ce qu'on a déjà fait :
- [x] choisir le projet
- [x] écrire le code
- [x] codez l'interface graphique
- [x] écrire le carnet de bord


Nous avons travaillé en équipe pour développer un jeu de la vie.
Au cours de ces fonctions, nous avons rencontrer de nombreux problême, nous allons
donc vous expliquer quel était il et comment avons nous fait pour y faire face

## Tout d'abord la répartition du travail:

#### Pour ce projet nous avons codé un total de 10 fonctions, avec également quatre questions répondus sur un fichier odt.

Hugo a répondue au question,
Titouan et Timeo ont travaillé sur les 6 premières fonction, c'est a dire le code en python.
Mathieu a codez l'interface graphique.
Nous avons tous écris le carnet de bord.

## Passons au problème que nous avons recontrés.

### Commençons par les fonctions du code python puis les fofnctions de l'interface graphique


#### La fonction lecture,
il n y a pas eu de probleme car celle-ci était guidée. 
#### La fonction affiche(automate)
Nous avons remarqué que celle-ci ressemblait fortement a la fonction affichage(g) du projet puissance 4. En consequence celle-ci était assez facile a faire. 
#### La fonction compte_voisins(automate)
Elle paraîssait assez simple a première vue car il suffisait juste d'ajoutez les 8 cases autour de la cellule,cependant nous avons pu remarquer que cela posait problème lorsque nous devions calculer le nombre de voisins pour une cellule qui était sur un bord. Ducoup j'ai premièrement pensé à faire des cas spécifique pour chaque côté comme ceci:
```
if hauteur==0 and largeur==0:
```
Cependant le nombre de condition a faire séparement était trop grand. Nous avons donc décidé d'optimisé la fonction.
Pour cela je me suis dit qu'il fallait faire une boucle qui prenait les 8 cases et si une des cases était en dehors de la liste on ne la prenait pas.
J'ai donc effectué cette boucle avec des max si la cellule était a gauche ou en haut et des min si la cellule était a droite ou en bas et une condition qui dit que si la cellule est la même que celle dont on compte les voisins on la prend pas. Comme ceci:
```
for x in range(max(0,i-1),(min(hauteur,i+2))): 
    for y in range(max(0,j-1),(min(largeur,j+2))):
        if i != x or j != y:
```




#### La fonction Calcul_etape(automate)
Elle était assez simple, le seul probleme était que nous avons du penser a  import la fonction copy pour pouvoir faire une copy de l'automate et le modifier afin d'obtenir la prochaine étape.

#### La fonction Ecriture(nom_base,etape,automate)
Pour cette fonction nous avons confondus /n et \n ducoup nous avons passez beacoup de temps a comprendre ce qui n'allait pas alors que c'était juste un erreur d'orthographe. De plus il y avait dans les nom de fichier deux fois voir trois fois ".txt". Donc j'ai due enlever le ".txt" de la fonction lecture ainsi que celui lorsque qu'on marque le nom de la fonction et qu'on met on ne doit pas rajouter le '.txt' pour que le code marche.
#### La fonction simul_graphique(nom_base,max_fic)
Le plus compliqué dans cette fonction fut de coordonner les differentes variable des differentes fonctions et ne pas se perdre entre nom_fic et nom_base.

### Les fonctions de l'Interface Graphique

Pour les fonctions de l'interface graphique j'ai divisé en trois fonction:
calDataAutomate(largeur, hauteur), affiche_graphique(automate, x0, y0, cote, f) et simul_graphique(nom_fic).
Ce découpage était arbitraire et pouvait également être fait en une seule fontion mais nous avons trouvé plus pratique de decoupez en trois fonction.

#### La fonction calDataAutomate(largeur, hauteur)
Simplement une fonction nescessaire a affiche_graphique, nous l'avons seulement séparés pour bien calculer les points x0 et y0 avant d'afficher la grille
#### La fonction affiche_graphique(automate, x0, y0, cote, f)
Le probleme rencontré dans cette fonction était de trouver la bonne formule pour bien tracer la grille et le cadrillage.
#### La fontion simul_graphique(nom_fic)
Cette fonction est assez longue et pouvait même être sépare en sous fonction.
Nous avons commencé par une interface pygame suivit de l'affiche de la grille grâce au fonction précedente. Mais j'ai décidé de rajouter un bouton démarer, pause, stop et une variable qui montre le nb d'étape.Nous avons donc du creer 2 variable true: modifie et debut afin de pouvoir interferer sur les étapes grâce au bouton. Un des problemes de cette fonction a été que l'affichage se faisait trop rapidement en consequence j'ai due ajouter une ligne horaire.tick(1), de plus le bouton stop ne marche pas si on n'a pas mis pause a l'automate cellulaire, ce problème n'étant pas dérangeant nous l'avons laisser comme telle.

Cette fonction étant finie le projet est fonctionel.

