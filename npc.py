"npc"
import pygame
pygame.init()

class npc():
    def __init__(self, npcGameObject, name, queList, ansList):
        self.npcGameObject = npcGameObject
        self.name = name
        self.queList = queList
        self.ansList = ansList
        self.npcGameObject.setName(self.name)

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def draw(self, message, other, mode, surface):
        if mode == "npc":
            surface.blit(other.name.text, (other.x, other.y - 50))
            surface.blit(message.textObj.text, (other.x, other.y - 20))
        elif mode == "gameObject":
            surface.blit(other.name.text, (other.x, other.y - 50))
            surface.blit(message.textObj.text, (other.x, other.y - 20))

    def setStartText(self, textObj):
        self.startText = textObj

    def setCurrMessage(self, currMessage):
        self.currMessage = currMessage

    def setCurrAnswer(self, currAnswer):
        self.currAnswer = currAnswer
