"""Реализует ячейку инвенторя"""

from gameObject import *
import pygame

pygame.init()

class InvSlotObject(GameObject):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isFull = 0

    def setIsFull(self, isFull):
        self.isFull = isFull

    def setItem(self, item):
        self.item = item

    def drawItem(self, screen):
        w, h = self.item.image.get_size()
        a = self.x + self.width//2
        b = self.y + self.height//2
        x = a - w//2
        y = b - h//2
        screen.blit(self.item.image, (x, y))
