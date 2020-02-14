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

    screen.blit(pygame.image.load("images/locations/TheEnd.png"), (0, 0))

    pygame.display.update()
