import pygame, sys
from gameObject import *
from locations import *
from information import *
from invSlotObject import *

#Initialize pygame
pygame.init()
pygame.mixer.init()
windowSize = (1024, 768)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

#background
background = locationObjectsList["choice"]

clock = pygame.time.Clock()

#разворачиваю механизм, отвечающий за отслеживание конца песни
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('music/walking.mp3')
pygame.mixer.music.play(0)
isEnd = 0

#Инициализаця текстовых сообщений
nameJohn = TextObject(None, 25, (255, 255, 255), "Джон - 1", 1, 0)
nameJeck = TextObject(None, 25, (255, 255, 255), "Джек - 2", 1, 0)

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == SONG_END or isEnd:
            pygame.mixer.music.play()
            isEnd = 0

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]:
        john.isCh = 1
        break
    if pressed[pygame.K_2]:
        jeck.isCh = 1
        break

    #"рисую на экране" задник
    screen.blit(background.background, (0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (340, 175, 70, 110))
    pygame.draw.rect(screen, (255, 255, 255), (595, 175, 70, 110))
    screen.blit(pygame.image.load("images/characters/john.png"), (345, 180))
    screen.blit(pygame.image.load("images/characters/jeck.png"), (600, 180))
    nameJohn.drawMes(screen, (340, 145))
    nameJeck.drawMes(screen, (600, 145))

    pygame.display.update()
