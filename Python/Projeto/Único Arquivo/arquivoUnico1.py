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

#Variavel que Percorrerá o Array das Sprites
sprite_index = 0

#-------------Carregando imagens e sons Para Seleção de Personagens-------------

telaSom = pygame.mixer.Sound("../../../Sounds/temaZelda.wav")

setaSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoTroca.wav")

selectSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoSelect.wav")

fundoSalao = pygame.image.load("../../../Sprites/Fundo/fundoSalao.png").convert_alpha()

setaD = pygame.image.load("../../../Sprites/Menu/setaDirBorda.png").convert_alpha()

setaE = pygame.image.load("../../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

botaoSelecionar = pygame.image.load("../../../Sprites/Menu/botaoSelect.png").convert_alpha()

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

#-------------Carregando imagens e sons Para Mugshots-------------
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


#Botão Selecionar
xBotaoSelecionar = widthScreen/2 - widthBotaoSelecionar/2
yBotaoSelecionar = heightScreen/2 - heightBotaoSelecionar*1.5
posBotaoSelecionar = (xBotaoSelecionar,yBotaoSelecionar)

#Fundo Personagem 
xFundoPersonagem = widthScreen/2 - widthFundoPersonagem/2
yFundoPersonagem = heightScreen/2 - heightFundoPersonagem/2 
posFundoPersonagem = (xFundoPersonagem,yFundoPersonagem)

#Herói
xHeroi = widthScreen/2 - widthHeroi/2
yHeroi = heightScreen/2 - widthHeroi/1.5
posHeroi = (xHeroi,yHeroi)

#Descrição Personagem
xBotaoPersonagem = widthScreen/2 - widthBotaoPersonagem/2
yBotaoPersonagem = heightScreen - heightBotaoPersonagem/1.3
posBotaoPersonagem = (xBotaoPersonagem,yBotaoPersonagem)

#Cavaleiro  
xCavaleiro = widthScreen/2 - widthCavaleiro/2
yCavaleiro = heightScreen/2 - widthCavaleiro/1.5
posCavaleiro = (xCavaleiro,yCavaleiro)

#Feiticeira  
xFeiticeira = widthScreen/2 - widthFeiticeira/2
yFeiticeira = heightScreen/2 - widthFeiticeira/1.5
posFeiticeira = (xFeiticeira,yFeiticeira)

#Mago  
xMago = widthScreen/2 - widthMago/2
yMago = heightScreen/2 - widthMago/1.5
posMago = (xMago,yMago)

#Princesa  
xPrincesa = widthScreen/2 - widthPrincesa/2
yPrincesa = heightScreen/2 - widthPrincesa/1.5
posPrincesa = (xPrincesa,yPrincesa)

#Personagem Geral Mugshot
xPersonagemMugshot = 10
yPersonagemMugshot = 10
posPersonagemMugshot = (xPersonagemMugshot,yPersonagemMugshot)

screen.fill(blue)

clock = pygame.time.Clock()

#Variavel que definirá qual personagem o usuário escolheu
troca = 1

#Tamanho do Texto
font = pygame.font.Font('freesansbold.ttf', 32)

#-------------Função que escreve na tela-------------
def mensagemTela(mensagem,cor):
        i=0
        tamanhoMsg = len(mensagem)
        a=20
        b = 10
        while i != tamanhoMsg - 1:
                texto = font.render(mensagem[i], True, cor)
                screen.blit(texto, [widthPersonagemMugshot + a , b])
                a = a + 20
                if a == 1280-widthPersonagemMugshot:
                        b = b+40
                        a = 20
                
                i = i+1
                if i == tamanhoMsg:
                        break
                time.sleep(0.1)
                pygame.display.update()

#Loop da música
telaSom.play(-1)

#Variavel para parar o programa geral
running = True

#Variavel para parar o programa Seleção de Personagens
selecionar = True

#Variavel para parar o programa Seleção de Personagens
verHistoria = True
print(widthScreen/2 - widthBotaoSelecionar/2)
#-------------SELECIONA PERSONAGEM-------------
while (selecionar):
        clock.tick(3)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        xMouse, yMouse = event.pos
                
                
                                        
                        if xMouse >= xEsq and xMouse <= widthE and yMouse >= yEsq and yMouse <= yEsq + heightE:
                                print('Clicou na Esquerda')
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

                                
                        
                        elif xMouse >= xDir and xMouse <= 1280 and yMouse >= yDir and yMouse <= yDir + heightD:
                                print('Clicou na Direita')
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
                        elif xMouse >= xBotaoSelecionar and xMouse <= 640 and yMouse >= yBotaoSelecionar and yMouse <= yBotaoSelecionar + heightBotaoSelecionar:
                                print("Selecionou:" + str(troca))
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
        mensagem="TESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTETESTE"
        cor = blue
        i=0
        tamanhoMsg = len(mensagem)
        a=20
        b = 10
        while i != tamanhoMsg - 1:
                texto = font.render(mensagem[i], True, cor)
                screen.blit(texto, [widthPersonagemMugshot + a , b])
                a = a + 20
                if a == 1280-widthPersonagemMugshot:
                        b = b+40
                        a = 20
                
                i = i+1
                if i == tamanhoMsg:
                        break
                time.sleep(0.1)
                screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
                sprite_index = (sprite_index + 1) % 2
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
