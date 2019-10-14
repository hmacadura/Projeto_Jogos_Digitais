import pygame
from pygame import draw
from pygame.locals import *
from random import randint
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((1280,720))
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        exit()


direcao = True
x = 0
y = 648
rodando = True
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    coord =[x,y]
    if x==0 and y==0:
        rodando = False
    pygame.draw.rect(screen,cor,Rect(coord,dimensao))
    if direcao:
        if x == 900:
            direcao = False
            y = y-72
        pygame.draw.rect(screen,cor,Rect(coord,dimensao))
        x = x+90
    else:
       
        if x == 0:
            direcao = True
            y = y-72    
        pygame.draw.rect(screen,cor,Rect(coord,dimensao))
        x = x-90
    pygame.display.update()
    print (x)
    print (y)

