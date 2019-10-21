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
coordXTabuleiroEsquerda = 0
coordXTabuleiroDireita= 72
coordYTabuleiroCima = 648
coordYTabuleiroBaixo = 720
rodando = True
contador = 0
numSorteado = 20
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
    if coordXTabuleiroEsquerda==0 and coordYTabuleiroCima==0:
        rodando = False
    if direcao:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 810 :
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                coordXTabuleiroDireita = coordXTabuleiroDireita+90
                pygame.time.wait(100)
                contador +=1
            else:
                direcao = False
                coordYTabuleiroCima = coordYTabuleiroCima-72
                coordYTabuleiroBaixo = coordYTabuleiroBaixo-72
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                contador +=1
                pygame.time.wait(100)
    else:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 0:
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda-90
                coordXTabuleiroDireita = coordXTabuleiroDireita-90
                contador +=1
                pygame.time.wait(100)
            else:
                direcao = True
                coordYTabuleiroCima = coordYTabuleiroCima-72
                coordYTabuleiroBaixo = coordYTabuleiroBaixo-72
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
            if contador == numSorteado:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = event.pos
                        if xMouse >= coordXTabuleiroEsquerda and xMouse <= coordXTabuleiroDireita and yMouse >= coordYTabuleiroBaixo and yMouse <= coordYTabuleiroCima:
                            print("Acertou:")
                        else:
                            print ("errou")
    pygame.display.update()

