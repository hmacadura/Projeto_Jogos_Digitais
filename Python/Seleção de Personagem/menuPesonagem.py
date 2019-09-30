import pygame

pygame.init()
width = 350
height = 400
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('clicked on image')
setaD = pygame.image.load("../../Sprites/Menu/setaDir.png").convert()
setaE = pygame.image.load("../../Sprites/Menu/setaEsq.png").convert()
x = 20; 
y = 30; 
troca = True
screen.fill((255,255,255))
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
                    screen.fill((255,255,255))
                    screen.blit(setaE ,  ( x,y))
                    print('Clicou na Esquerda')
                    troca = True
    pygame.display.update()
pygame.quit()


