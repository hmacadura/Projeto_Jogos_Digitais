import pygame
import random
from random import randint


pygame.init()
#screen = pygame.display.set_mode( (0,0),pygame.FULLSCREEN )
screen = pygame.display.set_mode( (800,600))
background_color = (255, 255, 255)

fundoDado = pygame.image.load("../../Sprites/Fundo/marmore.png").convert()


botaoDado = pygame.image.load("../../Sprites/Menu/botaoDado.png").convert_alpha()

pygame.mixer.init()
dadoSom = pygame.mixer.Sound("../../Sounds/Efeitos/somDado.wav")

dadoSprites = []
for countMenu in range (1,7):
        dadoSprites.append(pygame.image.load("../../Sprites/Dado/Modelo Preto/Dado" + str(countMenu) + ".png").convert_alpha())


xbotaoDado = 0 
ybotaoDado = 100
posBotaoDado = (xbotaoDado,ybotaoDado)
widthBotaoDado = botaoDado.get_width()
heightBotaoDado = botaoDado.get_height()


xDado = 300
yDado = 100
posDado = (xDado,yDado)


numeroDado = random.randint(1, 6)
screen.fill(background_color)

clock = pygame.time.Clock()

sprite_index = 0


screen.blit(botaoDado ,posBotaoDado)
print(numeroDado)


running = True
while (running):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = event.pos
                        
                        
                                                
                        if xMouse >= 0 and xMouse <= widthBotaoDado and yMouse >=100 and yMouse <= 100 + heightBotaoDado:
                                print('Clicou no Botão do dado')
                                dadoSom.play()
                                pygame.time.wait(2200)
                                

                                if numeroDado == 1:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))

                                elif numeroDado == 2:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))
        
                                elif numeroDado == 3:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))
                                        
                                elif numeroDado == 4:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))

                                elif numeroDado == 5:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))

                                elif numeroDado == 6:
                                        numeroDado = random.randint(1, 6)
                                        print("Novo valor sorteado:" + str(numeroDado))

                                
        
        screen.fill(background_color)
        if numeroDado == 1:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[0], posDado)
                
        elif numeroDado == 2:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[1],posDado)
        
        elif numeroDado == 3:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[2],posDado)
                
        elif numeroDado == 4:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[3],posDado)

        elif numeroDado == 5:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[4],posDado)
                
        elif numeroDado == 6:
                screen.blit(fundoDado ,(0,0))
                screen.blit(dadoSprites[5],posDado)
        

        screen.blit(botaoDado ,posBotaoDado)

        sprite_index = (sprite_index + 1) % 2
                                
                                        
        pygame.display.update()
        
pygame.quit()
