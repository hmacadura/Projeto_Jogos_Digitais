import pygame
import sys
import time
pygame.init()
pygame.mixer.init()

#Tamanho da Tela
widthScreen = 1280
heightScreen = 720

#-------------TELA CHEIA-------------
screen = pygame.display.set_mode( (widthScreen,heightScreen),pygame.FULLSCREEN )

#-------------JANELA NORMAL-------------
#screen = pygame.display.set_mode( (widthScreen,heightScreen))

#-------------Definindo Cores-------------
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkSlateGray = (47, 79, 79)

#Variavel que Percorrerá o Array das Sprites
sprite_index = 0

#-------------Carregando imagens e sons Para Seleção de Personagens-------------

#-------------------------------------------SONS--------------------------------
telaSom = pygame.mixer.Sound("../../../Sounds/temaZelda.wav")

setaSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoTroca.wav")

selectSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoSelect.wav")
#-------------------------------------------Imagens-----------------------------
fundoTelaInicio = pygame.image.load("../../../Sprites/Fundo/telaInicio.png").convert_alpha()

fundoSalao = pygame.image.load("../../../Sprites/Fundo/fundoSalao.png").convert_alpha()

setaD = pygame.image.load("../../../Sprites/Menu/setaDirBorda.png").convert_alpha()

setaE = pygame.image.load("../../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

botaoSelecionar = pygame.image.load("../../../Sprites/Menu/botaoSelect.png").convert_alpha()

botaoIniciar = pygame.image.load("../../../Sprites/Menu/botaoIniciar.png").convert_alpha()

botaoOpcoes = pygame.image.load("../../../Sprites/Menu/botaoOpcoes.png").convert_alpha()

botaoInstrucoes = pygame.image.load("../../../Sprites/Menu/botaoInstrucoes.png").convert_alpha()

botaoVoltar = pygame.image.load("../../../Sprites/Menu/botaoVoltar.png").convert_alpha()

botaoComSom = pygame.image.load("../../../Sprites/Menu/botaoComSom.png").convert_alpha()

botaoSemSom = pygame.image.load("../../../Sprites/Menu/botaoSemSom.png").convert_alpha()

iconeSemSom = pygame.image.load("../../../Sprites/Menu/som0.png").convert_alpha()

iconeComSom = pygame.image.load("../../../Sprites/Menu/som1.png").convert_alpha()

botaoHeroi = pygame.image.load("../../../Sprites/Menu/botaoHeroi.png").convert_alpha()

botaoCavaleiro = pygame.image.load("../../../Sprites/Menu/botaoCavaleiro.png").convert_alpha()

botaoFeiticeira = pygame.image.load("../../../Sprites/Menu/botaoFeiticeira.png").convert_alpha()

botaoMago = pygame.image.load("../../../Sprites/Menu/botaoMago.png").convert_alpha()

botaoPrincesa = pygame.image.load("../../../Sprites/Menu/botaoPrincesa.png").convert_alpha()

fundoPersonagem = pygame.image.load("../../../Sprites/Menu/fundoSelecao.png").convert_alpha()

heroiSpritesMenu = []
for countMenu in range (1,3):
        heroiSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Herói/Imagens Normais/Heroi" + str(countMenu) + ".png").convert_alpha())

cavaleiroSpritesMenu = []
for countMenu in range (1,3):
        cavaleiroSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Cavaleiro/Imagens Normais/Cavaleiro" + str(countMenu) + ".png").convert_alpha())

feiticeiraSpritesMenu = []
for countMenu in range (1,3):
        feiticeiraSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Feiticeira/Imagens Normais/Feiticeira" + str(countMenu) + ".png").convert_alpha())

magoSpritesMenu = []
for countMenu in range (1,3):
        magoSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Mago/Imagens Normais/Mago" + str(countMenu) + ".png").convert_alpha())

princesaSpritesMenu = []
for countMenu in range (1,3):
        princesaSpritesMenu.append(pygame.image.load("../../../Sprites/Personagens/Princesa/Imagens Normais/Princesa" + str(countMenu) + ".png").convert_alpha())

#-------------Carregando imagens Mugshots-------------
heroiSpritesMugshot = []
for countMenu in range (1,3):
        heroiSpritesMugshot.append(pygame.image.load("../../../Sprites/Personagens/Herói/Mugshot/Heroi" + str(countMenu) + ".png").convert_alpha())

cavaleiroSpritesMugshot = []
for countMenu in range (1,3):
        cavaleiroSpritesMugshot.append(pygame.image.load("../../../Sprites/Personagens/Cavaleiro/Mugshot/Cavaleiro" + str(countMenu) + ".png").convert_alpha())

feiticeiraSpritesMugshot = []
for countMenu in range (1,3):
        feiticeiraSpritesMugshot.append(pygame.image.load("../../../Sprites/Personagens/Feiticeira/Mugshot/Feiticeira" + str(countMenu) + ".png").convert_alpha())

magoSpritesMugshot = []
for countMenu in range (1,3):
        magoSpritesMugshot.append(pygame.image.load("../../../Sprites/Personagens/Mago/Mugshot/Mago" + str(countMenu) + ".png").convert_alpha())

princesaSpritesMugshot = []
for countMenu in range (1,3):
        princesaSpritesMugshot.append(pygame.image.load("../../../Sprites/Personagens/Princesa/Mugshot/Princesa" + str(countMenu) + ".png").convert_alpha())


#-------------Funcoes-------------
def clicou (posMouse, Superficie, PosSuperficie):
        #Rect(x, y, width, height)
        widthSuperficie = Superficie.get_rect()[2]
        heightSuperficie = Superficie.get_rect()[3]
        
        return posMouse[0] >= PosSuperficie[0] and posMouse[0] <= (PosSuperficie[0] + widthSuperficie) and posMouse[1] >= PosSuperficie[1] and posMouse[1] <= (PosSuperficie[1] +  heightSuperficie)

#-------------Largura e Altura das Sprites------------- 
#Heroi
widthHeroi = heroiSpritesMenu[sprite_index].get_width()
heightHeroi = heroiSpritesMenu[sprite_index].get_height()

#Cavaleiro
widthCavaleiro = cavaleiroSpritesMenu[sprite_index].get_width()
heightCavaleiro = cavaleiroSpritesMenu[sprite_index].get_height()

#Feiticeira
widthFeiticeira = feiticeiraSpritesMenu[sprite_index].get_width()
heightFeiticeira = feiticeiraSpritesMenu[sprite_index].get_height()

#Mago
widthMago = magoSpritesMenu[sprite_index].get_width()
heightMago = magoSpritesMenu[sprite_index].get_height()

#Princesa
widthPrincesa = princesaSpritesMenu[sprite_index].get_width()
heightPrincesa = princesaSpritesMenu[sprite_index].get_height()

#Seta Esquerda
widthE = setaE.get_width()
heightE = setaE.get_height()

#Seta Direita
widthD = setaD.get_width()
heightD = setaD.get_height()

#Botão Heroi
widthBotaoPersonagem = botaoHeroi.get_width()
heightBotaoPersonagem = botaoHeroi.get_height()

#Botão Selecionar
widthBotaoSelecionar = botaoSelecionar.get_width()
heightBotaoSelecionar = botaoSelecionar.get_height()

#Botão Iniciar
widthBotaoIniciar = botaoIniciar.get_width()
heightBotaoIniciar = botaoIniciar.get_height()

#Botão Opções
widthBotaoOpcoes = botaoOpcoes.get_width()
heightBotaoOpcoes = botaoOpcoes.get_height()

#Botão Instruções
widthBotaoInstrucoes = botaoInstrucoes.get_width()
heightBotaoInstrucoes = botaoInstrucoes.get_height()

#Botão Voltar
widthBotaoVoltar = botaoVoltar.get_width()
heightBotaoVoltar = botaoVoltar.get_height()

#Botão Com Som
widthBotaoComSom = botaoComSom.get_width()
heightBotaoComSom = botaoComSom.get_height()

#Botão Sem Som
widthBotaoSemSom = botaoSemSom.get_width()
heightBotaoSemSom = botaoSemSom.get_height()

#Ícone Som
widthIconeSom = iconeComSom.get_width()
heightIconeSom = iconeComSom.get_height()

#Fundo Personagem 
widthFundoPersonagem = fundoPersonagem.get_width()
heightFundoPersonagem = fundoPersonagem.get_height()

#Personagem Mugshot
widthPersonagemMugshot = heroiSpritesMugshot[sprite_index].get_width()
heightPersonagemMugshot = heroiSpritesMugshot[sprite_index].get_width()
#-------------Definindo Posições-------------

#Fundo
xFundo = 0
yFundo = 0
posFundo = (xFundo,yFundo)

#Seta Esquerda
xEsq = 0
yEsq = heightScreen/2 - heightE/2
posE = (xEsq,yEsq)

#Seta Direita
xDir = widthScreen - widthD
yDir = heightScreen/2 - heightD/2 
posD = (xDir,yDir)

#Ícone Som
xIconeSom = widthScreen/2 - widthIconeSom/2
yIconeSom = heightScreen - heightIconeSom*2
posIconeSom = (xIconeSom,yIconeSom)

#Botão Selecionar
xBotaoSelecionar = widthScreen/2 - widthBotaoSelecionar/2
yBotaoSelecionar = heightScreen/10
posBotaoSelecionar = (xBotaoSelecionar,yBotaoSelecionar)

#Botão Voltar
xBotaoVoltar = widthScreen/2 - widthBotaoVoltar/2
yBotaoVoltar = widthScreen/3
posBotaoVoltar = (xBotaoVoltar,yBotaoVoltar)

#Botão Iniciar
xBotaoIniciar = widthScreen/2 - widthBotaoIniciar/2 
yBotaoIniciar = heightScreen/2*1.2 - heightBotaoIniciar*1.2
posBotaoIniciar = (xBotaoIniciar,yBotaoIniciar)

#Botão Instruções
xBotaoInstrucoes = widthScreen/2 - widthBotaoInstrucoes/2
yBotaoInstrucoes = yBotaoIniciar + heightBotaoInstrucoes*1.2
posBotaoInstrucoes = (xBotaoInstrucoes,yBotaoInstrucoes)

#Botão Opções
xBotaoOpcoes = widthScreen/2 - widthBotaoOpcoes/2
yBotaoOpcoes = yBotaoInstrucoes + heightBotaoOpcoes*1.2
posBotaoOpcoes = (xBotaoOpcoes,yBotaoOpcoes)

#Botão Com Som
xBotaoComSom = widthScreen/2 - widthBotaoComSom/2
yBotaoComSom = widthScreen/10
posBotaoComSom = (xBotaoComSom,yBotaoComSom)

#Botão Sem Som
xBotaoSemSom = widthScreen/2 - widthBotaoSemSom/2
yBotaoSemSom = yBotaoComSom
posBotaoSemSom = (xBotaoSemSom,yBotaoSemSom)

#Fundo Personagem 
xFundoPersonagem = widthScreen/2 - widthFundoPersonagem/2
yFundoPersonagem = heightScreen/2 - heightFundoPersonagem/2 
posFundoPersonagem = (xFundoPersonagem,yFundoPersonagem)

#Herói
xHeroi = widthScreen/2 - widthHeroi/2
yHeroi = heightScreen/2 - widthHeroi/1.5
posHeroi = (xHeroi,yHeroi)

#Cavaleiro  
xCavaleiro = xHeroi
yCavaleiro = yHeroi
posCavaleiro = (xCavaleiro,yCavaleiro)

#Feiticeira  
xFeiticeira = xHeroi
yFeiticeira = yHeroi
posFeiticeira = (xFeiticeira,yFeiticeira)

#Mago  
xMago = xHeroi
yMago = yHeroi
posMago = (xMago,yMago)

#Princesa  
xPrincesa = xHeroi
yPrincesa = yHeroi
posPrincesa = (xPrincesa,yPrincesa)

#Botão Descrição Personagem
xBotaoPersonagem = widthScreen/2 - widthBotaoPersonagem/2
yBotaoPersonagem = heightScreen/2 + heightBotaoPersonagem*1.5
posBotaoPersonagem = (xBotaoPersonagem,yBotaoPersonagem)


#Personagem Geral Mugshot
xPersonagemMugshot = 10
yPersonagemMugshot = 10
posPersonagemMugshot = (xPersonagemMugshot,yPersonagemMugshot)

clock = pygame.time.Clock()

#Variavel que definirá qual personagem o usuário escolheu
troca = 1

#Variavel que definirá se tem som
escolhaSom = 0

#Tamanho do Texto
font = pygame.font.Font('freesansbold.ttf', 32)

#Variavel para parar o programa geral
running = True

#Variavel para parar a tela inicial
verInicio = True

#Variavel para parar a Seleção de Personagens
selecionar = False

#Variavel para parar o Menu
verMenu = True

#Variavel para parar a Tela de Instrução
instrucaoTela = False

#Variavel para parar a Tela de Som
somTela = False

#Variavel para parar o Mugshot
verHistoria = True

#-------------Tela Início-------------
while (verInicio):
        screen.blit(fundoTelaInicio ,posFundo)
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        verInicio = False
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posMouse = event.pos

                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                print("Saindo da Tela Início:")
                                selectSom.play()
                                verInicio = False
                                running = False
        pygame.display.update()

#-------------Tela Menu-------------
while (verMenu):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        verInicio = False
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posMouse = event.pos
                        
                        if clicou(posMouse, botaoIniciar, posBotaoIniciar):
                                print("Entrando no Jogo:")
                                if escolhaSom == 1:
                                        selectSom.play()
                                        pygame.time.wait(300)
                                        
                                selecionar = True
                                verMenu = False
                                running = False

                        elif clicou(posMouse, botaoInstrucoes, posBotaoInstrucoes):
                                print("Entrando na Tela de Instruções:")
                                if escolhaSom == 1:
                                        selectSom.play()
                                        pygame.time.wait(300)
                                        
                                instrucaoTela = True
                                verMenu = False
                                running = False
                        
                                                        
                        elif clicou (posMouse, botaoOpcoes, posBotaoOpcoes):
                                print("Entrando na Tela de Som:")
                                if escolhaSom == 1:
                                        selectSom.play()
                                        pygame.time.wait(300)
                                        
                                somTela = True
                                verMenu = False
                                running = False
                                               
                                
                screen.blit(botaoIniciar    , posBotaoIniciar)
                screen.blit(botaoInstrucoes , posBotaoInstrucoes)        
                screen.blit(botaoOpcoes     , posBotaoOpcoes)                             
        pygame.display.update()
#-------------Tela Som-------------
while (somTela):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        verInicio = False
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posMouse = event.pos
#ARRUMAR OS BOTÕES
                        if clicou(posMouse, botaoVoltar, posBotaoVoltar):
                                print("Voltando pro menu:")
                                selectSom.play()
                                pygame.time.wait(300)
                                verMenu = True
                                running = False
                                somTela = False
                                
                        elif clicou (posMouse, iconeComSom, posIconeSom):
                                print("Menu de Som:")                                        
                                if escolhaSom == 0:
                                        selectSom.play()
                                        pygame.time.wait(300)
                                        print("escolhaSom == 0")
                                        escolhaSom = 1

                                elif escolhaSom == 1:
                                        print("escolhaSom == 1")
                                        escolhaSom = 0        

                if escolhaSom == 1:
                        screen.fill(darkSlateGray)
                        screen.blit(botaoComSom,posBotaoComSom)
                        screen.blit(iconeComSom,posIconeSom)
                        print("Jogo está COM Som")
                elif escolhaSom == 0:
                        screen.fill(darkSlateGray)
                        screen.blit(botaoSemSom,posBotaoSemSom)
                        screen.blit(iconeSemSom,posIconeSom)
                        print("Jogo está SEM Som")
        screen.blit(botaoVoltar,(xBotaoVoltar,500))                             
        pygame.display.update()
        
#-------------Tela Instruções-------------
while (instrucaoTela):
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        verInicio = False
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posMouse = event.pos
                        
                        if clicou(posMouse, botaoVoltar, posBotaoVoltar):
                                print("Voltando pro menu:")
                                if escolhaSom == 1:
                                        selectSom.play()
                                        pygame.time.wait(300)
                                verMenu = True
                                running = False
                                instrucaoTela = False
        screen.fill(white)
        screen.blit(botaoVoltar,(xBotaoVoltar,500))                             
           
        pygame.display.update()                  
#-------------SELECIONA PERSONAGEM-------------
#Loop da música
if escolhaSom == 1:
        telaSom.play(-1)
while (selecionar):
        clock.tick(3)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                        posMouse = event.pos
                        if clicou(posMouse, setaE, posE):
                                print('Clicou na Esquerda')
                                if escolhaSom == 1:
                                        setaSom.play()
        
                                if troca == 1:
                                        print("troca==1")
                                        troca = 5

                                elif troca == 2:
                                        print("troca==2")
                                        troca = 1

                                elif troca == 3:
                                        print("troca==3")
                                        troca = 2

                                elif troca == 4:
                                        print("troca==4")
                                        troca = 3

                                elif troca == 5:
                                        print("troca==5")
                                        troca = 4

                                
                        elif clicou(posMouse, setaD, posD):
                                print('Clicou na Direita')
                                if escolhaSom == 1:
                                        setaSom.play()
                                if troca == 1:
                                        print("troca==1")
                                        troca = 2
                                        
                                elif troca == 2:
                                        print("troca==2")
                                        troca = 3
                                        
                                elif troca == 3:
                                        print("troca==3")
                                        troca = 4

                                elif troca == 4:
                                        print("troca==4")
                                        troca = 5
                                              
                                elif troca == 5:
                                        print("troca==5")
                                        troca = 1
                                        
                        elif clicou(posMouse, botaoSelecionar, posBotaoSelecionar):
                                print("Selecionou:" + str(troca))
                                if escolhaSom == 1:
                                        telaSom.stop()
                                        selectSom.play()
                                        pygame.time.wait(300)
                                        
                                selecionar = False
                                running = False
                       
        screen.fill(blue)
        if troca == 1:
                screen.blit(fundoSalao, posFundo)
                screen.blit(botaoHeroi, posBotaoPersonagem)
                #screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(heroiSpritesMenu[sprite_index], posHeroi)
                
        elif troca == 2:
                
                screen.blit(fundoSalao, posFundo)
                screen.blit(botaoCavaleiro, posBotaoPersonagem)
                #screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(cavaleiroSpritesMenu[sprite_index],posCavaleiro)
        
        elif troca == 3:
                screen.blit(fundoSalao, posFundo)
                screen.blit(botaoFeiticeira, posBotaoPersonagem)
                #screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(feiticeiraSpritesMenu[sprite_index],posFeiticeira)
                
        elif troca == 4:
                screen.blit(fundoSalao, posFundo)
                screen.blit(botaoMago, posBotaoPersonagem)                
                #screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(magoSpritesMenu[sprite_index],posMago)

        elif troca == 5:
                screen.blit(fundoSalao, posFundo)
                screen.blit(botaoPrincesa, posBotaoPersonagem)                
                #screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(princesaSpritesMenu[sprite_index],posPrincesa)

        screen.blit(setaD ,  posD)
        screen.blit(setaE ,  posE)
        screen.blit(botaoSelecionar ,   posBotaoSelecionar)


        sprite_index = (sprite_index + 1) % 2
                                
                                        
        pygame.display.update()
print(troca)

screen.fill(black)

#-------------Mugshot-------------
clock.tick(3)
for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

#Compara a variavel troca para saber qual a escolha do usuario
if troca == 1:
        print("HERÓI")
        screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
        mensagem="TESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTE"
        cor = blue
        contadorMensagem=0
        tamanhoMsg = len(mensagem)
        xMensagem=20
        yMensagem = 10
        contadorSprite = 0
        while contadorMensagem != tamanhoMsg - 1:
                texto = font.render(mensagem[contadorMensagem], True, cor)
                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                xMensagem = xMensagem + 20
                if xMensagem == 1280-widthPersonagemMugshot:
                        if yMensagem < 200:
                                xMensagem = 20
                        else:
                                xMensagem =0


                        yMensagem = yMensagem+40
                        
                contadorMensagem = contadorMensagem+1
                if contadorMensagem == tamanhoMsg:
                        break
                #time.sleep(0.1)
                contadorSprite = contadorSprite + 1
                screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
                if contadorSprite == 3:
                        sprite_index = (sprite_index + 1) % 2
                        contadorSprite = 0
                pygame.display.update()

elif troca == 2:
        print("Cavaleiro")      
        screen.blit(cavaleiroSpritesMugshot[sprite_index],posPersonagemMugshot)

elif troca == 3:
        print("Feiticeira")
        screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)

elif troca == 4:
        print("Mago")
        screen.blit(magoSpritesMugshot[sprite_index],posPersonagemMugshot)


elif troca == 5:
        print("Princesa")
        screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)


sprite_index = (sprite_index + 1) % 2
pygame.display.update()
         
#-------------PARA O PROGRAMA-------------
while (running):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
