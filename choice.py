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
        Jhon = 1
        Jeck = 0
        break
    if pressed[pygame.K_2]:
        Jeck = 1
        Jhon = 0
        break

    #"рисую на экране" задник
    screen.blit(background.background, (0, 0))

    pygame.display.update()
