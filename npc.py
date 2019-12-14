"npc"
import pygame
pygame.init()

class npc():
    def __init__(self, npcGameObject, name, queList, ansList):
        self.npcGameObject = npcGameObject
        self.name = name
        self.queList = queList
        self.ansList = ansList

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def draw(self, message, other, surface):
        other = self.npcGameObject
        surface.blit(self.name.text, (other.x + other.width//2, other.y - other.width - 30))
        surface.blit(message.textObj.text, (other.x + other.width//2, other.y - other.width - 10))

    def setStartText(self, textObj):
        self.startText = textObj

    def setCurr(self, currMessage):
        self.currMessage = currMessage
