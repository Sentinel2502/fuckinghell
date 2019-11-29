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

    def intersectsY(self, other):
        if self.y >= other.y and self.y <= (other.y + other.height - self.height):
            return 1
        if (self.y + self.height) >= other.y and self.y + self.height <= (other.y + other.height - self.height):
            return 1
        return 0

    def intersectsX(self, other):
        if self.x >= other.x and self.x <= other.x + other.width:
            return 1
        if (self.x + self.width) > other.x and (self.x + self.width) <= (other.x + other.width):
            return 1
        return 0

    def intersects(self, other):
        if self.intersectsX(other) and self.intersectsY(other):
            return 1
        return 0
    def moveIfIntersects(self, other, coordinates, pressed):
        x = coordinates[0]
        y = coordinates[1]
        """if self.intersectsY(other) and y > other.y:
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
                x -= 5"""

        return x, y
