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
coordXTabuleiro = 0
coordYTabuleiro = 648
rodando = True
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    coord =[coordXTabuleiro,coordYTabuleiro]
    if coordXTabuleiro==0 and coordYTabuleiro==0:
        rodando = False
    pygame.draw.rect(screen,cor,Rect(coord,dimensao))
    if direcao:
        if coordXTabuleiro != 900:
            pygame.draw.rect(screen,cor,Rect(coord,dimensao))
            coordXTabuleiro = coordXTabuleiro+90
        else:
            direcao = False
            coordYTabuleiro = coordYTabuleiro-72
    else:
        if coordXTabuleiro != 0:
            pygame.draw.rect(screen,cor,Rect(coord,dimensao))
            coordXTabuleiro = coordXTabuleiro-90

        else:
            direcao = True
            coordYTabuleiro = coordYTabuleiro-72    
        
    pygame.display.update()

