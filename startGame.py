from moduleSystem import *

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