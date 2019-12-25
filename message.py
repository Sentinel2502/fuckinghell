"реплики персонажей"
import pygame
from textObject import *
pygame.init()

class message(TextObject):
    def __init__(self, textObjList, triggerList, id):
        self.textObjList = textObjList
        self.triggerList = triggerList
        self.id = id

    def setOtherMessageList(self, otherMessageList):
        self.otherMessageList = otherMessageList
