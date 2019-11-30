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

    def intersectsY(self, other, margin):
        y = other.y
        height = other.height
        y -= margin
        height += 2*margin
        if self.y >= y and self.y <= (y + height - self.height):
            return 1
        if (self.y + self.height) >= y and self.y + self.height <= (y + height - self.height):
            return 1
        return 0

    def intersectsX(self, other, margin):
        x = other.x
        width = other.width
        width += 2*margin
        x -= margin
        if self.x >= x and self.x <= x + width:
            return 1
        if (self.x + self.width) > x and (self.x + self.width) <= (x + width):
            return 1
        return 0

    def intersects(self, other, margin):
        if self.intersectsX(other, margin) and self.intersectsY(other, margin):
            return 1
        return 0
    """def moveIfIntersects(self, other, coordinates, pressed):
        x = coordinates[0]
        y = coordinates[1]
        if self.intersectsY(other) and y > other.y:
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 0
            if pressed[pygame.K_RIGHT]:
                x += 5
            if pressed[pygame.K_LEFT]:
                x -= 5
        if self.intersectsY(other) and y < other.y:
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 0
            if pressed[pygame.K_RIGHT]:
                x += 5
            if pressed[pygame.K_LEFT]:
                x -= 5
        if self.intersectsX(other) and x > other.x and (y + self.height >= other.y and y <= other.y + other.height):
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 5
            if pressed[pygame.K_RIGHT]:
                x += 5
            if pressed[pygame.K_LEFT]:
                x -= 0
        elif self.intersectsX(other) and x < other.x and (y + self.height >= other.y and y <= other.y + other.height):
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 5
            if pressed[pygame.K_RIGHT]:
                x += 0
            if pressed[pygame.K_LEFT]:
                x -= 5
        else:
            if pressed[pygame.K_UP]:
                y -= 5
            if pressed[pygame.K_DOWN]:
                y += 5
            if pressed[pygame.K_RIGHT]:
                x += 5
            if pressed[pygame.K_LEFT]:
                x -= 5

        return x, y"""
