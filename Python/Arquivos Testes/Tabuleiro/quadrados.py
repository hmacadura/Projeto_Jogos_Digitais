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
        return PosMouse[0] >= PosSuperficie[0] and PosMouse[0] <= (PosSuperficie[0] + widthSuperficie) and PosMouse[1] >= PosSuperficie[1] and PosMouse[1] <= (PosSuperficie[1] +  heightSuperficie)



direcao = True
coordXTabuleiroEsquerda = 0
coordYTabuleiroCima = 648
rodando = True
contador = 0
numSorteado = randint(1,7)
contadorErros = 0
localiza = True
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
    if direcao:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 810 :
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
                if contador == numSorteado:
                    coordXTabuleiroEsquerda = coordXTabuleiroEsquerda-90
            else:
                direcao = False
                coordYTabuleiroCima = coordYTabuleiroCima-72
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                contador +=1
                pygame.time.wait(100)
    else:
        print ("Entrou else")
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 0:
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda-90
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                contador +=1
                if contador == numSorteado:
                    coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                pygame.time.wait(100)
            else:
                direcao = True
                coordYTabuleiroCima = coordYTabuleiroCima-72
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
    if contador %10 == 0:
        retangulo = (coordXTabuleiroEsquerda,coordYTabuleiroCima+50,90,72)
        posicao =  (coordXTabuleiroEsquerda,coordYTabuleiroCima+50)
    else:
        retangulo = (coordXTabuleiroEsquerda,coordYTabuleiroCima,90,72)
        posicao =  (coordXTabuleiroEsquerda,coordYTabuleiroCima)
    pygame.display.update()
    localiza = True
    if contador == numSorteado:
        while localiza:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posMouse = event.pos       
                    if contador == numSorteado:
                        print (contadorErros)
                        print (posMouse)
                        print (posicao)
                        if clicouTabuleiro(posMouse,retangulo,posicao ):
                            print("Acertou:")
                            contadorErros = 0
                            localiza = False
                            sorteio = randint(1,7)
                            print (sorteio)
                            numSorteado = numSorteado + sorteio
                        else:
                            print ("errou")
                            contadorErros = contadorErros + 1
                            if contadorErros >=5:
                                cor = (0,255,0)
                                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                                pygame.display.update()
    if contador == 100:
        print("ganhou")
        rodando = False
    pygame.display.update()

    




