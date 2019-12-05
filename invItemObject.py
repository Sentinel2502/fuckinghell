"""Реализует объект, который можно взять и поместить в инвентарь"""

from gameObject import *

class InvItemObject(GameObject):
    def __init__(self, x, y, width, height, image, isVisible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isVisible = isVisible
        self.image = image

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def draw(self, other, surface):
        if self.isVisible:
            surface.blit(self.text, (other.x + other.width//2, other.y - other.width - 10))
        else:
            pass

    def setIsVisible(self, isVisible):
        self.isVisible = isVisible
