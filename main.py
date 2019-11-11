import pygame, sys
import GameObject
from GameObject import *

def checkIfOutBoundary(character, x, y):
    if x + characterSize[0] > 800:
        x = 800 - characterSize[0]

    if y + characterSize[1] > 600:
        y = 600 - characterSize[1]

    if y <= 0:
        y = 0
    if x <= 0:
        x = 0

    return x, y

#Initialize pygame
pygame.init()
pygame.mixer.init()
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

#Resources
character = pygame.image.load("images/charactes/ggg.png")
background = pygame.image.load("images/locations/bedroom.png")

characterSize = character.get_size()

x, y = 200, 100

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pressed = pygame.key.get_pressed() #реализую движение персонажа по экрану
    if pressed[pygame.K_RIGHT]:
        x += 5
    if pressed[pygame.K_LEFT]:
        x -= 5
    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5

    x, y = checkIfOutBoundary(character, x, y)

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(character, (x, y))



    pygame.display.update()
