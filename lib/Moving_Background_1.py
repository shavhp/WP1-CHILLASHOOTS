import math
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 144
bg = pygame.image.load("../images/bg_stars_game.png").convert()
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width + 1)
