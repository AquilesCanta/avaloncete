import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.font.init()

VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

windowSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cubo loco')

x = 212
y = 160
pasos = 3

while True:
    windowSurface.fill(BLANCO)
    pygame.draw.rect(windowSurface, VERDE, (x, y, 200, 200), 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        x -= pasos
    if key_input[pygame.K_UP]:
        y -= pasos
    if key_input[pygame.K_RIGHT]:
        x += pasos
    if key_input[pygame.K_DOWN]:
        y += pasos
    pygame.display.update()
