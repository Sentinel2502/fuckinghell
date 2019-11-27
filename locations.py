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

    def checkIfOutBoundary(self, character, coordinates): #проверяет, находится ли персонаж в границах экрана (character - спрайт персонажа)
        self.coordinates = coordinates
        self.x = self.coordinates[0]
        self.y = self.coordinates[1]
        self.character = character
        characterSize = self.character.get_size()
        if self.x + characterSize[0] > self.width:
            self.x = self.width - characterSize[0]

        if self.y + characterSize[1] > self.height:
            self.y = self.height - characterSize[1]

        if self.y <= 0:
            self.y = 0
        if self.x <= 0:
            self.x = 0

        return self.x, self.y
