import pygame
import sys
class seleciona:
        def selecaoPersonagem():
                pygame.init()
                pygame.mixer.init()
                #screen = pygame.display.set_mode( (0,0),pygame.FULLSCREEN )

                #Tamanho da Tela
                widthScreen = 800
                heighScreen = 600 

                screen = pygame.display.set_mode( (widthScreen,heighScreen))
                background_color = (56, 32, 14)

                #Carregando imagens e sons 

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

                #Definindo Posições

                #Fundo
                xFundo = 0
                yFundo = -100
                posFundo = (xFundo,yFundo)
                
                #Seta Esquerda
                xEsq = 0 
                yEsq = 100
                posE = (xEsq,yEsq)
                widthE = setaE.get_width()
                heightE = setaE.get_height()

                #Seta Direita
                xDir = 600 
                yDir = 100 
                posD = (xDir,yDir)
                widthD = setaD.get_width()
                heightD = setaD.get_height()

                #Botão Selecionar
                xBotaoSelecionar = 240
                yBotaoSelecionar = 350
                posBotaoSelecionar = (xBotaoSelecionar,yBotaoSelecionar)
                widthBotaoSelecionar = botaoSelecionar.get_width()
                heightBotaoSelecionar = botaoSelecionar.get_height()
                
                #Fundo Personagem 
                xFundoPersonagem = 234
                yFundoPersonagem = 60
                posFundoPersonagem = (xFundoPersonagem,yFundoPersonagem)
                
                #Personagem Geral
                xPersonagem = 315
                yPersonagem = 100
                posPersonagem = (xPersonagem,yPersonagem)
                
                #Variavel que Percorrerá o Array dos Personagens
                sprite_index = 0


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

                #Variavel que definirá qual personagem o usuário escolheu
                troca = 1
                
                screen.fill(background_color)
                clock = pygame.time.Clock()

                #Loop da música
                telaSom.play(-1)

                running = True
                while (running):
                        clock.tick(3)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        running = False
                                        
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
                                                running = False
                                       
                        screen.fill(background_color)
                        if troca == 1:
                                screen.blit(fundoGrama, posFundo)
                                screen.blit(fundoPersonagem, posFundoPersonagem)
                                screen.blit(heroiSpritesMenu[sprite_index], posPersonagem)
                                
                        elif troca == 2:
                                screen.blit(fundoGrama, posFundo)
                                screen.blit(fundoPersonagem, posFundoPersonagem)
                                screen.blit(cavaleiroSpritesMenu[sprite_index],posPersonagem)
                        
                        elif troca == 3:
                                screen.blit(fundoGrama, posFundo)
                                screen.blit(fundoPersonagem, posFundoPersonagem)
                                screen.blit(feiticeiraSpritesMenu[sprite_index],posPersonagem)
                                
                        elif troca == 4:
                                screen.blit(fundoGrama, posFundo)
                                screen.blit(fundoPersonagem, posFundoPersonagem)
                                screen.blit(magoSpritesMenu[sprite_index],posPersonagem)

                        elif troca == 5:
                                screen.blit(fundoGrama, posFundo)
                                screen.blit(fundoPersonagem, posFundoPersonagem)
                                screen.blit(princesaSpritesMenu[sprite_index],posPersonagem)

                        screen.blit(setaD ,  posD)
                        screen.blit(setaE ,  posE)
                        screen.blit(botaoSelecionar ,   posBotaoSelecionar)


                        sprite_index = (sprite_index + 1) % 2
                                                
                                                        
                        pygame.display.update()

                pygame.quit()
                print(troca)
                return troca
seleciona.selecaoPersonagem()
