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
#pygame.mixer.init()

#загружаю базовые звуки (универсальные для всех локаций)
#pygame.mixer.music.load('music/walking.mp3')

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
#библиотекарь
#<<<

#<<<

locationObjectsList["library"].setGameField((0, 0, 1024, 768))
locationObjectsList["library"].setIntersectionObjectsList([])
locationObjectsList["library"].setExitObjectsList([])
locationObjectsList["library"].setExitPoint((484, 639))
locationObjectsList["library"].setTextObjectsList([])
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
