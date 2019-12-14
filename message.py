"реплики персонажей"
import pygame
from textObject import *
pygame.init()

class message(textObject):
    def __init__(self, textObject, triggerList):
        self.textObject = textObject
        self.triggerList = triggerList
