import pygame
from pygame.locals import *

pygame.init()

pygame.display.set_caption("Pygame1_gorda")

pantalla = pygame.display.set_mode((500, 500))

verde = (0, 255, 0)
blanco = (255 , 255, 255)

x = 50
y = 50

iniciar = True
while iniciar:
    pantalla.fill(blanco)
    pygame.draw.rect(pantalla, verde, (x, y, 100, 100), 0)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            iniciar = False
            pygame.quit()
            key_input = pygame.key.get_pressed()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_DOWN:
                y += 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
    
