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

#background
background = locationObjectsList["library"]

#данные о персонаже
x, y = background.exit_x, background.exit_y
speed = 5
character = {"charStand": pygame.image.load("images/characters/thing.png"),
"charFor": [pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png")],
"charBack": [pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png")],
"charLeft": [pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png")],
"charRight": [pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png"), pygame.image.load("images/characters/thing.png")]}
characterSize = character["charStand"].get_size()
logo = GameObject(x, y, characterSize[0], characterSize[1])
fps = 8
spriteAm = 3
spriteList = []
for  i in range(spriteAm):
    for j in range(fps):
        spriteList.append(i)
logo.setName(TextObject(None, 25, (255, 255, 255), "Вы:", 1, logo))

#Resources
currentTextMessage = TextObject(None, 10, (0, 0, 0), "", 1, logo)
isInventory = False

clock = pygame.time.Clock()

#переменные, обеспечивающие смену спрайтов анимации ходьбы
curSprite = 0

#переменные для диалога
isDialogue = 0

#идите просто нахуй(описания)
isText = 0

#костыль (вывод инвенторя)
diary = pygame.image.load("images/icons/diary.png")

#разворачиваю механизм, отвечающий за отслеживание конца песни
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('music/walking.mp3')
pygame.mixer.music.play(0)
isEnd = 0

#библиотекарь
horrorObj = GameObject(430, 234, 590-430, 389-234)
horrorObj.setImage(pygame.image.load("images/npc/horror.png"))

horrorAns = [message(makeTextObjectList(("*крики ужаса*", pygame.font.Font(None, 22), 100), (None, 20, (255, 255, 255), "*крики ужаса*", 1, logo), 0, 1), [0], "крики ужаса"),
message(makeTextObjectList(("...", pygame.font.Font(None, 22), 100), (None, 20, (255, 255, 255), "...", 1, horrorObj), 0, 1), [0], "...")]

horrorQue = [message(makeTextObjectList(("Пх’нглуи мглв’нафх КтулхуР’льех вгах’нагл фхтагн", pygame.font.Font(None, 22), 100), (None, 20, (255, 255, 255), "Пх’нглуи мглв’нафх КтулхуР’льех вгах’нагл фхтагн", 1, horrorObj), 0, 1), [0], "фхтагн"),
message(makeTextObjectList(("Пх’нглуи мглв’нафх КтулхуР’льех вгах’нагл фхтагн", pygame.font.Font(None, 22), 100), (None, 20, (255, 255, 255), "Ты умрешь!", 1, horrorObj), 0, 1), [0], "смерть")]

horror = npc(horrorObj, TextObject(None, 25, (255, 255, 255), "Неописуемый ужас:", 1, horrorObj), horrorQue, horrorAns)
horror.setStartText(horrorQue[0])
horror.setCurrMessage(horrorQue[0])
horror.setCurrAnswer(horrorAns[0])

libraryNpcList = [horror]

background.setNpcList(libraryNpcList)

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == SONG_END or isEnd:
            pygame.mixer.music.play()
            isEnd = 0
            #pygame.mixer.music.queue('music/walking.mp3')

    #задаю координаты гг
    logo.setPosition(x, y)

    #проверяю объекты на предмет столкновения с персонажем
    for i in range(len(background.intersectionObjectsList)):
        if logo.intersects(background.intersectionObjectsList[i], 0):
            if pressed[pygame.K_d]:
                x -= speed
            if pressed[pygame.K_a]:
                x += speed
            if pressed[pygame.K_w]:
                y += speed
            if pressed[pygame.K_s]:
                y -= speed

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

    #отрисовываю npc и проверяю персонажа на столкновение с ними
    for i in range(len(background.npcList)):
        screen.blit(background.npcList[i].npcGameObject.image, (background.npcList[i].npcGameObject.x, background.npcList[i].npcGameObject.y))
        if logo.intersects(background.npcList[i].npcGameObject, 0):
            if pressed[pygame.K_d]:
                x -= speed
            if pressed[pygame.K_a]:
                x += speed
            if pressed[pygame.K_w]:
                y += speed
            if pressed[pygame.K_s]:
                y -= speed

    #реализую перемещение персонажа
    pressed = pygame.key.get_pressed()
    if not pressed[pygame.K_w] and not pressed[pygame.K_s] and not pressed[pygame.K_d] and not pressed[pygame.K_a]:
        screen.blit(character["charStand"], (x, y))
        pygame.mixer.music.stop()
        isEnd = 1
        #pygame.mixer.music.stop()
    else:
        if curSprite + 1 > len(spriteList)-1:
            curSprite = 0
        #pygame.mixer.music.queue("music/walking.mp3")
        #pygame.mixer.music.play()

    if pressed[pygame.K_p]:
        count = 4

    if pressed[pygame.K_w] and pressed[pygame.K_d]:
        x += speed - speed//3
        y -= speed - speed//3
        screen.blit(character["charRight"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_w] and pressed[pygame.K_a]:
        x -= speed - speed//3
        y -= speed - speed//3
        screen.blit(character["charLeft"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_s] and pressed[pygame.K_d]:
        x += speed - speed//3
        y += speed - speed//3
        screen.blit(character["charRight"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_s] and pressed[pygame.K_a]:
        x -= speed - speed//3
        y += speed - speed//3
        screen.blit(character["charLeft"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_w]:
        y -= speed
        screen.blit(character["charBack"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_s]:
        y += speed
        screen.blit(character["charFor"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_d]:
        x += speed
        screen.blit(character["charRight"][spriteList[curSprite]], (x, y))
        curSprite += 1
    elif pressed[pygame.K_a]:
        x -= speed
        screen.blit(character["charLeft"][spriteList[curSprite]], (x, y))
        curSprite += 1

    #реализую диалог с npc
    for i in range(len(background.npcList)):
        if logo.intersects(background.npcList[i].npcGameObject, 10):
            if pressed[pygame.K_e]:
                isDialogue = 1
            elif pressed[pygame.K_ESCAPE]:
                isDialogue = 0
            elif not isDialogue:
                background.npcList[i].ask(logo, screen, pygame.image.load("images/icons/dialogue.png"))

            if isDialogue:
                pygame.draw.rect(screen, (0, 0, 0), (350, 250, 450, 350))
                background.npcList[i].draw(background.npcList[i].currMessage, background.npcList[i].npcGameObject, "npc", screen)
                background.npcList[i].draw(background.npcList[i].currAnswer, logo, "gameObject", screen)
                for j in range(len(background.npcList[i].ansList)):
                    pass

        else:
            isDialogue = 0

    #Проверяю, нажати ли кнопка вызова инвенторя
    if pressed[pygame.K_q]:
        isInventory = True
    if pressed[pygame.K_ESCAPE]:
        isInventory = False

    #Проверяю гг на предмет пересечения с текстовыми зонами, если есть нажатие, вывожу текст на экран
    for i in range(len(background.textObjectsList)):
        if logo.intersects(background.textObjectsList[i].object, 10) and (background.textObjectsList[i].isInter or background.textObjectsList[i].isVisible):
            if pressed[pygame.K_e]:
                if i == 0:
                    isVisible = 1
                background.textObjectsList[i].isVisible = 1
                background.textObjectsList[i].setTrigger(1)
            elif pressed[pygame.K_ESCAPE]:
                background.textObjectsList[i].isVisible = 0
            elif not background.textObjectsList[i].isVisible:
                background.textObjectsList[i].ask(logo, screen, pygame.image.load("images/icons/eye.png"))

            if background.textObjectsList[i].isVisible:
                pygame.draw.rect(screen, (0, 0, 0), (450, 350, 320, 130))
                if i == 0:
                    screen.blit(diary, (100, 100))
                else:
                    background.textObjectsList[i].draw(background.textObjectsList[i].ques, "text", screen)
                print(background.textObjectsList[i].ques[0].string, background.textObjectsList[i].trigger)
                if background.textObjectsList[i].trigger == 1:
                    background.textObjectsList[i].isInter = 0
                    background.textObjectsList[(i+1)%4].isInter = 1

        else:
            background.textObjectsList[i].isVisible = 0
            isVisible = 0

    #вывожу инвентарь на экран
    if isInventory:
        screen.blit(inv.image, (windowSize[0]//2 - inv.width//2, windowSize[1]//2 - inv.height//2))
        for i in range(len(invSlots)):
            if invSlots[i].isFull:
                invSlots[i].drawItem(screen)

    pygame.display.update()
