""" Реализуется проверка персонажа на нахождение внутри обозначенных границ локации
    Реализуется переключение между локациями
    Реализуются подключение объектов коллизии к локациям"""
import pygame
from gameObject import *


class LocationObject:
    def __init__(self, resolution, background):
        self.resolution = resolution
        self.width = resolution[0]
        self.height = resolution[1]
        self.background = background #фоновое изображение

    def setExitPoint(self, coordinates):
        self.exit_x = coordinates[0]
        self.exit_y = coordinates[1]

    def scaleBackground(self, resolution): #изменяет размер фонового изображения
        self.background = pygame.transform.scale(self.background, resolution)

    def setGameField(self, gameFieldObject): #задает прямоугольник, в котором может двигаться персонаж
        self.gameFieldObject = gameFieldObject

    def setIntersectionObjectsList(self, intersectionObjectsList): #задает список объектов, с кот. может пересечься персонаж
        self.intersectionObjectsList = intersectionObjectsList

    def setExitObjectsList(self, exitObjectsList): #задает список объектов при соприкосновении с кот., игрок переходит на другую локацию
        self.exitObjectsList = exitObjectsList

    def setTextObjectsList(self, textObjectsList):
        self.textObjectsList = textObjectsList

    def checkIfOutBoundary(self, character, coordinates): #проверяет, находится ли персонаж в границах экрана (character - спрайт персонажа)
        x = coordinates[0]
        y = coordinates[1]
        character = character
        characterSize = character.get_size()
        if x + characterSize[0] > self.width:
            x = self.width - characterSize[0]

        if y + characterSize[1] > self.height:
            y = self.height - characterSize[1]

        if y <= 0:
            y = 0
        if x <= 0:
            x = 0

        return x, y
