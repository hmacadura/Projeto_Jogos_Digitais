import pygame
import sys
import time
import quadrados
pygame.init()
pygame.mixer.init()

#Tamanho da Tela
widthScreen = 1280
heightScreen = 720

#-------------TELA CHEIA-------------
#screen = pygame.display.set_mode( (widthScreen,heightScreen),pygame.FULLSCREEN )

#-------------JANELA NORMAL-------------
screen = pygame.display.set_mode( (widthScreen,heightScreen))

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
zelda = pygame.mixer.Sound("../../../Sounds/temaZelda.wav")

vitoriaSom = pygame.mixer.Sound("../../../Sounds/overwatchVitory.wav")

somTabuleiro = pygame.mixer.Sound("../../../Sounds/07-spirit-of-hospitality.wav")

derrotaSom = pygame.mixer.Sound("../../../Sounds/03-resurrections.wav")

setaSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoTroca.wav")

selectSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoSelect.wav")
#-------------------------------------------Imagens-----------------------------
#TESTE PRA SABER QUAL TELA ESCOLHER 
fundoTelaInicio = pygame.image.load("../../../Sprites/Fundo/telaInicioComTituloVermelho.png").convert_alpha()

fundoCaverna = pygame.image.load("../../../Sprites/Fundo/fundoCaverna.png").convert_alpha()

fundoVitoria = pygame.image.load("../../../Sprites/Fundo/fundoVitoria.png").convert_alpha()

fundoDerrota = pygame.image.load("../../../Sprites/Fundo/gramaSol.png").convert_alpha()

tabuleiro = pygame.image.load("../../../Sprites/Fundo/tabuleiroComSimbolos.png").convert_alpha()

fundoSalao = pygame.image.load("../../../Sprites/Fundo/fundoSalao.png").convert_alpha()

molduraMugshot = pygame.image.load("../../../Sprites/Menu/molduraMugshot.png").convert_alpha()

setaD = pygame.image.load("../../../Sprites/Menu/setaDirBorda.png").convert_alpha()

setaE = pygame.image.load("../../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

botaoSelecionar = pygame.image.load("../../../Sprites/Menu/botaoSelect.png").convert_alpha()

botaoIniciar = pygame.image.load("../../../Sprites/Menu/botaoIniciar.png").convert_alpha()

botaoOpcoes = pygame.image.load("../../../Sprites/Menu/botaoOpcoes.png").convert_alpha()

botaoInstrucoes = pygame.image.load("../../../Sprites/Menu/botaoInstrucoes.png").convert_alpha()

botaoTentarNovamente = pygame.image.load("../../../Sprites/Menu/botaoTentarNovamente.png").convert_alpha()

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

podium = pygame.image.load("../../../Sprites/Menu/podium720.png").convert_alpha()

fundoTelaInstrucao = pygame.image.load("../../../Sprites/Fundo/telaInstrucao.png").convert_alpha()

cavaleiroNegroVitoria = pygame.image.load("../../../Sprites/Personagens/Cavaleiro Negro/Sprites Sem Sombras/CavaleiroNegroSemSombraGanhou.png").convert_alpha()

cavaleiroNegroDerrota = pygame.image.load("../../../Sprites/Personagens/Cavaleiro Negro/Sprites Sem Sombras/CavaleiroNegroSemSombra11.png").convert_alpha()

#-----------SELEÇÃO-------------------------
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

#Botão Tentar Novamente
widthBotaoTentarNovamente = botaoTentarNovamente.get_width()
heightBotaoTentarNovamente = botaoTentarNovamente.get_height()

#Ícone Som
widthIconeSom = iconeComSom.get_width()
heightIconeSom = iconeComSom.get_height()

#Fundo Personagem 
widthFundoPersonagem = fundoPersonagem.get_width()
heightFundoPersonagem = fundoPersonagem.get_height()

#Personagem Mugshot
widthPersonagemMugshot = heroiSpritesMugshot[sprite_index].get_width()
heightPersonagemMugshot = heroiSpritesMugshot[sprite_index].get_height()

#Moldura Mugshot
widthMolduraMugshot = molduraMugshot.get_width()
heightMolduraMugshot = molduraMugshot.get_height()

#Cavleiro Negro Vitoria
widthCavaleiroNegroVitoria = cavaleiroNegroVitoria.get_width()
heightCavaleiroNegroVitoria = cavaleiroNegroVitoria.get_height()

#Cavleiro Negro Derrota
widthCavaleiroNegroDerrota = cavaleiroNegroDerrota.get_width()
heightCavaleiroNegroDerrota = cavaleiroNegroDerrota.get_height()

#Podium
widthPodium = podium.get_width()
heightPodium = podium.get_height()

#-------------Definindo Posições-------------

#Fundo
xFundo = 0
yFundo = 0
posFundo = (xFundo,yFundo)

#Podium
xPodium = widthScreen/2 - widthPodium/2
yPodium = heightScreen/2 - heightPodium/2.25
posPodium = (xPodium,yPodium)

#Cavleiro Negro Vitoria
xCavaleiroNegroVitoria = widthScreen/2 - widthCavaleiroNegroVitoria/2
yCavaleiroNegroVitoria = heightScreen/2 - heightCavaleiroNegroVitoria/1.2
posCavaleiroNegroVitoria = (xCavaleiroNegroVitoria,yCavaleiroNegroVitoria)

#Cavleiro Negro Derrota
xCavaleiroNegroDerrota = widthScreen/2 - widthCavaleiroNegroDerrota*1.6
yCavaleiroNegroDerrota = heightScreen/2 - heightCavaleiroNegroDerrota/1.75
posCavaleiroNegroDerrota = (xCavaleiroNegroDerrota,yCavaleiroNegroDerrota)

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
yBotaoVoltar = 3*heightScreen/4 + heightBotaoVoltar/3 
posBotaoVoltar = (xBotaoVoltar,yBotaoVoltar)

#Botão TentarNovamente
xBotaoTentarNovamente = widthScreen/2 - widthBotaoTentarNovamente/2
yBotaoTentarNovamente = heightScreen/2 + heightBotaoTentarNovamente*1.75
posBotaoTentarNovamente = (xBotaoTentarNovamente,yBotaoTentarNovamente)

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
xPersonagemMugshot = 15
yPersonagemMugshot = 15
posPersonagemMugshot = (xPersonagemMugshot,yPersonagemMugshot)

#Moldura Mugshot
xMolduraMugshot = xPersonagemMugshot - 15
yMolduraMugshot = yPersonagemMugshot - 15
posMolduraMugshot = (xMolduraMugshot,yMolduraMugshot)

clock = pygame.time.Clock()

#Variavel que definirá qual personagem o usuário escolheu
troca = 1

#Variavel que definirá se tem som
escolhaSom = 1

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
verHistoria = False

#Variavel para parar o Jogo
jogo = True

#Variavel para saber o resultado
resultado = True

condicao = 0

#Funções
#-------------Tela jogo-------------
def telaJogo(ValorSom,troca):
        print("bora")
        valorSom = escolhaSom
        while jogo == True:
                screen.blit(fundoCaverna ,posFundo)
                screen.blit(tabuleiro ,posFundo)
                clock.tick(60)
                resposta = quadrados.tabuleiro(ValorSom,troca)
                telaFinal(ValorSom,troca)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                verInicio = False
                                pygame.quit()
                                sys.exit()                
                pygame.display.update()
                
#-------------Tela Início-------------
def telaInicio():
                #Loop da música
        if escolhaSom == 1:
                zelda.play(-1)
        while True:
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
                                        running = False
                                        verInicio = False
                                        return
                pygame.display.update()
        
#-------------Tela Menu-------------
def telaMenu(ValorSom):
        escolhaSom = ValorSom
        while True:
                clock.tick(60)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                verInicio = False
                                pygame.quit()
                                sys.exit()
                                
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                posMouse = event.pos
                                if escolhaSom == 1:
                                                selectSom.play()
                                if clicou(posMouse, botaoIniciar, posBotaoIniciar):
                                        escolhaSom = telaSeleciona(escolhaSom)
                                        print("Entrando no Jogo:")
                                        #if escolhaSom == 1:
                                         #       selectSom.play()
                                                                                        
                                elif clicou(posMouse, botaoInstrucoes, posBotaoInstrucoes):
                                        escolhaSom = telaInstrucao(escolhaSom)
                                        print("Entrando na Tela de Instruções:")
                                        if escolhaSom == 1:
                                                selectSom.play()
                                                                                                                                     
                                elif clicou (posMouse, botaoOpcoes, posBotaoOpcoes):
                                        escolhaSom = telaSom(escolhaSom)
                                        print("Entrando na Tela de Som:")
                                        if escolhaSom == 1:
                                                selectSom.play()
                                        
                screen.blit(fundoTelaInicio , posFundo)
                screen.blit(botaoIniciar    , posBotaoIniciar)
                screen.blit(botaoInstrucoes , posBotaoInstrucoes)        
                screen.blit(botaoOpcoes     , posBotaoOpcoes)                             
                pygame.display.update()

#-------------Tela Som-------------
def telaSom(ValorSom):
        escolhaSom = ValorSom
        while True:
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
                                        return escolhaSom

                                if clicou (posMouse, iconeComSom, posIconeSom):
                                        print("Menu de Som:")                                        
                                        if escolhaSom == 0:
                                                selectSom.play()
                                                zelda.play()
                                                print("escolhaSom == 0")
                                                escolhaSom = 1

                                        elif escolhaSom == 1:
                                                zelda.stop()
                                                print("escolhaSom == 1")
                                                escolhaSom = 0
                                                

                screen.fill(darkSlateGray)
                if escolhaSom == 1:
                        screen.blit(botaoComSom,posBotaoComSom)
                        screen.blit(iconeComSom,posIconeSom)
                        print("Jogo está COM Som")
                elif escolhaSom == 0:
                        screen.blit(botaoSemSom,posBotaoSemSom)
                        screen.blit(iconeSemSom,posIconeSom)
                        print("Jogo está SEM Som")
                screen.blit(botaoVoltar,posBotaoVoltar)                             
                pygame.display.update()


def telaInstrucao(ValorSom):
        escolhaSom = True
#-------------Tela Instruções-------------
        while True:
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
                                        return escolhaSom
                screen.fill(white)
                screen.blit(fundoTelaInstrucao,posFundo)                             
                screen.blit(botaoVoltar,posBotaoVoltar)                             
                   
                pygame.display.update()

def telaSeleciona(ValorSom):
        #Variavel que Percorrerá o Array das Sprites
        sprite_index = 0
        troca = 1
        escolhaSom = ValorSom
#-------------SELECIONA PERSONAGEM-------------

        while True:
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
                                                selectSom.play()
                                        screen.fill(black)
                                        telaMugshot(escolhaSom,troca,condicao)
                                        return troca and escolhaSom

                                        
                               
                screen.fill(blue)
                if troca == 1:
                        screen.blit(fundoSalao, posFundo)
                        screen.blit(botaoHeroi, posBotaoPersonagem)
                        screen.blit(heroiSpritesMenu[sprite_index], posHeroi)
                        
                elif troca == 2:
                        
                        screen.blit(fundoSalao, posFundo)
                        screen.blit(botaoCavaleiro, posBotaoPersonagem)
                        screen.blit(cavaleiroSpritesMenu[sprite_index],posCavaleiro)
                
                elif troca == 3:
                        screen.blit(fundoSalao, posFundo)
                        screen.blit(botaoFeiticeira, posBotaoPersonagem)
                        screen.blit(feiticeiraSpritesMenu[sprite_index],posFeiticeira)
                        
                elif troca == 4:
                        screen.blit(fundoSalao, posFundo)
                        screen.blit(botaoMago, posBotaoPersonagem)                
                        screen.blit(magoSpritesMenu[sprite_index],posMago)

                elif troca == 5:
                        screen.blit(fundoSalao, posFundo)
                        screen.blit(botaoPrincesa, posBotaoPersonagem)                
                        screen.blit(princesaSpritesMenu[sprite_index],posPrincesa)

                screen.blit(setaD ,  posD)
                screen.blit(setaE ,  posE)
                screen.blit(botaoSelecionar ,   posBotaoSelecionar)


                sprite_index = (sprite_index + 1) % 2
                                        
                                                
                pygame.display.update()
        print(troca)
        
def telaMugshot(ValorSom,troca, condicao):
        escolhaSom = ValorSom
        #Variavel que Percorrerá o Array das Sprites
        sprite_index = 0
#-------------Mugshot-------------
        clock.tick(60)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False
                                pygame.quit()
                                sys.exit()

                #Compara a variavel troca para saber qual a escolha do usuario
                        if troca == 1:
                                #Importanto a fonte
                                font = pygame.font.Font('../../../Fonte/cour.ttf', 32) 
                                print("HERÓI")
                                screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
                                screen.blit(molduraMugshot, posMolduraMugshot)
                                if condicao ==0:
                                        condicao = condicao + 1
                                        print ("condição: " + str(condicao))
                                        mensagem = "Olá meu nome é Arthur, sou o herói do reino.        " +\
                                                   "Já derrotei exércitos, monstros e dragões!"+\
                                                   "Quando    finalmente retornei de minha jornada em busca da    pedra filosofal, ouço comerciantes comentando sobre os eventos dos últimos dias." +\
                                                   "Aparentemente, um       Cavaleiro Negro apareceu em nosso Reino e destronou nosso sábio Rei Davi." +\
                                                   "Existe uma lei milenar em nosso  reino.    Caso o Rei não esteja governando corretamente, qualquer  pessoa poderá desafiá-lo para o Desafio Matemático." +\
                                                   "Uma corrida  em     turnos, que se passa pela caverna do Bruxo Sebastian o Justo." +\
                                                   "   A cada turno o participante rolará um dado e terá que fazer a   soma entre o número tirado no dado, com a casa que estava, para se deslocar até a nova." +\
                                                   "O primeiro que chegar a casa 100 terá    direito ao trono! Preciso ajudá-lo, EM NOME DO REI! " +\
                                                   "                                CLIQUE PARA CONTINUAR! "
                                        
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:     
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos

                                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                                print("Saindo da Tela Mugshot:")
                                                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        pygame.mixer.pause()
                                                running = False
                                                verHistoria = False
                                                telaJogo(escolhaSom,troca)
                                                return troca and escolhaSom
                                                pygame.display.update()

              
                        elif troca == 2:
                                #Importanto a fonte
                                font = pygame.font.Font('C:\Windows\Fonts\cour.ttf', 25) 
                                print("Cavaleiro")      
                                screen.blit(cavaleiroSpritesMugshot[sprite_index],posPersonagemMugshot)
                                screen.blit(molduraMugshot, posMolduraMugshot)
                                if condicao ==0:
                                        condicao = condicao + 1
                                        print ("condição: " + str(condicao))
                                        mensagem = "Olá meu nome é Valentin, sou o cavaleiro chefe da   guarda real." +\
                                                   "Sirvo vossa majestade o Rei Davi desde  que ele era príncipe." +\
                                                   "Ontem um viajante chegou ao    reino em busca de conselhos reais." +\
                                                   "Como vossa        majestade auxilia todos no reino, agendou um tempo  para falar com esse viajante." +\
                                                   "Eu estava almoçando    quando ouvi os gritos e vi as pessoas correndo do palácio." +\
                                                   "O Rei Davi tinha sido destronado e o viajante se apresentou ao Reino  como o Cavaleiro Negro o Novo Rei." +\
                                                   "Ele prendeu o Rei Davi e o    resto dos meus soldados na prisão real!" +\
                                                   "Mas descobri um jeito de salvá-lo! Existe uma lei milenar em nosso reino. " +\
                                                   "Caso o Rei não esteja governando corretamente, qualquer pessoa poderá          desafiá-lo para o Desafio Matemático." +\
                                                   "Uma corrida em turnos, que se passa pela   caverna do Bruxo Sebastian o Justo. " +\
                                                   "A cada turnoo participante rolará um dado e terá que fazer a soma entre o   número tirado no dado, com a casa que estava, para se deslocar  até a nova. " +\
                                                   "O primeiro que chegar a casa 100 terá direito ao    trono! Preciso ajudá-lo, EM NOME DO REI! " +\
                                                   "                                           CLIQUE PARA CONTINUAR! "
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(cavaleiroSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos

                                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                                print("Saindo da Tela Mugshot:")
                                                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        pygame.mixer.pause()
                                                running = False
                                                verHistoria = False
                                                telaJogo(escolhaSom,troca)
                                                return troca and escolhaSom
                                                pygame.display.update()
                                                
                        elif troca == 3:
                                #Importanto a fonte
                                font = pygame.font.Font('C:\Windows\Fonts\cour.ttf', 25) 
                                print("Feiticeira")
                                screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)
                                screen.blit(molduraMugshot, posMolduraMugshot)
                                if condicao ==0:
                                        condicao = condicao + 1
                                        print ("condição: " + str(condicao))
                                        mensagem = "Olá meu nome é Pandora, sou uma Feiticeira." +\
                                                   "Moro     próximo ao grande Reino." +\
                                                   "Minha mãe a Feiticeira      Morgana não foi a melhor pessoa do mundo." +\
                                                   "Pode se    dizer que fomos banidos do Reino pelo Mago Gaspar,  algo sobre minha mãe ter roubando seus pergaminhos  sagrados." +\
                                                   "Minha mãe se foi e ainda não sou aceita lá.Vendo minhas poções de cura e ataque nos portões com diversos   aventureiros." +\
                                                   "É lá onde descubro as novidades da grande          civilização. Foi quando descobri que o Rei Davi tinha sido      destronado e preso." +\
                                                   "Tive então uma ideia, me teleportei para casae revirei os pergaminhos deixados por minha mãe." +\
                                                   "Achei uma cópia das regras do reino.Existe uma lei milenar em nosso reino." +\
                                                   "Caso oRei não esteja governando corretamente, qualquer pessoa poderá  desafiá-lo para o Desafio Matemático." +\
                                                   "Uma corrida em turnos, que se passa pela caverna do Bruxo Sebastian o Justo." +\
                                                   "A cada turno o participante rolará um dado e terá que fazer a soma entre o     número tirado no dado, com a casa que estava, para se deslocar  até a nova. "
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                        pygame.time.wait(2000)
                                        
                                        screen.fill(black)
                                        screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)
                                        mensagem = "O primeiro que chegar a casa 100 terá direito ao    trono! Se eu vencer e ajudá-lo, poderei ser aceita  novamente no Reino! " +\
                                                   "Então vamos lá, EM NOME DO REI. " +\
                                                   "            CLIQUE PARA CONTINUAR!"
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos

                                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                                print("Saindo da Tela Mugshot:")
                                                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        pygame.mixer.pause()
                                                running = False
                                                verHistoria = False
                                                telaJogo(escolhaSom,troca)
                                                return troca and escolhaSom
                                                pygame.display.update()

                        elif troca == 4:
                                #Importanto a fonte
                                font = pygame.font.Font('C:\Windows\Fonts\cour.ttf', 25) 
                                print("Mago")
                                screen.blit(magoSpritesMugshot[sprite_index],posPersonagemMugshot)
                                screen.blit(molduraMugshot, posMolduraMugshot)
                                if condicao ==0:
                                        condicao = condicao + 1
                                        print ("condição: " + str(condicao))
                                        mensagem = "Olá meu nome é Gaspar, sou o Mago do Reino." +\
                                                   "Meu papelno Reino é criar poções de curas para os hospitais eproteger os pergaminhos sagrados da biblioteca      central." +\
                                                   "Era um dia normal, estava levando as poções para o hospital central, quando senti uma energia   maligna saindo do castelo do Rei Davi." +\
                                                   "Quando estava caminhando até o palácio, encontrei a Princesa Sofia nos degrausda Biblioteca central, ela me explicou o que aconteceu." +\
                                                   "Não pude deixá-la sozinha enquanto esse Cavaleiro Negro se proclamava    Rei." +\
                                                   "Procuramos os antigos livros de leis. Neles descobrimos que existe uma forma! Existe uma lei milenar em nosso reino." +\
                                                   "Caso o  Rei não esteja governando corretamente, qualquer pessoa poderá  desafiá-lo para o Desafio Matemático." +\
                                                   "Uma corrida em turnos, que se passa pela caverna do Bruxo Sebastian o Justo." +\
                                                   "A cada turno o participante rolará um dado e terá que fazer a soma entre o     número tirado no dado, com a casa que estava, para se deslocar até a nova." +\
                                                   "O primeiro que chegar a casa 100 terá direito ao      trono! Preciso ajudá-lo, EM NOME DO REI! " +\
                                                   "                                             CLIQUE PARA CONTINUAR! "
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(magoSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos

                                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                                print("Saindo da Tela Mugshot:")
                                                #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        pygame.mixer.pause()
                                                running = False
                                                verHistoria = False
                                                telaJogo(escolhaSom,troca)
                                                return troca and escolhaSom
                                                pygame.display.update()


                        elif troca == 5:
                                #Importanto a fonte
                                font = pygame.font.Font('C:\Windows\Fonts\cour.ttf', 25) 
                                print("Princesa")
                                screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)
                                screen.blit(molduraMugshot, posMolduraMugshot)
                                if condicao ==0:
                                        condicao = condicao + 1
                                        print ("condição: " + str(condicao))
                                        mensagem = "Olá meu nome é Sofia, sou a Princesa do Reino." +\
                                                   "Meu   pai, o Rei Davi é o homem mais bondoso do Reino,ele sempre ajuda os seus súditos." +\
                                                   "Hoje foi um horrível   dia para meu pai. Teria sido um dia comum, porém    quando foi ajudar o viajante." +\
                                                   "O mesmo, tirou seu     disfarce e se apresentou na sala do trono como o    Cavaleiro Negro,  e disse que caso o Rei não quisesse morrer," +\
                                                   "   teria que renunciar à coroa! Olhei para meu pai e ele fez o     sinal para que eu fugisse com o restante dos súditos." +\
                                                   "O CavaleiroNegro prendeu meu pai na prisão real. Como princesa, não posso  ficar parada!" +\
                                                   "Lendo os antigos livros sobre nossas leis, descobriuma forma de salvá-lo! Existe uma lei milenar em nosso reino." +\
                                                   "   Caso o Rei não esteja governando corretamente, qualquer pessoa  poderá desafiá-lo para o Desafio Matemático." +\
                                                   "Uma corrida em      turnos, que se passa pela caverna do Bruxo Sebastian o Justo. "
                                        
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                #time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()

                                        pygame.time.wait(2000)
                                        
                                        screen.fill(black)
                                                
                                        screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)
                                        mensagem = "A cada turno o participante rolará um dado e terá   que fazer a soma entre o número tirado no dado, com a casa que estava, para se deslocar até a nova." +\
                                                   "     O primeiro que chegar a casa 100 terá direito ao    trono! Preciso ajudá-lo, EM NOME DO REI! " +\
                                                   "                        CLIQUE PARA CONTINUAR!"
                                        cor = white
                                        contadorMensagem = 0
                                        tamanhoMsg = len(mensagem)
                                        xMensagem = 40
                                        yMensagem = 10
                                        contadorSprite = 0
                                        while contadorMensagem != tamanhoMsg - 1:
                                                texto = font.render(mensagem[contadorMensagem], True, cor)
                                                screen.blit(texto, [widthPersonagemMugshot + xMensagem , yMensagem])
                                                xMensagem = xMensagem + 20
                                                if xMensagem == 1280 - widthPersonagemMugshot:
                                                        if yMensagem < 180:
                                                                xMensagem = 40
                                                        else:
                                                                xMensagem = -200
                                                        yMensagem = yMensagem+37
                                                        
                                                contadorMensagem = contadorMensagem+1
                                                if contadorMensagem == tamanhoMsg:
                                                        break
                                                time.sleep(0.05)
                                                contadorSprite = contadorSprite + 1
                                                screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)
                                                screen.blit(molduraMugshot, posMolduraMugshot)
                                                if contadorSprite == 3:
                                                        sprite_index = (sprite_index + 1) % 2
                                                        contadorSprite = 0
                                                pygame.display.update()
                                                
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos

                                        if clicou(posMouse,fundoTelaInicio, posFundo):
                                                print("Saindo da Tela Mugshot:")
                                               #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        pygame.mixer.pause()
                                                running = False
                                                verHistoria = False
                                                telaJogo(escolhaSom,troca)
                                                return troca and escolhaSom
                                                pygame.display.update()
                                                

                                                #CRIAR UM WHILE TRUE PARA CADA MENSAGEM DANDO RETURN
                                                
                                sprite_index = (sprite_index + 1) % 2
                                pygame.display.update()
def telaFinal(ValorSom,troca):
        escolhaSom = ValorSom
#----------------------TELA FINAL--------------------
        while True:
                somTabuleiro.stop()
                clock.tick(60)
                if resultado == False:
                        if escolhaSom == 1 :
                                derrotaSom.play()
                        
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        verInicio = False
                                        pygame.quit()
                                        sys.exit()
                                                               
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos
                                        
                                        
                                        if clicou(posMouse, botaoTentarNovamente, posBotaoVoltar):
                                                print("Voltando pro menu:")
                                                derrotaSom.stop()
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        derrotaSom.stop()
                                                return
                                                
                        screen.blit(fundoDerrota,posFundo)                             
                        screen.blit(podium,posPodium)
                        screen.blit(cavaleiroNegroVitoria,posCavaleiroNegroVitoria)
                        if troca == 1:
                                screen.blit(heroiSpritesMenu[sprite_index], (xCavaleiroNegroDerrota + 15,yCavaleiroNegroDerrota))
                                
                        elif troca == 2:
                                screen.blit(cavaleiroSpritesMenu[sprite_index],(xCavaleiroNegroDerrota + 15,yCavaleiroNegroDerrota))
                        
                        elif troca == 3:
                                screen.blit(feiticeiraSpritesMenu[sprite_index],(xCavaleiroNegroDerrota + 15,yCavaleiroNegroDerrota))
                                
                        elif troca == 4:            
                                screen.blit(magoSpritesMenu[sprite_index],(xCavaleiroNegroDerrota + 15,yCavaleiroNegroDerrota))

                        elif troca == 5:          
                                screen.blit(princesaSpritesMenu[sprite_index],(xCavaleiroNegroDerrota + 15,yCavaleiroNegroDerrota))
                        screen.blit(botaoTentarNovamente,posBotaoTentarNovamente)                             
                           
                        pygame.display.update()
                        
                elif resultado == True:
                        if escolhaSom == 1 :
                                zelda.stop()
                                vitoriaSom.play()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        verInicio = False
                                        pygame.quit()
                                        sys.exit()
                                                               
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posMouse = event.pos
                                        
                                        if clicou(posMouse, botaoTentarNovamente, posBotaoVoltar):
                                                print("Voltando pro menu:")
                                                vitoriaSom.stop()
                                                derrotaSom.stop()
                                                if escolhaSom == 1:
                                                        selectSom.play()
                                                        vitoriaSom.stop()
                                                return
                                                
                                                
                        screen.blit(fundoVitoria,posFundo)                             
                        screen.blit(podium,posPodium)
                        screen.blit(cavaleiroNegroDerrota,posCavaleiroNegroDerrota)
                        if troca == 1:
                                screen.blit(heroiSpritesMenu[sprite_index], (xCavaleiroNegroVitoria + 17.5,yCavaleiroNegroVitoria + 15))
                                
                        elif troca == 2:
                                screen.blit(cavaleiroSpritesMenu[sprite_index],(xCavaleiroNegroVitoria + 17.5,yCavaleiroNegroVitoria + 15))
                        
                        elif troca == 3:
                                screen.blit(feiticeiraSpritesMenu[sprite_index],(xCavaleiroNegroVitoria + 17.5,yCavaleiroNegroVitoria + 15))
                                
                        elif troca == 4:            
                                screen.blit(magoSpritesMenu[sprite_index],(xCavaleiroNegroVitoria + 17.5,yCavaleiroNegroVitoria + 15))

                        elif troca == 5:          
                                screen.blit(princesaSpritesMenu[sprite_index],(xCavaleiroNegroVitoria + 17.5,yCavaleiroNegroVitoria + 15))
                        screen.blit(botaoTentarNovamente,posBotaoTentarNovamente)                             
                           
                        pygame.display.update()

   
while True:
        if verInicio == True:
                telaInicio()
                escolhaSom = telaMenu(escolhaSom)
                

                        
        
                
        



 
              



#-------------PARA O PROGRAMA-------------
while (running):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
