import pygame

pygame.init()
screen = pygame.display.set_mode( (800, 600) )

setaD = pygame.image.load("../../Sprites/Menu/setaDirBorda.png").convert_alpha()
setaE = pygame.image.load("../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

heroiSpritesMenu = []
for countMenu in range (1,2):
        heroiSpritesMenu.append(pygame.image.load("../../Sprites/Personagens/Herói/Imagens Normais/Heroi" + str(countMenu) + ".png").convert_alpha())

cavaleiroSpritesMenu = []
for countMenu in range (1,2):
        cavaleiroSpritesMenu.append(pygame.image.load("../../Sprites/Personagens/Cavaleiro/Imagens Normais/Cavaleiro" + str(countMenu) + ".png").convert_alpha())

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


troca = 1
screen.fill((255,0,0))

clock = pygame.time.Clock()

sprite_index = 0

screen.blit(setaD ,  (xDir,yDir))
screen.blit(setaE ,  (xEsq,yEsq))
screen.blit(heroiSpritesMenu[sprite_index],	 posPersona)
                                    


running = True
while (running):
        clock.tick(600)
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                        
        if event.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = event.pos
                        
                        if setaD.get_rect().collidepoint(xMouse, yMouse):
                                if troca == 1:
                                    screen.fill((255,0,0))
                                    screen.blit(cavaleiroSpritesMenu[sprite_index],posPersona)
                                    screen.blit(setaD ,  posD)
                                    screen.blit(setaE ,  posE)
                                    print('Clicou na Direita')
                                    troca = 2
                                        
                        elif setaE.get_rect().collidepoint(xMouse, yMouse):   
                                if troca == 2:
                                    screen.fill((255,0,0))
                                    screen.blit(heroiSpritesMenu[sprite_index],	 posPersona)
                                    screen.blit(setaD ,  posD)
                                    screen.blit(setaE ,  posE)
                                    print('Clicou na Esquerda')
                                    troca = 1
                                        
        pygame.display.update()
        sprite_index = (sprite_index + 1)  % 8
pygame.quit()
