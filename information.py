"""инормация для игры"""

import pygame
from gameObject import *
from locations import *
from invItemObject import *
from invSlotObject import *
from message import *
from npc import *
from wrapline import *
from trigger import *

pygame.init()
pygame.font.init()

#Инициализаця персонажей
#Aлиса
x, y = 0, 0
Aspeed = 5
Acharacter = {"charStand": pygame.image.load("images/characters/charStand.png"),
"charFor": [pygame.image.load("images/characters/charFor1.png"), pygame.image.load("images/characters/charFor2.png"), pygame.image.load("images/characters/charFor3.png"), pygame.image.load("images/characters/charFor4.png"), pygame.image.load("images/characters/charFor5.png"), pygame.image.load("images/characters/charFor6.png")],
"charBack": [pygame.image.load("images/characters/charBack1.png"), pygame.image.load("images/characters/charBack2.png"), pygame.image.load("images/characters/charBack3.png"), pygame.image.load("images/characters/charBack4.png"), pygame.image.load("images/characters/charBack5.png"), pygame.image.load("images/characters/charBack6.png")],
"charLeft": [pygame.image.load("images/characters/charLeft1.png"), pygame.image.load("images/characters/charLeft2.png"), pygame.image.load("images/characters/charLeft3.png"), pygame.image.load("images/characters/charLeft1.png"), pygame.image.load("images/characters/charLeft2.png"), pygame.image.load("images/characters/charLeft3.png")],
"charRight": [pygame.image.load("images/characters/charRight1.png"), pygame.image.load("images/characters/charRight2.png"), pygame.image.load("images/characters/charRight3.png"), pygame.image.load("images/characters/charRight1.png"), pygame.image.load("images/characters/charRight2.png"), pygame.image.load("images/characters/charRight3.png")]}
AcharacterSize = Acharacter["charStand"].get_size()
alice = GameObject(x, y, AcharacterSize[0], AcharacterSize[1])
fps = 6
spriteAm = 6
AspriteList = []
for i in range(spriteAm):
    for j in range(fps):
        AspriteList.append(i)
alice.setName(TextObject(None, 25, (255, 255, 255), "Вы:", 1, alice))

#Джон
x, y = 0, 0
Jospeed = 5
Jocharacter = {"charStand": pygame.image.load("images/characters/john.png"),
"charFor": [pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png")],
"charBack": [pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png")],
"charLeft": [pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png")],
"charRight": [pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png"), pygame.image.load("images/characters/john.png")]}
JocharacterSize = Jocharacter["charStand"].get_size()
john = GameObject(x, y, JocharacterSize[0], JocharacterSize[1])
fps = 8
spriteAm = 3
JospriteList = []
for  i in range(spriteAm):
    for j in range(fps):
        JospriteList.append(i)
john.setName(TextObject(None, 25, (255, 255, 255), "Вы:", 1, john))

#Джек
x, y = 0, 0
Jespeed = 5
Jecharacter = {"charStand": pygame.image.load("images/characters/jeck.png"),
"charFor": [pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png")],
"charBack": [pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png")],
"charLeft": [pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png")],
"charRight": [pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png"), pygame.image.load("images/characters/jeck.png")]}
JecharacterSize = Jecharacter["charStand"].get_size()
jeck = GameObject(x, y, JecharacterSize[0], JecharacterSize[1])
fps = 8
spriteAm = 3
JespriteList = []
for  i in range(spriteAm):
    for j in range(fps):
        JespriteList.append(i)
jeck.setName(TextObject(None, 25, (255, 255, 255), "Вы:", 1, jeck))

#cписок локаций
locationObjectsList = {
"bedroom": LocationObject((1024, 768), pygame.image.load("images/locations/bedroom.png")),
"library": LocationObject((1024, 768), pygame.image.load("images/locations/library.png")),
"choice": LocationObject((1024, 768), pygame.image.load("images/locations/choice.png"))}


#СПАЛЬНЯ

bedroomNpcList = []
bedroomIntersectionObjectsList = [GameObject(13, 550, 280, 204), GameObject(625, 324, 268, 107), GameObject(900, 92, 219, 542-92),
GameObject(332, 467, 571-332, 657-467), GameObject(472, 654, 526-472, 706-654), GameObject(17, 396, 139-17, 535-396),
GameObject(0, 0, 1023, 378), GameObject(904, 649, 997-904, 728-649), GameObject(409, 344, 591-409, 408-344), GameObject(631, 431, 673-631, 449-431),
GameObject(797, 440, 889-797, 482-440)]
#fontName, fontSize, color, text, smoothing, object, isInter=True
#(text, font, maxwidth),                                          (fontName, fontSize, color, text, smoothing, object)
bedroomTextObjectsList = [makeTextObjectList(("Рюкзак с дерьмом (с матешей)", pygame.font.Font(None, 25), 200), (None, 25, (255, 255, 255), "Рюкзак с дерьмом (с матешей)", 0, GameObject(616, 408, 672-616, 468-408)), 0, 1, 1),
makeTextObjectList(("Видимо, бессонная ночь не стоит и четверки за сочинение. Отлично! Один прокол и получай три в году.", pygame.font.Font(None, 25), 300), (None, 25, (255, 255, 255), "Видимо, бессонная ночь не стоит и четверки за сочинение. Отлично! Один прокол и получай три в году.", 0, GameObject(726, 433, 779-706, 516-433)), 0, 0),
makeTextObjectList(("Лучшая подруга. Лучая во всем, даже сочинение списала на отлично, пока я готовила его ночь", pygame.font.Font(None, 25), 200), (None, 25, (255, 255, 255), "Лучшая подруга. Лучая во всем, даже сочинение списала на отлично, пока я готовила его ночь", 0, GameObject(332, 504, 388-332, 658-504)), 0, 0),
makeTextObjectList(("", pygame.font.Font(None, 25), 200), (None, 25, (255, 255, 255), "", 0, GameObject(625, 324, 894-625, 431-324)), 0, 0, 1)]
diary = pygame.image.load("images/icons/diary.png")
isVisible = 0
bedroomTextObjectsList[0].setTrigger(0)
bedroomTextObjectsList[1].setTrigger(0)
bedroomTextObjectsList[2].setTrigger(0)
bedroomTextObjectsList[3].setTrigger(0)
bedroomExitObjectsList = []
bedroomItemObjectsList = []

locationObjectsList["bedroom"].setGameField(GameObject(0, 374, 1024, 374))
locationObjectsList["bedroom"].setIntersectionObjectsList(bedroomIntersectionObjectsList)
locationObjectsList["bedroom"].setExitObjectsList(bedroomExitObjectsList)
locationObjectsList["bedroom"].setExitPoint((200, 300))
locationObjectsList["bedroom"].setTextObjectsList(bedroomTextObjectsList)
locationObjectsList["bedroom"].setItemObjectsList(bedroomItemObjectsList)
locationObjectsList["bedroom"].setNpcList(bedroomNpcList)

#БИБЛИОТЕКА
libraryTextObjectsList = [makeTextObjectList(("Старое, но уютное кресло. Хочу ли я отдохнуть?", pygame.font.Font(None, 25), 200), (None, 25, (255, 255, 255), "Старое, но уютное кресло. Хочу ли я отдохнуть?", 0, GameObject(803, 571, 889-803, 685)), 0, 1)]

locationObjectsList["library"].setGameField((0, 0, 1024, 768))
locationObjectsList["library"].setIntersectionObjectsList([])
locationObjectsList["library"].setExitObjectsList([])
locationObjectsList["library"].setExitPoint((484, 639))
locationObjectsList["library"].setTextObjectsList(libraryTextObjectsList)
locationObjectsList["library"].setItemObjectsList([])
locationObjectsList["library"].setNpcList([])

#Экран выбора персонажа

#ИНВЕНТАРЬ
inv = GameObject(1024, 768, 272, 384)
inv.setImage(pygame.image.load("images/icons/inventory.png"))
invSlots = [
InvSlotObject(19 + inv.x//2 - inv.width//2, 32 + inv.y//2 - inv.height//2, 231, 164),
InvSlotObject(17 + inv.x//2 - inv.width//2, 235 + inv.y//2 - inv.height//2, 62, 54),
InvSlotObject(102 + inv.x//2 - inv.width//2, 235 + inv.y//2 - inv.height//2, 62, 54),
InvSlotObject(187 + inv.x//2 - inv.width//2, 235 + inv.y//2 - inv.height//2, 62, 54),
InvSlotObject(17 + inv.x//2 - inv.width//2, 304 + inv.y//2 - inv.height//2, 62, 54),
InvSlotObject(102 + inv.x//2 - inv.width//2, 304 + inv.y//2 - inv.height//2, 62, 54),
InvSlotObject(187 + inv.x//2 - inv.width//2, 304 + inv.y//2 - inv.height//2, 62, 54)]
