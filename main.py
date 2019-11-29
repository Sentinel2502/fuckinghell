"Главный файл для запуска программы"

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
currentTextMessage = TextObject(None, 10, (0, 0, 0), "", 1, logo)
isInventory = False

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    logo.setPosition(x, y)

    #проверяю объекты на предмет столкновения с персонажем
    for i in range(len(background.intersectionObjectsList)):
        if logo.intersects(background.intersectionObjectsList[i], 0):
            if pressed[pygame.K_d]:
                x -= 5
            if pressed[pygame.K_a]:
                x += 5
            if pressed[pygame.K_w]:
                y += 5
            if pressed[pygame.K_s]:
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

    #"рисую на экране" задник и персонажа
    screen.blit(background.background, (0, 0))
    screen.blit(character, (x, y))

    #реализую перемещение персонажа
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 5
    if pressed[pygame.K_s]:
        y += 5
    if pressed[pygame.K_d]:
        x += 5
    if pressed[pygame.K_a]:
        x -= 5

    #Проверяю, нажати ли кнопка вызова инвенторя
    if pressed[pygame.K_q]:
        isInventory = True
    if pressed[pygame.K_ESCAPE]:
        isInventory = False

    #Вывожу на экран текст об объекте с кот. соприкасаюсь и меню
    screen.blit(currentTextMessage.text, (logo.x + logo.width//2, logo.y - logo.width - 10))
    if isInventory:
        screen.blit(inventorySlotObject.image, (512 - inventorySlotObject.width//2, 384 - inventorySlotObject.height//2))

    #проверяю персонажа на предмет столкновения с текстовыми зонами
    for i in range(len(background.textObjectsList)):
        if logo.intersects(background.textObjectsList[i].object, 10):
            if pressed[pygame.K_e]:
                currentTextMessage = background.textObjectsList[i]
            elif currentTextMessage != background.textObjectsList[i]:
                background.textObjectsList[i].ask(logo, screen, pygame.image.load("images/icons/eye.png"))
        else:
            currentTextMessage = TextObject(None, 10, (0, 0, 0), "", 1, logo)

    pygame.display.update()
