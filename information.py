"""инормация для игры"""

import pygame
from gameObject import *
from locations import *
from textObject import *
from invItemObject import *
from invSlotObject import *

pygame.init()

#данные о персонаже
x, y = 710, 575
speed = 5
character = {"charStand": pygame.image.load("images/characters/charStand.png"),
"charFor": [pygame.image.load("images/characters/charFor1.png"), pygame.image.load("images/characters/charFor2.png")],
"charBack": [pygame.image.load("images/characters/charBack1.png"), pygame.image.load("images/characters/charBack2.png")],
"charLeft": [pygame.image.load("images/characters/charLeft2.png"), pygame.image.load("images/characters/charLeft1.png")],
"charRight": [pygame.image.load("images/characters/charRight1.png"), pygame.image.load("images/characters/charRight2.png")]}
characterSize = character["charStand"].get_size()
logo = GameObject(x, y, characterSize[0], characterSize[1])
fps = 10
spriteAm = 2
spriteList = []
for  i in range(spriteAm):
    for j in range(fps):
        spriteList.append(i)

#cписок локаций
locationObjectsList = {
"bedroom": LocationObject((1024, 768), pygame.image.load("images/locations/bedroom.png")),
"library": LocationObject((1024, 768), pygame.image.load("images/locations/library.png"))}


#СПАЛЬНЯ
bedroomIntersectionObjectsList = [GameObject(13, 550, 280, 204), GameObject(625, 324, 268, 107), GameObject(900, 92, 219, 542-92)]
bedroomTextObjectsList = [TextObject(None, 20, (255, 255, 255), "Куча мусора", 1, bedroomIntersectionObjectsList[0]),
TextObject(None, 20, (255, 255, 255), "Лучше бы гроб здесь поставили :D", 1, bedroomIntersectionObjectsList[1]),
TextObject(None, 20, (255, 255, 255), "Боль, дебаг, страдания", 1, bedroomIntersectionObjectsList[2])]
bedroomExitObjectsList = [[GameObject(264, 153, 109, 223), "library"]]
bedroomItemObjectsList = [InvItemObject(616+11, 464+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(400+11, 464+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1)]

locationObjectsList["bedroom"].setGameField(GameObject(0, 374, 1024, 374))
locationObjectsList["bedroom"].setIntersectionObjectsList(bedroomIntersectionObjectsList)
locationObjectsList["bedroom"].setExitObjectsList(bedroomExitObjectsList)
locationObjectsList["bedroom"].setExitPoint((268, 384))
locationObjectsList["bedroom"].setTextObjectsList(bedroomTextObjectsList)
locationObjectsList["bedroom"].setItemObjectsList(bedroomItemObjectsList)

#персонажи спальни
#horror
horror = GameObject(374, 565, 150, 200)
horror.setImage(pygame.image.load("images/npc/horror.png"))

#БИБЛИОТЕКА
libraryIntersectionObjectsList = [GameObject(164, 459, 383-164, 593-459)]
libraryExitObjectsList = [[GameObject(271, 752, 600, 100), "bedroom"]]
libraryTextObjectsList = [TextObject(None, 20, (255, 255, 255), "Грусть, печаль, тоска", 1, libraryIntersectionObjectsList[0])]
libraryItemObjectsList = [InvItemObject(616+11, 464+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(400+11, 464+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(300+11, 500+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(200+11, 700+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(300+11, 400+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1),
InvItemObject(200+11, 300+4, 19, 35, pygame.image.load("images/objects/candle.png"), 1)]

locationObjectsList["library"].setGameField(GameObject(60, 400, 905, 367))
locationObjectsList["library"].setIntersectionObjectsList(libraryIntersectionObjectsList)
locationObjectsList["library"].setExitObjectsList(libraryExitObjectsList)
locationObjectsList["library"].setExitPoint((700, 500))
locationObjectsList["library"].setTextObjectsList(libraryTextObjectsList)
locationObjectsList["library"].setItemObjectsList(libraryItemObjectsList)

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
