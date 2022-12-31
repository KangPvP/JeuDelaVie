from moduleSystem import *
from startGame import simul_graphique

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