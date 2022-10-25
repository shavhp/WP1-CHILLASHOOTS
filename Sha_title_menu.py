# Imports pygame module
import pygame

import os

# Initializes pygame library
pygame.init()

# Create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Show background image
BACKGROUND = CANVAS.fill((0, 0, 0))

# Font and color of title
TITLE_FONT = pygame.font.Font(os.path.join('fonts', 'gametitle_04B_30__.ttf'), 60)
TITLE_COLOR_1 = (255, 0, 0)
TITLE_COLOR_2 = (255, 0, 0)

# Create text surface object
TITLE_1 = TITLE_FONT.render('GAME', True, TITLE_COLOR_1, None)
TITLE_2 = TITLE_FONT.render('OVER!!', True, TITLE_COLOR_2, None)

# Create rectangular object for text surface object
TITLE_RECT_1 = TITLE_1.get_rect()
TITLE_RECT_2 = TITLE_2.get_rect()

# Set center of rectangular object
TITLE_RECT_1.center = (SCREEN_WIDTH // 3.09, SCREEN_HEIGHT // 3)
TITLE_RECT_2.center = (SCREEN_WIDTH // 1.39, SCREEN_HEIGHT // 3)

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load(os.path.join('images', 'chinchilla_icon_sha.png'))
pygame.display.set_icon(icon)

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(TITLE_1, TITLE_RECT_1)
    CANVAS.blit(TITLE_2, TITLE_RECT_2)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

