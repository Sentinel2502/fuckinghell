"Реализует коллизию с объектами"
import pygame
pygame.init()


class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setImage(self, image):
        self.image = image

    def setName(self, name):
        self.name = name

    def intersectsY(self, other, margin):
        y = other.y
        height = other.height
        y -= margin
        height += 2*margin

        if self.y + self.height >= y and self.y + self.height <= y + height:
            return 1
        return 0

    def intersectsX(self, other, margin):
        x = other.x
        width = other.width
        width += 2*margin
        x -= margin

        if self.x + self.width >= x and self.x <= x + width:
            return 1
        return 0

    def intersects(self, other, margin):
        if self.intersectsY(other, margin) and self.intersectsX(other, margin):
            return 1
        return 0


    """def intersectsY(self, other, margin):
        y = other.y
        height = other.height
        y -= margin
        height += 2*margin
        if self.y >= y and self.y <= (y + height - self.height):
            return 1
        if (self.y + self.height) >= y and (self.y + self.height) <= (y + height - self.height):
            return 1
        return 0

    def intersectsX(self, other, margin):
        x = other.x
        width = other.width
        width += 2*margin
        x -= margin
        if self.x >= x and self.x <= x + width:
            return 1
        if (self.x + self.width) >= x and (self.x + self.width) <= (x + width):
            return 1
        return 0

    def intersects(self, other, margin):
        if self.intersectsX(other, margin) and self.intersectsY(other, margin):
            return 1
        return 0"""
