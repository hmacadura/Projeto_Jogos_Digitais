import pygame
import sys

pygame.init()
pygame.mixer.init()
#screen = pygame.display.set_mode( (0,0),pygame.FULLSCREEN )

#-------------Definindo Cores-------------
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Tamanho da Tela
widthScreen = 800
heighScreen = 600 

#Variavel que Percorrerá o Array das Sprites
sprite_index = 0

screen = pygame.display.set_mode( (widthScreen,heighScreen))

#-------------Carregando imagens e sons Para Seleção de Personagens-------------

telaSom = pygame.mixer.Sound("../../../Sounds/temaZelda.wav")

setaSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoTroca.wav")

selectSom = pygame.mixer.Sound("../../../Sounds/Efeitos/botaoSelect.wav")

fundoGrama = pygame.image.load("../../../Sprites/Fundo/gramaClaro.png").convert_alpha()

setaD = pygame.image.load("../../../Sprites/Menu/setaDirBorda.png").convert_alpha()

setaE = pygame.image.load("../../../Sprites/Menu/setaEsqBorda.png").convert_alpha()

botaoSelecionar = pygame.image.load("../../../Sprites/Menu/botaoSelect.png").convert_alpha()

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

#Botão Selecionar
widthBotaoSelecionar = botaoSelecionar.get_width()
heightBotaoSelecionar = botaoSelecionar.get_height()

#Fundo Personagem 
widthFundoPersonagem = fundoPersonagem.get_width()
heightFundoPersonagem = fundoPersonagem.get_height()

#-------------Definindo Posições-------------

#Fundo
xFundo = 0
yFundo = -100
posFundo = (xFundo,yFundo)

#Seta Esquerda
xEsq = 0 
yEsq = 100
posE = (xEsq,yEsq)

#Seta Direita
xDir = 600 
yDir = 100 
posD = (xDir,yDir)


#Botão Selecionar
xBotaoSelecionar = widthScreen/2 - widthBotaoSelecionar/2
yBotaoSelecionar = heighScreen - heightBotaoSelecionar
posBotaoSelecionar = (xBotaoSelecionar,yBotaoSelecionar)


#Fundo Personagem 
xFundoPersonagem = widthScreen/2 - widthFundoPersonagem/2
yFundoPersonagem = heighScreen/4 - heightFundoPersonagem/4
posFundoPersonagem = (xFundoPersonagem,yFundoPersonagem)

#Herói
xHeroi = widthScreen/2 - widthHeroi/2
yHeroi = heighScreen/3 - widthHeroi/2
posHeroi = (xHeroi,yHeroi)

#Cavaleiro  
xCavaleiro = widthScreen/2 - widthCavaleiro/2.1
yCavaleiro = heighScreen/3 - widthCavaleiro/2
posCavaleiro = (xCavaleiro,yCavaleiro)

#Feiticeira  
xFeiticeira = widthScreen/2 - widthFeiticeira/2
yFeiticeira = heighScreen/3 - widthFeiticeira/2
posFeiticeira = (xFeiticeira,yFeiticeira)

#Mago  
xMago = widthScreen/2 - widthMago/2
yMago = heighScreen/3 - widthMago/2
posMago = (xMago,yMago)

#Princesa  
xPrincesa = widthScreen/2 - widthPrincesa/2
yPrincesa = heighScreen/3 - widthPrincesa/2
posPrincesa = (xPrincesa,yPrincesa)

#Personagem Geral Mugshot
xPersonagemMugshot = 10
yPersonagemMugshot = 10
posPersonagemMugshot = (xPersonagemMugshot,yPersonagemMugshot)

screen.fill(blue)

clock = pygame.time.Clock()

#Variavel que definirá qual personagem o usuário escolheu
troca = 1

#Loop da música
telaSom.play(-1)

#Variavel para parar o programa geral
running = True

#Variavel para parar o programa Seleção de Personagens
selecionar = True

#Variavel para parar o programa Seleção de Personagens
verHistoria = True

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

                                
                        
                        elif xMouse >= xDir and xMouse <= 800 and yMouse >= yDir and yMouse <= yDir + heightD:
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
                        elif xMouse >= xBotaoSelecionar and xMouse <= 550 and yMouse >= yBotaoSelecionar and yMouse <= yBotaoSelecionar + heightBotaoSelecionar:
                                print("Selecionou:" + str(troca))
                                telaSom.stop()
                                selectSom.play()
                                pygame.time.wait(300)
                                selecionar = False
                                running = False
                       
        screen.fill(blue)
        if troca == 1:
                screen.blit(fundoGrama, posFundo)
                screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(heroiSpritesMenu[sprite_index], posHeroi)
                
        elif troca == 2:
                
                screen.blit(fundoGrama, posFundo)
                screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(cavaleiroSpritesMenu[sprite_index],posCavaleiro)
        
        elif troca == 3:
                screen.blit(fundoGrama, posFundo)
                screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(feiticeiraSpritesMenu[sprite_index],posFeiticeira)
                
        elif troca == 4:
                screen.blit(fundoGrama, posFundo)
                screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(magoSpritesMenu[sprite_index],posMago)

        elif troca == 5:
                screen.blit(fundoGrama, posFundo)
                screen.blit(fundoPersonagem, posFundoPersonagem)
                screen.blit(princesaSpritesMenu[sprite_index],posPrincesa)

        screen.blit(setaD ,  posD)
        screen.blit(setaE ,  posE)
        screen.blit(botaoSelecionar ,   posBotaoSelecionar)


        sprite_index = (sprite_index + 1) % 2
                                
                                        
        pygame.display.update()
print(troca)

screen.fill(black)
#-------------Mugshot-------------
while (verHistoria):
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
                font = pygame.font.Font('freesansbold.ttf', 32) 
                pygame.display.set_caption('Show Text')
                text = font.render('GeeksForGeeks', True, black,(255,255,255)) 


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
