import pygame
from pygame import draw
from pygame.locals import *
from random import randint
from sys import exit 
####
pygame.init()


fundoTelaTabuleiro = pygame.image.load("../../../Sprites/Fundo/tabuleiroComSimbolos.png")
dado = pygame.image.load("../../../Sprites/Dado/Modelo Branco/dado1.png")
botaoRodarDado = pygame.image.load("../../../Sprites/Menu/botaoDado.png")
heroi = pygame.image.load("../../../Sprites/Personagens/Herói/Imagens Normais/Heroi1.png")
cavaleiroNegro = pygame.image.load("../../../Sprites/Personagens/Cavaleiro Negro/Sprites Sem Sombras/CavaleiroNegroSemSombra1.png")

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
direcaoComputador = True
coordXTabuleiroJogador = 0
coordYTabuleiroJogador = 648
coordXTabuleiroComputador = 0
coordYTabuleiroComputador = 648
rodando = True
rodar = False
contadorJogador = 1
contadorComputador = 1
numSorteado = randint(1,7) + 1
numSorteadoComputador = randint(1,7) + 1
contadorJogadorErros = 0
localiza = True
coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
posFundo = [0,0]
dado1 = pygame.transform.scale(dado, (200,200))
heroiTransformado = pygame.transform.scale(heroi, (50,50))
cavaleiroNegroTransformado = pygame.transform.scale(cavaleiroNegro, (50,50))
posDado = [1000,400]
posBotao = [950,600]
while rodando:
    screen.blit(dado1 ,posDado)
    screen.blit(botaoRodarDado ,posBotao)
    cor = (255,0,0)
    dimensao = [90,72]
    screen.blit(fundoTelaTabuleiro ,posFundo)
    if direcao:
        if contadorJogador != numSorteado:
            if coordXTabuleiroJogador != 810 :
                coordXTabuleiroJogador = coordXTabuleiroJogador+90
                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                contadorJogador +=1
                pygame.time.wait(100)
            else:
                direcao = False
                coordYTabuleiroJogador = coordYTabuleiroJogador-72
                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                contadorJogador +=1
                pygame.time.wait(100)
    else:
        if contadorJogador != numSorteado:
            if coordXTabuleiroJogador != 0:
                coordXTabuleiroJogador = coordXTabuleiroJogador-90
                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                contadorJogador +=1
                pygame.time.wait(100)
            else:
                direcao = True
                coordYTabuleiroJogador = coordYTabuleiroJogador-72
                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                contadorJogador +=1
                pygame.time.wait(100)
    retangulo = (coordXTabuleiroJogador,coordYTabuleiroJogador,90,72)
    posicao =  (coordXTabuleiroJogador,coordYTabuleiroJogador)
    screen.blit(heroiTransformado, coordJogador)
    screen.blit(cavaleiroNegroTransformado, coordComputador)
    pygame.display.update()
    localiza = True
    if contadorJogador == numSorteado:
        while localiza:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posMouse = event.pos       
                    if contadorJogador == numSorteado:
                        if clicouTabuleiro(posMouse,retangulo,posicao ):
                            contadorJogadorErros = 0
                            sorteio = randint(1,7)
                            numSorteado = numSorteado + sorteio
                            print (contadorJogador)
                            localiza = False
                            rodar = True
                            if contadorJogador== 4:
                                coordXTabuleiroJogador = 630
                                coordYTabuleiroJogador = 504
                                contadorJogador = 28
                                numSorteado = 28
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                            elif contadorJogador== 37:
                                coordXTabuleiroJogador = 450
                                coordYTabuleiroJogador = 216
                                contadorJogador = 66
                                numSorteado = 66
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                direcao = True
                            elif contadorJogador== 42:
                                coordXTabuleiroJogador = 630
                                coordYTabuleiroJogador = 72
                                contadorJogador = 88
                                numSorteado = 88
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                direcao = True
                            elif contadorJogador== 53:
                                coordXTabuleiroJogador = 360
                                coordYTabuleiroJogador = 576
                                contadorJogador = 16
                                numSorteado = 16
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                direcao = False
                                pygame.display.update()
                            elif contadorJogador== 63:
                                coordXTabuleiroJogador = 450
                                coordYTabuleiroJogador = 432
                                contadorJogador = 43
                                numSorteado = 43
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                direcao = False
                                pygame.display.update()
                            elif contadorJogador== 85:
                                coordXTabuleiroJogador = 180
                                coordYTabuleiroJogador = 360
                                contadorJogador = 43
                                numSorteado = 43
                                coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                direcao = True
                                pygame.display.update()
                        else:
                            print ("errou")
                            contadorJogadorErros = contadorJogadorErros + 1
                            if contadorJogadorErros >=5:
                                cor = (0,255,0)
                                pygame.draw.rect(screen,cor,Rect(coordJogador,dimensao))
                                pygame.display.update()

                                
    while rodar:
        if direcaoComputador:
            if contadorComputador != numSorteadoComputador:
                if coordXTabuleiroComputador != 810 :
                    coordXTabuleiroComputador = coordXTabuleiroComputador+90
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    contadorComputador +=1
                else:
                    direcaoComputador = False
                    coordYTabuleiroComputador = coordYTabuleiroComputador-72
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    contadorComputador +=1
            else:
                rodar = False
                sorteio = randint(1,7)
                numSorteadoComputador = numSorteadoComputador + sorteio
        else:
            if contadorComputador != numSorteadoComputador:
                if coordXTabuleiroComputador != 0:
                    coordXTabuleiroComputador = coordXTabuleiroComputador-90
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    contadorComputador +=1
                else:
                    direcaoComputador = True
                    coordYTabuleiroComputador = coordYTabuleiroComputador-72
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    contadorComputador +=1
            else:
                rodar = False        
                sorteio = randint(1,7)
                numSorteadoComputador = numSorteadoComputador + sorteio
        if contadorJogador == 100:
            print("ganhou")
            rodando = False
        pygame.display.update()
        if contadorComputador == 100:
            print("perdeu")
            rodando = False
        pygame.display.update()

    




