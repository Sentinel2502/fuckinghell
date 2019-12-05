"""Реализует объект, который можно взять и поместить в инвентарь"""

from gameObject import *

class InvItemObject(GameObject):
    def __init__(self, x, y, width, height, image, isTaken):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isTaken = isTaken
        self.image = image

    def Take(self):
        self.isTaken = True
    def Discard(self):
        self.isTaken = False

    def putInInventory(self, inventorySlot):
        pass
