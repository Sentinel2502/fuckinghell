"""Реализует окошки с текстом"""

import pygame
from gameObject import *
pygame.init()

class TextObject(GameObject):
    def __init__(self, fontName, fontSize, color, text, smoothing, object):
        self.font = pygame.font.Font(fontName, fontSize)
        self.text = self.font.render(text, smoothing, color)
        self.object = object
        self.message = text

    def setIsVisible(self, isVisible):
        self.isVisible = isVisible

    def draw(self, other, surface):
        if self.isVisible:
            surface.blit(self.text, (other.x + other.width//2, other.y - other.width - 10))
        else:
            pass

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))
