"реплики персонажей"
import pygame
from textObject import *
pygame.init()

class message(TextObject):
    def __init__(self, textObj, triggerList, id):
        self.textObj = textObj
        self.triggerList = triggerList
        self.id = id

    def setOtherMessageList(self, otherMessageList):
        self.otherMessageList = otherMessageList
