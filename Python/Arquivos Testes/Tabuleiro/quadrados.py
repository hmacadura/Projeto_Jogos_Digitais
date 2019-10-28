import pygame
from pygame import draw
from pygame.locals import *
from random import randint
from sys import exit 
####
pygame.init()


fundoTelaTabuleiro = pygame.image.load("../../../Sprites/Fundo/tabuleiroComSimbolos.png")



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
contador = 1
numSorteado = 85
contadorErros = 0
localiza = True
coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
posFundo = [0,0]
while rodando:
    cor = (255,0,0)
    dimensao = [90,72]
    pygame.draw.rect(screen,cor,Rect(coord,dimensao))
    screen.blit(fundoTelaTabuleiro ,posFundo)
    if direcao:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 810 :
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda+90
                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
            else:
                direcao = False
                coordYTabuleiroCima = coordYTabuleiroCima-72
                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                contador +=1
                pygame.time.wait(100)
    else:
        if contador != numSorteado:
            if coordXTabuleiroEsquerda != 0:
                coordXTabuleiroEsquerda = coordXTabuleiroEsquerda-90
                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                contador +=1
                pygame.time.wait(100)
            else:
                direcao = True
                coordYTabuleiroCima = coordYTabuleiroCima-72
                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                pygame.draw.rect(screen,cor,Rect(coord,dimensao))
                pygame.time.wait(100)
                contador +=1
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
                        print (retangulo)
                        print (posMouse)
                        print (posicao)
                        if clicouTabuleiro(posMouse,retangulo,posicao ):
                            print("Acertou:")
                            contadorErros = 0
                            localiza = False
                            sorteio = randint(1,7)
                            numSorteado = numSorteado + sorteio
                            print (contador)
                            if contador== 4:
                                coordXTabuleiroEsquerda = 630
                                coordYTabuleiroCima = 504
                                contador = 28
                                numSorteado = 28
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                            elif contador== 37:
                                coordXTabuleiroEsquerda = 450
                                coordYTabuleiroCima = 216
                                contador = 66
                                numSorteado = 66
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                                direcao = True
                            elif contador== 42:
                                coordXTabuleiroEsquerda = 630
                                coordYTabuleiroCima = 72
                                contador = 88
                                numSorteado = 88
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                                direcao = True
                            elif contador== 53:
                                coordXTabuleiroEsquerda = 360
                                coordYTabuleiroCima = 576
                                contador = 16
                                numSorteado = 16
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                                direcao = False
                                pygame.display.update()
                            elif contador== 63:
                                coordXTabuleiroEsquerda = 450
                                coordYTabuleiroCima = 432
                                contador = 43
                                numSorteado = 43
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                                direcao = False
                                pygame.display.update()
                            elif contador== 85:
                                coordXTabuleiroEsquerda = 180
                                coordYTabuleiroCima = 360
                                contador = 43
                                numSorteado = 43
                                coord =[coordXTabuleiroEsquerda,coordYTabuleiroCima]
                                direcao = True
                                pygame.display.update()
                            
                            
                            
                                
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

    




