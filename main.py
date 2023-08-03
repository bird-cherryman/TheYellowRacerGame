import random
import pygame
import os

from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT
pygame.init()

WIDHT = 1000
HEIGHT = 600
FONT = pygame.font.SysFont('Verdana', 20)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

FPS = pygame.time.Clock()

main_display = pygame.display.set_mode((WIDHT, HEIGHT))
player = pygame.image.load('car-1.png').convert_alpha() 
player_rect = pygame.Rect(0, 0, *player.get_size())

score = 0

playing = True
while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False


    main_display.blit(FONT.render(str(score), True, COLOR_WHITE), (WIDHT-50,20))
    main_display.blit(player, player_rect)

    pygame.display.flip()
