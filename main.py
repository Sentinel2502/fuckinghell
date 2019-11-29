"Главный файл для запуска программы. Нужен для отладки функций движка"

import pygame, sys
from gameObject import *
from locations import *
from information import *

#Initialize pygame
pygame.init()
pygame.mixer.init()
windowSize = (1024, 768)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

#Resources
character = pygame.image.load("images/characters/char.png")
background = locationObjectsList["bedroom"]
characterSize = character.get_size()

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    logo.setPosition(x, y)

    #проверяю объекты на предмет столкновения с персонажем
    for i in range(len(background.intersectionObjectsList)):
        if logo.intersects(background.intersectionObjectsList[i], 0):
            if pressed[pygame.K_RIGHT]:
                x -= 5
            if pressed[pygame.K_LEFT]:
                x += 5
            if pressed[pygame.K_UP]:
                y += 5
            if pressed[pygame.K_DOWN]:
                y -= 5

    #проверяю персонажа на предмет столкновения с "выходами"
    for i in range(len(background.exitObjectsList)):
        if not logo.intersects(background.exitObjectsList[i][0], 0):
            pass
        else:
            background = locationObjectsList[background.exitObjectsList[i][1]]
            x, y = background.exit_x, background.exit_y

    #проверяем нахождение персонажа в границах игровой зоны
    x, y = background.checkIfOutBoundary(character, (x, y))

    screen.blit(background.background, (0, 0))
    screen.blit(character, (x, y))

    #реализую перемещение персонажа
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5
    if pressed[pygame.K_RIGHT]:
        x += 5
    if pressed[pygame.K_LEFT]:
        x -= 5

    #проверяю персонажа на предмет столкновения с текстовыми зонами
    for i in range(len(background.textObjectsList)):
        if logo.intersects(background.textObjectsList[i].object, 10):
            background.textObjectsList[i].ask(logo, screen, pygame.image.load("images/icons/eye.png"), pressed)


    pygame.display.update()
