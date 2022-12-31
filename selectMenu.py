from moduleSystem import *
from customMenu import customAutomate
from startGame import simul_graphique

def selectAutomate(fenetre):

    fenetre.fill((255,255,255))

    liste1_rectPos = [[(90+175*i+50*i), 115] for i in range(3)]
    liste2_rectPos = [[(90+175*i+50*i), 115+175+65] for i in range(3)]
    liste_rectPos = liste1_rectPos + liste2_rectPos #Liste de position des emplacements des automates

    liste_rectName = elementSelectFixe(fenetre, liste_rectPos)

    liste_rectObj = []

    for i in range(len(liste_rectPos)):
        liste_rectObj.append(pygame.Rect(liste_rectPos[i][0],liste_rectPos[i][1], 175, 175)) #Conversion de la liste: liste_rect en liste_rectObj

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

def elementSelectFixe(fenetre, liste_rectPos):

    #Titre de la fenetre
    fonte = pygame.font.SysFont('Comic Sans MS', 36)
    texte = fonte.render('Choisissez votre Automate de Départ', True, (0,0,255), (255,255,255))
    textRect = texte.get_rect()
    textRect.center = (400,50)
    fenetre.blit(texte, textRect)

    # Carré noir désignant l'emplacement des automates + carré clicable pour choisir l'automate correspondant
    # for rectangle in liste_rectObj:
        # pygame.draw.rect(fenetre, (0, 0, 0), rectangle,5)

    liste_rectName = [] # liste_rectName => liste du noms des fichiers correspondant aux automates

    for i in range(0, 6):  # Range 6 pour les 6 choix possible
        if i <= 2:
            # Automate pré défini (position 1 à 4)
            a = lecture("automate" + str(i + 1))
            liste_rectName.append("automate" + str(i + 1))
        elif i <= 4:
            # Automate généré aléaoirement (position 5 et 6)
            crea_map_alea(random.randint(5, 15), random.randint(5, 15), "map_random" + str(i), random.randint(3, 6))
            a = lecture("map_random" + str(i))
            liste_rectName.append("map_random" + str(i))
        else:
            crea_map_alea(random.randint(15, 15), random.randint(9, 9), "custom" + str(i), random.randint(3, 6))
            a = lecture("custom" + str(i))
            liste_rectName.append("custom" + str(i))

        # Calcule pour centré les automates au centre de leurs emplacement
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
        textRect.center = (87.5 + liste_rectPos[i][0], 175 + 15 + liste_rectPos[i][1])
        fenetre.blit(texte, textRect)

        pygame.display.flip()

    return liste_rectName