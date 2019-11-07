import pygame
from pygame import draw
from pygame.locals import *
from random import randint
from sys import exit 
####

def tabuleiro():
        pygame.init()
        screen = pygame.display.set_mode((1280,720))
        fundoTelaTabuleiro = pygame.image.load("../../../Sprites/Fundo/tabuleiroComSimbolos.png")
        botaoRodarDado = pygame.image.load("../../../Sprites/Menu/botaoDado.png")
        fundoCaverna = pygame.image.load("../../../Sprites/Fundo/fundoCaverna.png")

        dadoSpritesMenu = []
        for countMenu in range (1,7):
                dadoSpritesMenu.append(pygame.image.load("../../../Sprites/Dado/Modelo Branco/dado" + str(countMenu) + ".png").convert_alpha())
        heroiSpritesMenu = []
        for countMenu in range (1,8):
                heroiSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Herói/Imagens Normais/Heroi" + str(countMenu) + ".png").convert_alpha())
        cavaleiroNegroSpritesMenu = []
        for countMenu in range (1,12):
                cavaleiroNegroSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Cavaleiro Negro/Sprites Sem Sombras/CavaleiroNegroSemSombra" + str(countMenu) + ".png").convert_alpha())
        magiaSpritesMenu = []
        for countMenu in range (1,9):
                magiaSpritesMenu.append(pygame.image.load("../../../Sprites/Magia/Magia Azul/Imagens Normais/magia_azul" + str(countMenu) + ".png").convert_alpha())






        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()



        def clicouTabuleiro (PosMouse, Superficie, PosSuperficie):
                #Rect(x, y, width, height)
                widthSuperficie = 90
                heightSuperficie = 72
                return PosMouse[0] >= PosSuperficie[0] and PosMouse[0] <= (PosSuperficie[0] + widthSuperficie) and PosMouse[1] >= PosSuperficie[1] and PosMouse[1] <= (PosSuperficie[1] +  heightSuperficie)


        font = pygame.font.Font('C:\Windows\Fonts\cour.ttf', 25) 
        direcao = True
        direcaoAtual = True
        direcaoComputador = True
        coordXTabuleiroJogador = 0
        coordYTabuleiroJogador = 648
        coordXTabuleiroJogadorAtual = 0
        coordYTabuleiroJogadorAtual = 648
        coordXTabuleiroComputador = 0
        coordYTabuleiroComputador = 648
        rodando = True
        rodar = False
        contadorJogador = 1
        contadorJogadorAtual = 1
        contadorComputador = 1
        sorteio = randint(0,5)
        print(sorteio)
        numSorteado = sorteio + 2
        numSorteadoComputador = randint(1,6) + 1
        contadorJogadorErros = 0
        personagemIndice = 0
        computadorIndice = 0
        magiaIndice = 0
        localiza = True
        cavaleiroNegro = cavaleiroNegroSpritesMenu[computadorIndice]
        heroi = heroiSpritesMenu[personagemIndice]
        dado = dadoSpritesMenu[sorteio]
        coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
        coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
        posFundo = [0,0]
        dado1 = pygame.transform.scale(dado, (200,200))
        heroiTransformado = pygame.transform.scale(heroi, (50,50))
        cavaleiroNegroTransformado = pygame.transform.scale(cavaleiroNegro, (50,50))
        posDado = [1000,400]
        posBotao = [950,600]
        xMensagem = 830
        yMensagem = 50
        while rodando:
            cor = (255,255,255)
            dimensao = [90,72]
            computadorIndice +=1
            computadorIndice = computadorIndice %2
            personagemIndice +=1
            personagemIndice = personagemIndice %2
            cavaleiroNegro = cavaleiroNegroSpritesMenu[computadorIndice]
            cavaleiroNegroTransformado = pygame.transform.scale(cavaleiroNegro, (50,50))
            heroi = heroiSpritesMenu[personagemIndice]
            heroiTransformado = pygame.transform.scale(heroi, (50,50))
            screen.blit(fundoCaverna,posFundo)
            screen.blit(dado1,posDado)
            screen.blit(botaoRodarDado ,posBotao)
            screen.blit(fundoTelaTabuleiro ,posFundo)
            screen.blit(fundoTelaTabuleiro ,posFundo)
            screen.blit(heroiTransformado, coordJogadorAtual)
            screen.blit(cavaleiroNegroTransformado, coordComputador)
            if contadorJogadorAtual > contadorComputador:
                mensagem = "Jogador - Casa " + str(contadorJogadorAtual) 
                texto = font.render(mensagem, True, cor)
                screen.blit(texto, [100 + xMensagem , yMensagem])
                mensagem2 = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                texto2 = font.render(mensagem2, True, cor)
                screen.blit(texto2, [100 + xMensagem , yMensagem+50])
            elif contadorJogadorAtual == contadorComputador:
                mensagem = "Jogador - Casa " + str(contadorJogadorAtual) 
                texto = font.render(mensagem, True, cor)
                screen.blit(texto, [100 + xMensagem , yMensagem])
                mensagem2 = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                texto2 = font.render(mensagem2, True, cor)
                screen.blit(texto2, [100 + xMensagem , yMensagem+50])
            else:
                mensagem = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                texto = font.render(mensagem, True, cor)
                screen.blit(texto, [100 + xMensagem , yMensagem])
                mensagem2 = "Jogador - Casa " + str(contadorJogadorAtual) 
                texto2 = font.render(mensagem2, True, cor)
                screen.blit(texto2, [100 + xMensagem , yMensagem+50])
            pygame.display.update()
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
            screen.blit(fundoTelaTabuleiro ,posFundo)
            screen.blit(heroiTransformado, coordJogadorAtual)
            screen.blit(cavaleiroNegroTransformado, coordComputador)
            pygame.display.update()
            print (numSorteado)
            localiza = True
            if contadorJogador == numSorteado:
                pygame.display.update()
                while localiza:
                    computadorIndice +=1
                    computadorIndice = computadorIndice %3
                    personagemIndice +=1
                    personagemIndice = personagemIndice %2
                    cavaleiroNegro = cavaleiroNegroSpritesMenu[computadorIndice]
                    cavaleiroNegroTransformado = pygame.transform.scale(cavaleiroNegro, (50,50))
                    heroi = heroiSpritesMenu[personagemIndice]
                    heroiTransformado = pygame.transform.scale(heroi, (50,50))
                    screen.blit(fundoCaverna,posFundo)
                    screen.blit(dado1,posDado)
                    screen.blit(botaoRodarDado ,posBotao)
                    screen.blit(fundoTelaTabuleiro ,posFundo)
                    screen.blit(fundoTelaTabuleiro ,posFundo)
                    screen.blit(heroiTransformado, coordJogadorAtual)
                    screen.blit(cavaleiroNegroTransformado, coordComputador)
                    if contadorJogadorAtual > contadorComputador:
                        mensagem = "Jogador - Casa " + str(contadorJogadorAtual) 
                        texto = font.render(mensagem, True, cor)
                        screen.blit(texto, [100 + xMensagem , yMensagem])
                        mensagem2 = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                        texto2 = font.render(mensagem2, True, cor)
                        screen.blit(texto2, [100 + xMensagem , yMensagem+50])
                    elif contadorJogadorAtual == contadorComputador:
                        mensagem = "Jogador - Casa " + str(contadorJogadorAtual) 
                        texto = font.render(mensagem, True, cor)
                        screen.blit(texto, [100 + xMensagem , yMensagem])
                        mensagem2 = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                        texto2 = font.render(mensagem2, True, cor)
                        screen.blit(texto2, [100 + xMensagem , yMensagem+50])
                    else:
                        mensagem = "Cavaleiro Negro - Casa "+ str(contadorComputador)
                        texto = font.render(mensagem, True, cor)
                        screen.blit(texto, [100 + xMensagem , yMensagem])
                        mensagem2 = "Jogador - Casa " + str(contadorJogadorAtual) 
                        texto2 = font.render(mensagem2, True, cor)
                        screen.blit(texto2, [100 + xMensagem , yMensagem+50])
                    
                    pygame.time.wait(100)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            posMouse = event.pos       
                            if contadorJogador == numSorteado:
                                if clicouTabuleiro(posMouse,retangulo,posicao ):
                                    contadorJogadorErros = 0
                                    sorteio = randint(1,6)
                                    dado = dadoSpritesMenu[sorteio -1]
                                    dado1 = pygame.transform.scale(dado, (200,200))
                                    screen.blit(dado1,posDado)
                                    print (contadorJogador)
                                    localiza = False
                                    rodar = True
                                    a = 0
                                    print (numSorteado)
                                    while contadorJogadorAtual != contadorJogador:
                                        if direcaoAtual:
                                            if contadorJogadorAtual != numSorteado :
                                                if coordXTabuleiroJogadorAtual != 810 :
                                                    if a <10:
                                                        coordXTabuleiroJogadorAtual = coordXTabuleiroJogadorAtual+9
                                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                                        a +=1
                                                        personagemIndice +=1
                                                        personagemIndice = personagemIndice %2 + 2
                                                    if a == 10:
                                                        contadorJogadorAtual +=1
                                                        a=0
                                                        
                                                else:
                                                    if contadorJogadorAtual != numSorteado :   
                                                        if coordXTabuleiroJogadorAtual == 810:
                                                            print("AAAAAAAAAAAAAAAAAaaaa")
                                                            a=0
                                                            direcaoAtual = False
                                                            while a<8:
                                                                if a<8:
                                                                    coordYTabuleiroJogadorAtual = coordYTabuleiroJogadorAtual-9
                                                                    coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                                                    personagemIndice +=1
                                                                    personagemIndice = personagemIndice %2 + 5
                                                                    a +=1
                                                                    heroi = heroiSpritesMenu[personagemIndice]
                                                                    heroiTransformado = pygame.transform.scale(heroi, (50,50))
                                                                    screen.blit(fundoTelaTabuleiro ,posFundo)
                                                                    screen.blit(heroiTransformado, coordJogadorAtual)
                                                                    screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                                    pygame.display.update()
                                                                    pygame.time.wait(100)
                                                                    if a ==8:
                                                                        contadorJogadorAtual +=1
                                                                        print (coordXTabuleiroJogadorAtual)
                                                                        print (coordYTabuleiroJogadorAtual)
                                                                else:
                                                                    a=10
                                        else:
                                            if contadorJogadorAtual != contadorJogador:
                                                if coordXTabuleiroJogadorAtual != 0:
                                                    if a <10:
                                                        coordXTabuleiroJogadorAtual = coordXTabuleiroJogadorAtual-9
                                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                                        a +=1
                                                        personagemIndice +=1
                                                        personagemIndice = personagemIndice %2 + 4
                                                        if a == 10:
                                                            contadorJogadorAtual +=1
                                                            a=0
                                                if contadorJogadorAtual != contadorJogador:   
                                                    if coordXTabuleiroJogadorAtual == 0:
                                                        print("AAAAAAAAA")
                                                        a=0
                                                        direcaoAtual = True
                                                        while a<8:
                                                                if a<8:
                                                                    coordYTabuleiroJogadorAtual = coordYTabuleiroJogadorAtual-9
                                                                    coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                                                    personagemIndice +=1
                                                                    personagemIndice = personagemIndice %2 + 5
                                                                    a +=1
                                                                    heroi = heroiSpritesMenu[personagemIndice]
                                                                    heroiTransformado = pygame.transform.scale(heroi, (50,50))
                                                                    screen.blit(fundoTelaTabuleiro ,posFundo)
                                                                    screen.blit(heroiTransformado, coordJogadorAtual)
                                                                    screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                                    pygame.display.update()
                                                                    pygame.time.wait(100)
                                                                    if a ==8:
                                                                        contadorJogadorAtual +=1
                                                                        
                                                                else:
                                                                    a=0
                                        print (coordXTabuleiroJogadorAtual)
                                        print (coordYTabuleiroJogadorAtual)
                                        print (coordXTabuleiroJogador)
                                        print (coordYTabuleiroJogador)
                                        if contadorJogadorAtual == contadorJogador:
                                            if  coordYTabuleiroJogadorAtual != coordYTabuleiroJogador or coordXTabuleiroJogadorAtual !=coordXTabuleiroJogador:
                                                coordYTabuleiroJogadorAtual = coordYTabuleiroJogador
                                                coordXTabuleiroJogadorAtual = coordXTabuleiroJogador
                                                coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        heroi = heroiSpritesMenu[personagemIndice]
                                        heroiTransformado = pygame.transform.scale(heroi, (50,50))
                                        screen.blit(fundoTelaTabuleiro ,posFundo)
                                        screen.blit(cavaleiroNegroTransformado, coordComputador) 
                                        screen.blit(heroiTransformado, coordJogadorAtual)
                                        pygame.display.update()
                                        print(contadorJogadorAtual)
                                       # pygame.time.wait(50)
                                    if contadorJogador== 4:
                                        magiaIndice = 0
                                        coordMagia=[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        while magiaIndice <7:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice +=1
                                        coordXTabuleiroJogador = 630
                                        coordYTabuleiroJogador = 504
                                        contadorJogador = 28
                                        numSorteado = 28
                                        coordMagia=[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        while magiaIndice >0:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice -=1
                                        coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                    elif contadorJogador== 37:
                                        magiaIndice = 0
                                        coordMagia=[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        while magiaIndice <7:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice +=1
                                        coordXTabuleiroJogador = 450
                                        coordYTabuleiroJogador = 216
                                        contadorJogador = 66
                                        numSorteado = 66
                                        while magiaIndice >0:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice -=1
                                        coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        direcao = True
                                    elif contadorJogador== 42:
                                        magiaIndice = 0
                                        coordMagia=[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        while magiaIndice <7:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice +=1
                                        coordXTabuleiroJogador = 630
                                        coordYTabuleiroJogador = 72
                                        contadorJogador = 88
                                        numSorteado = 88
                                        coordJogador =[coordXTabuleiroJogador,coordYTabuleiroJogador]
                                        while magiaIndice >0:
                                                magia = magiaSpritesMenu[magiaIndice]
                                                magia1 = pygame.transform.scale(magia, (72,90))
                                                screen.blit(fundoTelaTabuleiro ,posFundo)
                                                screen.blit(magia1, coordMagia)
                                                screen.blit(cavaleiroNegroTransformado, coordComputador)
                                                pygame.display.update()
                                                pygame.time.wait(30)
                                                magiaIndice -=1
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
                                    if contadorJogadorAtual== 4:
                                        coordXTabuleiroJogadorAtual = 630
                                        coordYTabuleiroJogadorAtual = 504
                                        contadorJogadorAtual = 28
                                        numSorteado = 28
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                    elif contadorJogadorAtual== 37:
                                        coordXTabuleiroJogadorAtual = 450
                                        coordYTabuleiroJogadorAtual = 216
                                        contadorJogadorAtual = 66
                                        numSorteado = 66
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        direcaoAtual = True
                                    elif contadorJogadorAtual== 42:
                                        coordXTabuleiroJogadorAtual = 630
                                        coordYTabuleiroJogadorAtual = 72
                                        contadorJogadorAtual = 88
                                        numSorteado = 88
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        direcaoAtual = True
                                    elif contadorJogadorAtual== 53:
                                        coordXTabuleiroJogadorAtual = 360
                                        coordYTabuleiroJogadorAtual = 576
                                        contadorJogadorAtual = 16
                                        numSorteado = 16
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        direcaoAtual = False
                                        pygame.display.update()
                                    elif contadorJogadorAtual== 63:
                                        coordXTabuleiroJogadorAtual = 450
                                        coordYTabuleiroJogadorAtual = 432
                                        contadorJogadorAtual = 43
                                        numSorteado = 43
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        direcao = False
                                        pygame.display.update()
                                    elif contadorJogadorAtual== 85:
                                        coordXTabuleiroJogadorAtual = 180
                                        coordYTabuleiroJogadorAtual = 360
                                        contadorJogadorAtual = 43
                                        numSorteado = 43
                                        coordJogadorAtual =[coordXTabuleiroJogadorAtual,coordYTabuleiroJogadorAtual]
                                        direcaoAtual = True
                                        pygame.display.update()
                                else:
                                    print ("errou")
                                    contadorJogadorErros = contadorJogadorErros + 1
                                    if contadorJogadorErros >=5:
                                        cor = (0,255,0)
                                        pygame.draw.rect(screen,cor,Rect(coordJogador,dimensao))
                                        pygame.display.update()

                numSorteado = numSorteado + sorteio                        
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
                        sorteio = randint(0,6)
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
                if contadorJogadorAtual== 4:
                    coordXTabuleiroComputador = 630
                    coordYTabuleiroComputador = 504
                    contadorComputador = 28
                    numSorteadoComputador = 28
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                elif contadorComputador== 37:
                    coordXTabuleiroComputador = 450
                    coordYTabuleiroComputador = 216
                    contadorComputador = 66
                    numSorteadoComputador = 66
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    direcaoAtual = True
                elif contadorComputador== 42:
                    coordXTabuleiroComputador = 630
                    coordYTabuleiroComputador = 72
                    contadorComputador = 88
                    numSorteadoComputador = 88
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    direcaoAtual = True
                elif contadorComputador== 53:
                    coordXTabuleiroComputador = 360
                    coordYTabuleiroComputador = 576
                    contadorComputador = 16
                    numSorteadoComputador = 16
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    direcaoAtual = False
                    pygame.display.update()
                elif contadorComputador== 63:
                    coordXTabuleiroComputador = 450
                    coordYTabuleiroComputador = 432
                    contadorComputador = 43
                    numSorteadoComputador = 43
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    direcao = False
                    pygame.display.update()
                elif contadorComputador== 85:
                    coordXTabuleiroComputador = 180
                    coordYTabuleiroComputador = 360
                    contadorComputador = 43
                    numSorteadoComputador = 43
                    coordComputador =[coordXTabuleiroComputador,coordYTabuleiroComputador]
                    direcaoAtual = True
                    pygame.display.update()
                screen.blit(fundoTelaTabuleiro ,posFundo)
                screen.blit(heroiTransformado, coordJogadorAtual)
                screen.blit(cavaleiroNegroTransformado, coordComputador)
                pygame.display.update()
                #pygame.time.wait(1000)
                if contadorJogador == 100:
                    print("ganhou")
                    rodando = False
                pygame.display.update()
                if contadorComputador == 100:
                    print("perdeu")
                    rodando = False
                pygame.display.update()

            





