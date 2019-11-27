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

#Настраиваю штуки (потом всю информацию о настройках для определенных локаций перенести в отдельный файл)
"""background.setGameField(GameObject(0, 374, 1024, 374))
background.setIntersectionObjectsList(bedroomIntersectionObjectsList)
background.setExitObjectsList(bedroomExitObjectsList)"""

x, y = 710, 575
isIngameField = True

# создаем "хитбокс" для персонажа
logo = GameObject(x, y, characterSize[0], characterSize[1])

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    logo.setPosition(x, y)

    #проверяю объекты на предмет столкновения с персонажем
    for i in range(len(background.intersectionObjectsList)):
        if logo.intersects(background.intersectionObjectsList[i]):
            if pressed[pygame.K_RIGHT]:
                x -= 5
            if pressed[pygame.K_LEFT]:
                x += 5
            if pressed[pygame.K_UP]:
                y += 5
            if pressed[pygame.K_DOWN]:
                y -= 5

    #проверяю персонажа на предмет столкновения с "выходами"ъ
    for i in range(len(background.exitObjectsList)):
        if not logo.intersects(background.exitObjectsList[i][0]):
            pass
        else:
            background = locationObjectsList[background.exitObjectsList[i][1]]
            x, y = background.exit_x, background.exit_y

    #проверяем нахождение персонажа в границах игровой зоны
    if not logo.intersects(background.gameFieldObject):
        if pressed[pygame.K_RIGHT]:
            x -= 5
        if pressed[pygame.K_LEFT]:
            x += 5
        if pressed[pygame.K_UP]:
            y += 5
        if pressed[pygame.K_DOWN]:
            y -= 5

    #реализую движение персонажа по экрану
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        x += 5
    if pressed[pygame.K_LEFT]:
        x -= 5
    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5



    screen.blit(background.background, (0, 0))
    screen.blit(character, (x, y))


    pygame.display.update()
