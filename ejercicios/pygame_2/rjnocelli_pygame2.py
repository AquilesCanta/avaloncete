import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

windowSurface = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Cubo loco')

velocidad = [3,3]

x = 212
y = 160

while True:
    windowSurface.fill(BLANCO)
    pygame.draw.rect(windowSurface, VERDE, (x, y, 200, 200), 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if x>=500:
        velocidad[0] = -velocidad[0]
    if x<=0:
        velocidad[0] = -velocidad[0]
    if y>300:
        velocidad[1] = -velocidad[1]
    if y<0:
        velocidad[1] = -velocidad[1] 

    x += velocidad[0]
    y += velocidad[1]
    pygame.display.update()
