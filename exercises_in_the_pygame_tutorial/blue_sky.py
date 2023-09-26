import pygame

import sys

pygame.init()
run = True
screen = pygame.display.set_mode((900, 600))
bg = (20, 20, 230)
screen.fill(bg)
pygame.display.set_caption("Mr Blue Sky")


while run:
	screen.fill(bg)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()

	pygame.display.flip()		

				