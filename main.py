"Главный файл для запуска программы"

import pygame, sys
from gameObject import *
from locations import *
from information import *
from invSlotObject import *

#Initialize pygame
pygame.init()
pygame.mixer.init()
windowSize = (1024, 768)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

#Resources
background = locationObjectsList["bedroom"]
currentTextMessage = TextObject(None, 10, (0, 0, 0), "", 1, logo)
isInventory = False

#переменные, обеспечивающие смену власти
altFor = 1
altBack = 1
altLeft = 1
altRight = 1
freq = 10 #то есть кадр анимации ходьбы персонажа сменяется каждые 10 кадров
freqStep = -10

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #задаю координаты гг
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
    x, y = background.checkIfOutBoundary(character["charStand"], (x, y))

    #"рисую на экране" задник
    screen.blit(background.background, (0, 0))

    #ОБЪЕКТЫ, которые можно взять
    for i in range(len(background.itemObjectsList)):
        if background.itemObjectsList[i].isVisible:
            screen.blit(background.itemObjectsList[i].image, (background.itemObjectsList[i].x, background.itemObjectsList[i].y))
        if logo.intersects(background.itemObjectsList[i], 10) and background.itemObjectsList[i].isVisible:
            if invSlots[len(invSlots)-1].isFull:
                break
            if pressed[pygame.K_e]:
                background.itemObjectsList[i].setIsVisible(0)
                for j in range(len(invSlots)-1):
                    if not invSlots[j+1].isFull:
                        invSlots[j+1].setItem(background.itemObjectsList[i])
                        invSlots[j+1].setIsFull(1)
                        break
            else:
                background.itemObjectsList[i].ask(logo, screen, pygame.image.load("images/icons/hand.png"))

    #реализую перемещение персонажа
    pressed = pygame.key.get_pressed()
    if not pressed[pygame.K_w] and not pressed[pygame.K_s] and not pressed[pygame.K_d] and not pressed[pygame.K_a]:
        screen.blit(character["charStand"], (x, y))
    if pressed[pygame.K_w]:
        y -= 5
        if altFor:
            screen.blit(character["charBack1"], (x, y))
            altFor = 0
        else:
            screen.blit(character["charBack2"], (x, y))
            altFor = 1
    if pressed[pygame.K_s]:
        y += 5
        if altBack:
            screen.blit(character["charFor1"], (x, y))
            altBack = 0
        else:
            screen.blit(character["charFor2"], (x, y))
            altBack = 1
    if pressed[pygame.K_d]:
        x += 5
        if altRight:
            screen.blit(character["charRight1"], (x, y))
            altRight = 0
        else:
            screen.blit(character["charRight2"], (x, y))
            altRight = 1
    if pressed[pygame.K_a]:
        x -= 5
        if altLeft:
            screen.blit(character["charLeft1"], (x, y))
            altLeft = 0
        else:
            screen.blit(character["charLeft2"], (x, y))
            altLeft = 1

    #Проверяю, нажати ли кнопка вызова инвенторя
    if pressed[pygame.K_q]:
        isInventory = True
    if pressed[pygame.K_ESCAPE]:
        isInventory = False

    #Проверяю гг на предмет пересечения с текстовыми зонами, если есть нажатие, вывожу текст на экран
    for i in range(len(background.textObjectsList)):
        if logo.intersects(background.textObjectsList[i].object, 10):
            if pressed[pygame.K_e]:
                background.textObjectsList[i].setIsVisible(1)
            elif background.textObjectsList[i].isVisible == 1:
                background.textObjectsList[i].draw(logo, screen)
            else:
                background.textObjectsList[i].ask(logo, screen, pygame.image.load("images/icons/eye.png"))
        else:
            background.textObjectsList[i].setIsVisible(0)

    #вывожу инвентарь на экран
    if isInventory:
        screen.blit(inv.image, (windowSize[0]//2 - inv.width//2, windowSize[1]//2 - inv.height//2))
        for i in range(len(invSlots)):
            if invSlots[i].isFull:
                invSlots[i].drawItem(screen)

    pygame.display.update()
