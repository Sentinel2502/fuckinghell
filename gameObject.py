"Реализует коллизию с объектами"

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
