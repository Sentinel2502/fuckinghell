from itertools import chain
import pygame
pygame.init()
from textObject import *

def truncline(text, font, maxwidth):
        real=len(text)
        stext=text
        l=font.size(text)[0]
        cut=0
        a=0
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)
            done=0
        return real, done, stext

def wrapline(text, font, maxwidth):
    done=0
    wrapped=[]

    while not done:
        nl, done, stext=truncline(text, font, maxwidth)
        wrapped.append(stext.strip())
        text=text[nl:]
        print("wrapping")
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)

class makeTextObjectList(TextObject):
#(text, font, maxwidth), (fontName, fontSize, color, text, smoothing, object)
    def __init__(self, wrapline_args, textObjects_args, isVisible, isInter, justInter=0):
        dtext = wrapline_args[0]
        font = wrapline_args[1]
        maxwidth = wrapline_args[2]
        fontName = textObjects_args[0]
        fontSize = textObjects_args[1]
        color = textObjects_args[2]
        text = textObjects_args[3]
        smoothing = 1
        self.object = textObjects_args[5]
        self.isInter = isInter
        self.answerList = []
        self.triggerList = []
        self.trigger = 0

        ques = []

        wrapped = wrapline(text, font, maxwidth)

        for i in range(len(wrapped)):
            ques.append(TextObject(fontName, fontSize, color, wrapped[i], smoothing, object))

        self.ques = ques

    def setTrigger(self, value):
        self.trigger = value

    def setAnswerList(self, answerList):
        self.answerList = answerList
