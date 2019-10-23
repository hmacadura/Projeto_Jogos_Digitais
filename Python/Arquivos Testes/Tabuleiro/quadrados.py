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



def clicouTabuleiro (PosMouse, Superficie, PosSuperficie):
        #Rect(x, y, width, height)
        widthSuperficie = 90
        heightSuperficie = 72
        print (PosMouse)
        print (PosSuperficie)
        return PosMouse[0] >= PosSuperficie[0] and PosMouse[0] <= (PosSuperficie[0] + widthSuperficie) and PosMouse[1] >= PosSuperficie[1] and PosMouse[1] <= (PosSuperficie[1] +  heightSuperficie)



direcao = True
coordXTabuleiroEsquerda = 0
coordXTabuleiroDireita= 72
coordYTabuleiroCima = 648
coordYTabuleiroBaixo = 720
rodando = True
contador = 0
numSorteado = 100
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
    if contador == numSorteado:
        rodando = False
    if direcao:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 810 :
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                coordXTabuleiroDireita = coordXTabuleiroDireita+90
                pygame.time.wait(100)
                contador +=1
                if contador == numSorteado:
                    coordXTabuleiroEsquerda = coordXTabuleiroEsquerda-90
                    coordXTabuleiroDireita = coordXTabuleiroDireita-90
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
                if contador == numSorteado:
                    coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                    coordXTabuleiroDireita = coordXTabuleiroDireita+90
                pygame.time.wait(100)
            else:
                direcao = True
                coordYTabuleiroCima = coordYTabuleiroCima-72
                coordYTabuleiroBaixo = coordYTabuleiroBaixo-72
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
    pygame.display.update()

localiza = True
if contador %10 == 0:
    retangulo = (coordXTabuleiroEsquerda,coordYTabuleiroCima+50,90,72)
    posicao =  (coordXTabuleiroEsquerda,coordYTabuleiroCima+50)
else:
    retangulo = (coordXTabuleiroEsquerda,coordYTabuleiroCima,90,72)
    posicao =  (coordXTabuleiroEsquerda,coordYTabuleiroCima)
while localiza:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            posMouse = event.pos
            if contador == numSorteado:
                if clicouTabuleiro(posMouse,retangulo,posicao ):
                    print("Acertou:")
                    localiza = False
                else:
                    print ("errou")




