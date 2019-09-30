import pygame
from Botao import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((255,255,255))


def refazJanela():
	screen.fill((255,255,255))
	greenButton.draw(screen, (0,0,0))
run = True
greenButton = button((0,255,0), 150, 225, 250, 100, "Clica")
while run :
	refazJanela()
	pygame.display.update()
	
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			if greenButton.isOver(pos):
				print("Clicou")
				
		if event.type == pygame.MOUSEMOTION:
			if greenButton.isOver(pos):
				greenButton.color = (255,0,0)
			else:
				greenButton.color = (0,255,0)
		