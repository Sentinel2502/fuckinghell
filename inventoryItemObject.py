"""Реализует объект, который можно взять и поместить в инвентарь"""

class inventoryItemObject(GameObject):
    def __init__(self, x, y, width, height, isTaken):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isTaken = isTaken

    def Take(self):
        self.isTaken = True
    def Discard(self):
        self.isTaken = False

    def putInInventory(self, inventorySlot):
