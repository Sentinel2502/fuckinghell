import pygame, sys
import GameObject
from GameObject import *

#Initialize pygame
pygame.init()
pygame.mixer.init()
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
