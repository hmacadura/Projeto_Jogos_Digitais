import pygame

pygame.init()
#screen = pygame.display.set_mode( (0,0),pygame.FULLSCREEN )
screen = pygame.display.set_mode( (800,600))
background_color = (56, 32, 14)

setaD = pygame.image.load("../../Sprites/Menu/setaDirBorda.png").convert_alpha()
setaE = pygame.image.load("../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

heroiSpritesMenu = []
for countMenu in range (1,3):
        heroiSpritesMenu.append(pygame.image.load("../../Sprites/Personagens/Herói/Imagens Normais/Heroi" + str(countMenu) + ".png").convert_alpha())

cavaleiroSpritesMenu = []
for countMenu in range (1,3):
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
screen.fill(background_color)

clock = pygame.time.Clock()

sprite_index = 0

screen.blit(setaD ,  (xDir,yDir))
screen.blit(setaE ,  (xEsq,yEsq))
screen.blit(heroiSpritesMenu[sprite_index],	 posPersona)

print(len(heroiSpritesMenu))


running = True
while (running):
        clock.tick(3)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = event.pos
                        
                        
                                                
                        if xMouse >= 0 and xMouse <= widthE and yMouse >=100 and yMouse <= 100 + heightE:
                                print('Clicou na Esquerda')
                                
                                if troca == 2:
                                        print("troca==2")
                                        troca = 1

                                elif troca == 1:
                                        print("troca==1")
                                        troca = 2

                        
                        elif xMouse>=600 and xMouse<=800 and yMouse>=100 and yMouse<=100+heightD:
                                print('Clicou na Direita')
                                
                                if troca == 2:
                                        print("troca==2")
                                        troca = 1

                                elif troca == 1:
                                        print("troca==1")
                                        troca = 2
        
        screen.fill(background_color)
        if troca==2:
                screen.blit(cavaleiroSpritesMenu[sprite_index],posPersona)
        else:
                screen.blit(heroiSpritesMenu[sprite_index], posPersona) 
        screen.blit(setaD ,  posD)
        screen.blit(setaE ,  posE)

        sprite_index = (sprite_index + 1) % 2
                                
                                        
        pygame.display.update()
        
pygame.quit()
