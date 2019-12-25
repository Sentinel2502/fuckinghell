"npc"
import pygame
pygame.init()
pygame.font.init()

class npc():
    def __init__(self, npcGameObject, name, queList, ansList):
        self.npcGameObject = npcGameObject
        self.name = name
        self.name.font.set_bold(1)
        self.queList = queList
        self.ansList = ansList
        self.npcGameObject.setName(self.name)

    def ask(self, other, surface, image): #, image, pressed, button
        surface.blit(image, (other.x + other.width//2, other.y - image.get_size()[0] - 10))

    def draw(self, message, other, mode, surface):
        if mode == "npc":
            surface.blit(other.name.text, (360, 260))
            surface.blit(message.textObj.text, (360, 280))
        elif mode == "gameObject":
            surface.blit(other.name.text, (360 + 225, 260))
            surface.blit(message.textObj.text, (360 + 225, 280))

    def setStartText(self, textObj):
        self.startText = textObj

    def setCurrMessage(self, currMessage):
        self.currMessage = currMessage

    def setCurrAnswer(self, currAnswer):
        self.currAnswer = currAnswer
