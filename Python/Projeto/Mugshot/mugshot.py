import pygame
import sys
sys.path.insert(1, '..\Selecao')
import selecaoEmFuncao
pygame.init()
pygame.mixer.init()

#Tamanho da Tela
widthScreen = 800
heighScreen = 600
background_color = (0, 0, 155)

screen = pygame.display.set_mode( (widthScreen,heighScreen))

#Carregando imagens e sons 
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

#Chama função de escolher personagem
opcaoPersonagem = selecaoEmFuncao.seleciona.selecaoPersonagem()

pygame.init()
pygame.font.init()
pygame.mixer.init()
#screen = pygame.display.set_mode( (0,0),pygame.FULLSCREEN )

screen = pygame.display.set_mode( (widthScreen,heighScreen))

#Variavel que Percorrerá o Array dos Personagens
sprite_index = 0

#Personagem Geral
xPersonagemMugshot = 10
yPersonagemMugshot = 10
posPersonagemMugshot = (xPersonagemMugshot,yPersonagemMugshot)

#screen.fill(background_color)
clock = pygame.time.Clock()

running = True
while (running):
    clock.tick(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Compara a variavel troca para saber qual a escolha do usuario
    if opcaoPersonagem == 1:
        print("HERÓI")
        screen.blit(heroiSpritesMugshot[sprite_index], posPersonagemMugshot)
        font = pygame.font.Font('freesansbold.ttf', 32) 
        pygame.display.set_caption('Show Text')
        text = font.render('GeeksForGeeks', True, background_color,(255,255,255)) 


    elif opcaoPersonagem == 2:
        print("Cavaleiro")
        screen.blit(cavaleiroSpritesMugshot[sprite_index],posPersonagemMugshot)

    elif opcaoPersonagem == 3:
        print("Feiticeira")
        screen.blit(feiticeiraSpritesMugshot[sprite_index],posPersonagemMugshot)

    elif opcaoPersonagem == 4:
        print("Mago")
        screen.blit(magoSpritesMugshot[sprite_index],posPersonagemMugshot)


    elif opcaoPersonagem == 5:
        print("Princesa")
        screen.blit(princesaSpritesMugshot[sprite_index],posPersonagemMugshot)


    sprite_index = (sprite_index + 1) % 2
    pygame.display.update()
pygame.quit()
exit()
print(troca)
