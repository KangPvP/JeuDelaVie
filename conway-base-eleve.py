### DM : jeu de la vie de Conway

## 1NSI - Nom :

import pygame
import sys
import random
import copy

# Fonction de lecture de la situation de départ
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



# Fonction d'affichage d'un état (en mode texte)
def affiche(automate):
    """Cette fonction prend en paramètre :
    - une liste de listes de 0/1 représentant un automate cellulaire
    Elle produit un affichage où :
    - une cellule morte est représentée par un '.'
    - une cellule vivante est représentée par un 'X'
    Elle ne renvoie rien.
    """

    for i in range(len(automate)):
        argsValue = ""
        for y in range(len(automate[i])):
            if(automate[i][y] == 0):
                argsValue = argsValue + "."
            else:
                argsValue = argsValue + "x"
        print(argsValue)

    return


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


## SIMULATION - VERSION TXT + écriture dans fichiers

def simul_txt(nom_fic, max_fic=20):
    """Cette fonction simule le jeu de la vie avec :
    - nom_fic : chaine désignant le nom du fichier initial et la base des fichiers à écrire.
    - max_fic : le nombre max de fichiers à écrire (par défaut 20)
    """
    etape = 0
    automate = lecture(nom_fic)

    for y in range(max_fic+1): #nombre d'étape a exécuté

        for i in range(len(automate)): #affiche en console le contenu du fichier
            argsValue = ""
            for y in range(len(automate[i])):
                if(automate[i][y] == 0):
                    argsValue = argsValue + "0"
                else:
                    argsValue = argsValue + "1"
            print(argsValue) #affiche la ligne 1

        print("======================================") # Barre de séparation des différantes étapes

        ecriture(nom_fic, etape, automate)

        etape = etape + 1
        modifie, automate = calcul_etape(automate) #modification de l'automate précédant

        #la fonction ecriture prend 3 paramètre et simul_txt uniquement 2..


def simul_graphique(fenetre, nom_fic):
    etape = 0
    # Dimensions zone d'affichage
    xm, ym = 500, 500
    # Lecture des données de départ
    a = lecture(nom_fic)
    hauteur = len(a)
    largeur = len(a[0])

    # Position du coin haut-gauche de la première cellule et côté d'une case
    x0, y0, case = calDataAutomate(largeur, hauteur)

    fenetre.fill((255,255,255))

    # Pour le taux de rafraichissement
    framerate = 1
    horaire = pygame.time.Clock()
    horaire.tick(framerate)

    # Booléen indiquant si l'état est encore modifié à chaque étape :
    modifie = True

    affiche_graphique(a, x0, y0, case, fenetre)
    btnDemarrer, btnVUp, btnVDown = elementSimulFixe(fenetre)
    elementSimulActus(fenetre, framerate)
    pygame.display.flip()
    debut = False

    # Début de simulation
    while modifie:
        horaire = pygame.time.Clock()
        horaire.tick(framerate)

        if debut:
            modifie, a = calcul_etape(a)
            affiche_graphique(a, x0, y0, case, fenetre)
            etape = etape + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                modifie = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btnDemarrer.collidepoint(x,y):
                    if debut == False:
                        debut = True
                        btnDemarrer = pygame.Rect(0, 0, 110, 45)
                        btnDemarrer.center = (675, 150)
                        pygame.draw.rect(fenetre, (255, 255, 255), btnDemarrer)

                if btnVUp.collidepoint(x,y):
                    framerate = min(framerate + 1, 25)
                if btnVDown.collidepoint(x,y):
                    framerate = max(1, framerate - 1)
                elementSimulActus(fenetre, framerate)

        # Rafraichissement de la fenêtre
        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        texte = fonte.render('Étape ' + str(etape), True, (0,0,255), (255,255,255))
        textRect = texte.get_rect()
        textRect.center = (675,550)
        fenetre.blit(texte, textRect)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


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


def elementSimulFixe(fenetre):
    fonte = pygame.font.SysFont('Comic Sans MS', 27)
    texte = fonte.render('Jeu de la Vie', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (675,60)
    fenetre.blit(texte, textRect)

    btnDemarrer = pygame.Rect(0,0,110,45)
    btnDemarrer.center = (675,150)
    pygame.draw.rect(fenetre, (0, 255, 0), btnDemarrer,0,5)

    fonte = pygame.font.SysFont('Comic Sans MS', 21)
    texte = fonte.render('Démarrer', True, (0,0,255))
    textRect = texte.get_rect()
    textRect.center = (675,150)
    fenetre.blit(texte, textRect)

    btnVUp = upButton(fenetre, 725, 260, True)
    btnVDown = upButton(fenetre, 725,309, False)

    texte = fonte.render('Vitesse', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (625,300)
    fenetre.blit(texte, textRect)

    return btnDemarrer, btnVUp, btnVDown

def elementSimulActus(fenetre, fr):

    fonte = pygame.font.SysFont('Comic Sans MS', 25)

    pygame.draw.rect(fenetre, (255,255,255), (675, 283, 30, 30))

    texte = fonte.render(str(fr), True, (0,0,0))
    textRect = texte.get_rect()
    textRect.center = (690,300)
    fenetre.blit(texte, textRect)

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


def selectAutomate(fenetre):

    fenetre.fill((255,255,255))

    liste_rectName = [] # liste_rectName => liste du noms des fichiers correspondant aux automates
    liste1_rectPos = [[(90+175*i+50*i), 115] for i in range(3)]
    liste2_rectPos = [[(90+175*i+50*i), 115+175+65] for i in range(3)]

    liste_rectPos = liste1_rectPos + liste2_rectPos #Liste de position des emplacements des automates

    liste_rectObj = []

    for i in range(len(liste_rectPos)):
        liste_rectObj.append(pygame.Rect(liste_rectPos[i][0],liste_rectPos[i][1], 175, 175)) #Conversion de la liste: liste_rect en liste_rectObj

    #Titre de la fenetre
    fonte = pygame.font.SysFont('Comic Sans MS', 36)
    texte = fonte.render('Choisissez votre Automate de Départ', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (400,50)
    fenetre.blit(texte, textRect)

    #Carré noir désignant l'emplacement des automates + carré clicable pour choisir l'automate correspondant
    #for rectangle in liste_rectObj:
        #pygame.draw.rect(fenetre, (0, 0, 0), rectangle,5)


    for i in range(0,6): #Range 6 pour les 6 choix possible
        if i <= 2:
            #Automate pré défini (position 1 à 4)
            a = lecture("automate" + str(i+1))
            liste_rectName.append("automate" + str(i+1))
        elif i <= 4:
            #Automate généré aléaoirement (position 5 et 6)
            crea_map_alea(random.randint(5,15), random.randint(5,15), "map_random" + str(i), random.randint(3,6))
            a = lecture("map_random" + str(i))
            liste_rectName.append("map_random" + str(i))
        else:
            crea_map_alea(random.randint(15, 15), random.randint(9, 9), "custom" + str(i), random.randint(3, 6))
            a = lecture("custom" + str(i))
            liste_rectName.append("custom" + str(i))

        #Calcule pour centré les automates au centre de leurs emplacement
        xm, ym = 175, 175
        hauteur = len(a)
        largeur = len(a[0])
        case = xm // max(hauteur, largeur)
        x0 = (xm - case * largeur) // 2
        y0 = (ym - case * hauteur) // 2

        affiche_graphique(a, (x0 + liste_rectPos[i][0]), (y0 + liste_rectPos[i][1]), case, fenetre)
        fonte = pygame.font.SysFont('Comic Sans MS', 21)
        texte = fonte.render(liste_rectName[i], True, (0, 0, 255))
        textRect = texte.get_rect()
        textRect.center = (87.5 + liste_rectPos[i][0] , 175+15 + liste_rectPos[i][1])
        fenetre.blit(texte, textRect)

    pygame.display.flip()

    # Boucle pour détéctér une interation
    continuer = True
    while continuer:
        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable "continuer" à False
            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()

            # Si l'utilisateur clique sur la fenêtre, on vérifie si le clic a été fait une zone d'emplacement d'un Automate (carré noir)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Récupération de la position du clic
                x, y = event.pos
                for i in range(len(liste_rectObj)):
                    if liste_rectObj[i].collidepoint(x, y): # la fonction collidepoint permet de test is une intération avec la souris a été faite sur un Rectangle de PyGame
                        nbRect = i  # récupération de l'index de l'automate cliqué (0,1,2|3,4,5)
                        nameRect = liste_rectName[nbRect] #Récupéré le nom de fichier de l'automates cliqué
                        if nameRect == "custom5":
                            customAutomate(fenetre)  # Ouverture de l'automate séléctionné
                            continuer = False
                        else:
                            simul_graphique(fenetre, nameRect) #Ouverture de l'automate séléctionné
                            continuer = False

    # Fermeture de Pygame

def startGame():

    pygame.init()

    fenetre = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Jeu de la vie de Conway")
    fenetre.fill((255, 255, 255))

    dataPosA = [] #Données concernant la position et les caractéristique de chaques Automates
    x0 = 0
    y0 = 0

    for i in range(3):
        if i == 0:
            x0 = 50
            y0 = 140
        if i == 1:
            x0 = 500
            y0 = 80
        if i == 2:
            x0 = 180
            y0 = 420

        crea_map_alea(random.randint(10, 20), random.randint(10, 20), "map_random" + str(i+10), random.randint(3, 6))
        a = lecture("map_random" + str(i+10))

        hauteur = len(a)
        largeur = len(a[0])
        case = 250 // max(hauteur, largeur)
        dataPosA.append([a,x0,y0,case])


        affiche_graphique(a, x0, y0, case, fenetre)

    playBtn = elementFixStart(fenetre)

    pygame.display.flip()
    framerate = 7

    continuer = True
    while continuer:
        horaire = pygame.time.Clock()
        horaire.tick(framerate)
        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable "continuer" à False
            if event.type == pygame.QUIT:
                continuer = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if playBtn.collidepoint(x,y):
                    continuer = False
                    selectAutomate(fenetre)
        for i in range(3):
            a = dataPosA[i][0]
            x0 = dataPosA[i][1]
            y0 = dataPosA[i][2]
            case = dataPosA[i][3]
            modifie, automate = calcul_etape(a)

            dataPosA[i][0] = automate
            affiche_graphique(automate, x0, y0, case, fenetre)
        elementFixStart(fenetre)
        pygame.display.flip()

    # Fermeture de Pygame
    pygame.quit()

def elementFixStart(fenetre):

    playBtn = pygame.Rect([325, 360, 150, 80])
    pygame.draw.rect(fenetre, (0, 255, 0), playBtn,0,12)

    fonte = pygame.font.SysFont('Comic Sans MS', 36)
    texte = fonte.render('Play', True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (400, 400)
    fenetre.blit(texte, textRect)

    fonte = pygame.font.SysFont('Comic Sans MS', 46)
    texte = fonte.render('Jeu de la vie de Conway', True, (0, 0, 255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (400, 70)
    fenetre.blit(texte, textRect)

    return playBtn


def customAutomate(fenetre):

    fenetre.fill((255, 255, 255))

    #Rectangles Boutons
    btnValider, btnTerminer = elementCustomFixe(fenetre)
    btnXUp = upButton(fenetre, 725, 110, True)
    btnXDown = upButton(fenetre, 725,159, False)
    btnYUp = upButton(fenetre, 725, 210, True)
    btnYDown = upButton(fenetre, 725, 259, False)

    largeur, hauteur = 7,7
    a = [[0 for y in range(largeur)] for i in range(hauteur)]

    x0, y0, case = calDataAutomate(largeur, hauteur) #Calcul position et taille de l'autmate

    ZoneCustom = pygame.Rect(x0, y0, largeur * case, hauteur * case)

    affiche_graphique(a, x0, y0, case, fenetre)

    elementCustomActus(fenetre, largeur, hauteur)

    pygame.display.flip()

    continuer = True
    while continuer:
        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable "continuer" à False
            if event.type == pygame.QUIT:
                continuer = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ZoneCustom.collidepoint(x, y):
                    nbX = (x - x0) // case
                    nbY = (y - y0) // case
                    if a[nbY][nbX] == 0:
                        a[nbY][nbX] = 1
                    else:
                        a[nbY][nbX] = 0

                    affiche_graphique(a, x0, y0, case, fenetre)
                    pygame.display.flip()
                elif btnValider.collidepoint(x,y):
                    a = [[0 for y in range(largeur)] for i in range(hauteur)]
                    x0, y0, case = calDataAutomate(largeur, hauteur)
                    ZoneCustom = pygame.Rect(x0, y0, largeur * case, hauteur * case)

                    pygame.draw.rect(fenetre, (255,255,255), (45,45,510,510)) #Carré blanc Recouvrir l'automate précédant

                    affiche_graphique(a, x0, y0, case, fenetre)

                elif btnTerminer.collidepoint(x,y):
                    continuer = False
                    ecriture("custom5", 0, a)
                    simul_graphique(fenetre, "custom5_0000")
                elif btnXUp.collidepoint(x,y):
                    if largeur < 50:
                        largeur = largeur + 1
                elif btnXDown.collidepoint(x,y):
                    if largeur > 2:
                        largeur = largeur - 1
                elif btnYUp.collidepoint(x,y):
                    if hauteur < 50:
                        hauteur = hauteur + 1
                elif btnYDown.collidepoint(x,y):
                    if hauteur > 2:
                        hauteur = hauteur - 1
                elementCustomActus(fenetre, largeur, hauteur)
                pygame.display.flip()

    pygame.quit()
    sys.exit()

def calDataAutomate(largeur, hauteur): #Calcule de données relative a un Automate
    xm, ym = 500, 500

    case = xm // max(hauteur, largeur)
    x0 = 50 + (xm - case * largeur) // 2
    y0 = 50 + (ym - case * hauteur) // 2

    return x0, y0, case

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

def elementCustomFixe(fenetre):

    fonte = pygame.font.SysFont('Comic Sans MS', 27)
    texte = fonte.render("Choisis la taille", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675, 40)
    fenetre.blit(texte, textRect)

    texte = fonte.render("de l'automate ", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675, 70)
    fenetre.blit(texte, textRect)

    texte = fonte.render("Crée un motif ", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675, 400)
    fenetre.blit(texte, textRect)

    texte = fonte.render("de cellules ", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675, 430)
    fenetre.blit(texte, textRect)

    fonte = pygame.font.SysFont('Comic Sans MS', 21)
    texte = fonte.render('Largeur', True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (625, 150)
    fenetre.blit(texte, textRect)

    fonte = pygame.font.SysFont('Comic Sans MS', 21)
    texte = fonte.render('Hauteur', True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (625, 250)
    fenetre.blit(texte, textRect)

    btnValider = pygame.Rect(0,0,110,45)
    btnValider.center = (675,330)
    pygame.draw.rect(fenetre, (0,250,0), btnValider, 0, 5)

    fonte = pygame.font.SysFont('Comic Sans MS', 21)
    texte = fonte.render("Valider", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675,330)
    fenetre.blit(texte, textRect)

    btnTerminer = pygame.Rect(0, 0, 110, 45)
    btnTerminer.center = (675, 500)
    pygame.draw.rect(fenetre, (0, 250, 0), btnTerminer, 0, 5)

    fonte = pygame.font.SysFont('Comic Sans MS', 21)
    texte = fonte.render("Terminer", True, (0, 0, 255))
    textRect = texte.get_rect()
    textRect.center = (675, 500)
    fenetre.blit(texte, textRect)


    return btnValider, btnTerminer

def elementCustomActus(fenetre, xValue, yValue):

    fonte = pygame.font.SysFont('Comic Sans MS', 25)

    # Carré blanc Recouvre le nombre précédant
    pygame.draw.rect(fenetre, (255,255,255), (675, 135, 30, 30))
    pygame.draw.rect(fenetre, (255,255,255), (675, 235, 30, 30))

    texte = fonte.render(str(xValue), True, (0, 0, 0))
    textRect = texte.get_rect()
    textRect.center = (690, 150)
    fenetre.blit(texte, textRect)

    texte = fonte.render(str(yValue), True, (0, 0, 0))
    textRect = texte.get_rect()
    textRect.center = (690, 250)
    fenetre.blit(texte, textRect)

startGame()

# print("===================")
# print(calcul_etape(lecture('automate1')))
# affiche(lecture('automate1'))
# print("===================")
# affiche(calcul_etape(lecture('automate1')))



