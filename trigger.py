"Реализует триггеры"
import pygame
pygame.init()

class trigger():
    def __init__(self, passiveTriggerList, value, triggerName):
        self.passiveTriggerList = passiveTriggerList
        self.value = value

    def changePassiveTrigger(self, passiveTrigger, value):
        passiveTrigger = value

    def addPassiveTrigger(self, triggerName, passiveTrigger):
        self.passiveTriggerList[triggerName] = passiveTrigger
