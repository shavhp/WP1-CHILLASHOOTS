import pygame
import math
pygame.init()

clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving background")
chilla = pygame.image.load("images/chinchilla_sprite_sha.png").convert()
bg = pygame.image.load("images/bg.png").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width + 1)
print(tiles)

pygame.quit()
