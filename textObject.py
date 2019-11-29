"""Реализует окошки с текстом"""

import pygame
from gameObject import *
pygame.init()

class TextObject(GameObject):
    def __init__(self, fontName, fontSize, color, text, smoothing, object):
        self.font = pygame.font.Font(fontName, fontSize)
        self.text = self.font.render(text, smoothing, color)
        self.object = object

    def draw(self, other, surface, image):
        surface.blit(self.text, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def ask(self, other, surface, image, pressed): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))
        if pressed[pygame.K_e]:
            self.draw(other, surface, image)
