"""Реализует окошки с текстом"""

import pygame
from gameObject import *
pygame.init()
pygame.font.init()

class TextObject(GameObject):
    def __init__(self, fontName, fontSize, color, text, smoothing, object, isInter=True):
        self.string = text
        self.fontSize = fontSize
        self.font = pygame.font.Font(fontName, fontSize)
        self.text = self.font.render(text, smoothing, color)
        self.object = object
        self.message = text
        self.triggerList = {}
        self.isInter = isInter

    def setIsVisible(self, isVisible):
        self.isVisible = isVisible

    def draw(self, message, other, surface):
        nx = 460
        ny = 360
        list = message

        for i in range(len(list)):
            surface.blit(list[i].text, (nx, ny))
            ny += 20

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def isInter(self, bool):
        self.isInter = bool

    def addTrigger(self, triggerName, bool):
        triggerList[triggerName] = bool
