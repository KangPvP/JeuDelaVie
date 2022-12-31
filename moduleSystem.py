import pygame
import sys
import random
import copy

def lecture(nom_fic):
    """Cette fonction prend en paramètre :
    - une chaine de caractères désignant un nom de fichier (sans l'extension .txt)
    Elle renvoie une liste de liste automate contenant des 0 et des 1 avec :
    automate[l][c] contient 0 si la case de la ligne l et de la colonne c représente une cellule morte et 1 si elle c'est une cellule vivante.
    """
    # Ouverture du fichier en mode lecture ('read')
    fichier = open(nom_fic + '.txt', 'r')
    tempo = []
    # Parcours des lignes du fichier :
    for ligne in fichier:
        # On ajoute à automate la ligne :
        # - débarassée des espaces superflus (strip())
        # - transformée en liste de caractères (list( ... ))
        tempo.append(list(ligne.strip()))
    # Fermeture du fichier :
    fichier.close()
    # Conversion des éléments en 0/1 à la place de '0'/'1'
    automate = [ [ int(tempo[l][c]) for c in range(len(tempo[l])) ] for l in range(len(tempo))]

    return automate

# Fonction d'écriture de fichier
def ecriture(nom_fic, etape, automate):
    """
    Cette fonction écrit un fichier texte de 0 et de 1 correspondant à l'état de l'automate. Elle prend pour paramètres :
    - nom_fic : chaine désignant la base du nom de fichier
    - etape : int
    - automate : liste de listes représentant l'automate à écrire.
    """
    # Création du nom de fichier :
    num = str(etape)
    zeros = '_'
    for i in range(4-len(num)):
        zeros += '0'
    # Ouverture du fichier :
    fichier = open(nom_fic + zeros + num + '.txt', 'w')
    # Récupération des dimensions :
    largeur = len(automate[0])
    hauteur = len(automate)
    # Ecriture :
    for l in range(hauteur):
        for c in range(largeur):
            fichier.write(str(automate[l][c]))
        # Passage à la ligne :
        fichier.write('\n')
    fichier.close()


# Fonction qui calcule le nombre de voisins vivants de chaque cellule
def compte_voisins(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle renvoie une liste de listes voisins telle que :
    voisins[l][c] contient le nombre de cellules voisines vivantes autour de la cellule de la ligne l et de la colonne c.
    """

    voisins = [ [] for c in range(len(automate))]
    for i in range(len(automate)):
        for y in range(len(automate[i])):
            tabSave = []

            #Comment palier au problème out of rang
            if i == 0 :
                if y == 0:
                    tabSave.append(automate[i][y+1])

                    tabSave.append(automate[i+1][y])
                    tabSave.append(automate[i+1][y+1])

                elif y == len(automate[i])-1:
                    tabSave.append(automate[i][y-1])

                    tabSave.append(automate[i+1][y-1])
                    tabSave.append(automate[i+1][y])

                else:
                    tabSave.append(automate[i][y-1])
                    tabSave.append(automate[i][y+1])

                    tabSave.append(automate[i+1][y-1])
                    tabSave.append(automate[i+1][y])
                    tabSave.append(automate[i+1][y+1])

            elif i == len(automate)-1:
                if y == 0:
                    tabSave.append(automate[i-1][y])
                    tabSave.append(automate[i-1][y+1])

                    tabSave.append(automate[i][y+1])

                elif y == len(automate[i])-1:
                    tabSave.append(automate[i-1][y])
                    tabSave.append(automate[i-1][y-1])

                    tabSave.append(automate[i][y-1])
                else:
                    tabSave.append(automate[i-1][y-1])
                    tabSave.append(automate[i-1][y])
                    tabSave.append(automate[i-1][y+1])

                    tabSave.append(automate[i][y-1])
                    tabSave.append(automate[i][y+1])

            else :
                if y == 0:
                    tabSave.append(automate[i-1][y])
                    tabSave.append(automate[i-1][y+1])

                    tabSave.append(automate[i][y+1])

                    tabSave.append(automate[i+1][y])
                    tabSave.append(automate[i+1][y+1])


                elif y == len(automate[i])-1:
                    tabSave.append(automate[i-1][y-1])
                    tabSave.append(automate[i-1][y])

                    tabSave.append(automate[i][y-1])

                    tabSave.append(automate[i+1][y-1])

                else:
                    tabSave.append(automate[i-1][y-1])
                    tabSave.append(automate[i-1][y])
                    tabSave.append(automate[i-1][y+1])

                    tabSave.append(automate[i][y-1])
                    tabSave.append(automate[i][y+1])

                    tabSave.append(automate[i+1][y-1])
                    tabSave.append(automate[i+1][y])
                    tabSave.append(automate[i+1][y+1])

            x = tabSave.count(1)

            voisins[i].append(x)

    return voisins

# Fonction de calcul de l'étape suivante
def calcul_etape(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle modifie la liste de listes automate représentant l'automate à l'étape suivante selon la règle :
    - si, à l'étape n, une cellule morte est entourée d'exactement 3 cellules vivantes, elle devient vivante à l'étape n+1
    - si, à l'étape n, une cellule vivante est entourée de 2 ou 3 cellules vivantes, elle reste vivante à l'étape n+1 et elle meurt sinon.
    Cette fonction renvoie un booléen indiquant si l'automate a été modifié
    """

    newAutomate = copy.deepcopy(automate)
    automateVoisin = compte_voisins(automate)

    for i in range(len(automate)):
        for y in range(len(automate[i])):
            etatCellule = automate[i][y]
            nbVoisin = automateVoisin[i][y]
            #Comment modifier un list
            if etatCellule == 0:
                if nbVoisin == 3:
                    newAutomate[i][y] = 1
                else:
                    newAutomate[i][y] = 0
            else:
                if nbVoisin == 2 or nbVoisin == 3:
                    newAutomate[i][y] = 1
                else:
                    newAutomate[i][y] = 0

    if automate == newAutomate:
        return (False, newAutomate)
    else:
        return (True, newAutomate)

def crea_map_alea(lignes, colonnes, nom_fic, proba = .5):
    """Cette fonction prend en paramètres :
    - deux entiers lignes et colonnes désignant le nombre de lignes et de colonnes de la map à générer
    - un nom de fichier (sans extension) sous la forme d'une chaine
    - une proba indiquant la probabilité de créer une cellule vivante
    Elle créer la map aléatoirement qu'elle stocke dans le fichier (avec l'exetnsion .txt)
    """
    # Ouverture d'un fichier texte en mode écriture ('w'rite)
    fichier = open(nom_fic + '.txt', 'w')
    # Pour écrire un '1' dans le fichier on écrit :
    # fichier.write('1')
    # Pour écrire un saut de ligne, on écrit :
    #fichier.write('\n')

    for nbLigne in range(lignes):
        for nbIndex in range(colonnes):
            value = random.randint(1,proba)

            if value == 1:
                fichier.write('1')
            else:
                fichier.write('0')

        fichier.write('\n')

    # On ferme le fichier :
    fichier.close()

def calDataAutomate(largeur, hauteur): #Calcule de données relative a un Automate
    xm, ym = 500, 500

    case = xm // max(hauteur, largeur)
    x0 = 50 + (xm - case * largeur) // 2
    y0 = 50 + (ym - case * hauteur) // 2

    return x0, y0, case

def affiche_graphique(a, x0, y0, cote, f):
    hauteur = len(a)
    largeur = len(a[0])
    pygame.draw.rect(f, (0, 0, 0), [x0-5, y0 -5, cote*largeur+10, cote*hauteur+10])
    for l in range(hauteur):
        for c in range(largeur):
            if a[l][c] == 1:
                pygame.draw.rect(f, (0,255,0), [x0 + c*cote+1, y0+l*cote+1,cote-2,cote-2])
            else:
                pygame.draw.rect(f, (255,0,0), [x0 + c*cote+1, y0+l*cote+1,cote-2,cote-2])


#Fonction qui permet de dessiner un boutton UP ou Down
def upButton(fenetre, x,y,up):
    rectangle = pygame.Rect(x,y,40,31)
    xSize, ySize = rectangle.size

    pygame.draw.rect(fenetre, (180, 180, 180), rectangle, 0, 6)  # fond BTN
    pygame.draw.rect(fenetre, (50, 50, 50), rectangle, 2, 6)  # contour BTN

    if up:
        pygame.draw.polygon(fenetre, (50,50,50), [(x + 5, y + ySize - 9), (x + xSize / 2, y + 6), (x + xSize - 5, y + ySize - 9)]) #element BTN
    else:
        pygame.draw.polygon(fenetre, (50, 50, 50), [(x + 5, y + 9), (x + xSize / 2, y + ySize - 6),(x + xSize - 5, y + 9)])  # element BTN
    return rectangle


