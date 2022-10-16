import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load(os.path.join('../images', 'chinchilla_icon_sha.png'))
pygame.display.set_icon(icon)