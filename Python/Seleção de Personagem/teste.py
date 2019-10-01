import pygame

pygame.init()
screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption('clicked on image')
setaD = pygame.image.load("../../Sprites/Menu/setaDirBorda.png").convert()
setaE = pygame.image.load("../../Sprites/Menu/setaEsqBorda.png").convert()
heroi = pygame.image.load("../../Sprites/Personagens/Herói/Imagens Normais/Heroi1.png").convert()
cavaleiro = pygame.image.load("../../Sprites/Personagens/Cavaleiro/Imagens Normais/Cavaleiro1.png").convert()

xEsq = 0 
yEsq = 100
posE = (xEsq,yEsq)
widthE = setaE.get_width()
heightE = setaE.get_height()

xDir = 600 
yDir = 100 
posD = (xDir,yDir)
widthD = setaD.get_width()
heightD = setaD.get_height()


xPersona = 300
yPersona = 100
posPersona = (xPersona,yPersona)
widthPersona = heroi.get_width()
heightPersona = heroi.get_height()

troca = True
screen.fill((255,0,0))

screen.blit(setaD ,  (xDir,yDir))
screen.blit(setaE ,  (xEsq,yEsq))
screen.blit(heroi ,  (xPersona,yPersona))



running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            xMouse, yMouse = event.pos
            if setaD.get_rect().collidepoint(xMouse, yMouse):
                if troca == True:
                    screen.fill((255,0,0))
                    screen.blit(cavaleiro,posPersona)
                    screen.blit(setaD ,  posD)
                    screen.blit(setaE ,  posE)
                    print('Clicou na Direita')
                    troca = False
            elif setaE.get_rect().collidepoint(xMouse, yMouse):   
                if troca == False:
                    screen.fill((255,0,0))
                    screen.blit(heroi,	 posPersona)
                    screen.blit(setaD ,  posD)
                    screen.blit(setaE ,  posE)
                    print('Clicou na Esquerda')
                    troca = True
    pygame.display.update()
pygame.quit()
