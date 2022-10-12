import pygame
import math
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
chilla = pygame.image.load("images/chinchilla_sprite_sha.png").convert()
bg = pygame.image.load("images/Pic_1.jpg").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width + 1)
print(tiles)
