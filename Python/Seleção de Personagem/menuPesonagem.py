import pygame

pygame.init()

screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption('clicked on image')
setaD = pygame.image.load("../../Sprites/Menu/setaDirBorda.png").convert()
setaE = pygame.image.load("../../Sprites/Menu/setaEsqBorda.png").convert()
x = 20; 
y = 30; 
troca = True
screen.fill((0,0,0))
screen.blit(setaD ,  ( x,y))

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
		
            xMouse, yMouse = event.pos
            if setaD.get_rect().collidepoint(xMouse, yMouse):
                if troca == True:
                    screen.fill((0,0,0))
                    screen.blit(setaD ,  ( 20,30))
                    print('Clicou na Direita')
                    troca = False
                elif troca == False:
                    screen.fill((0,0,0))
                    screen.blit(setaE ,  ( x,y))
                    print('Clicou na Esquerda')
                    troca = True
    pygame.display.update()
pygame.quit()


