from moduleSystem import *
from selectMenu import selectAutomate

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

startGame()