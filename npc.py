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
            nx = 360
            ny = 260
            sx = 360
            sy = 280
            list = self.currMessage.textObjList.ques
        elif mode == "gameObject":
            nx = 360 + 225
            ny = 260
            sx = 360 + 225
            sy = 280
            list = self.currAnswer.textObjList.ques

        surface.blit(other.name.text, (nx, ny))

        for i in range(len(list)):
            surface.blit(list[i].text, (sx, sy))
            sy += 20


    def setStartText(self, textObj):
        self.startText = textObj

    def setCurrMessage(self, currMessage):
        self.currMessage = currMessage

    def setCurrAnswer(self, currAnswer):
        self.currAnswer = currAnswer
