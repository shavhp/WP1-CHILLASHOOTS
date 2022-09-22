import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN_SIZE = pygame.display.set_mode((1024, 768))

# Title and Icon
# Reminder to attribute creator of icon in credit section of game
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load('chinchilla_icon_sha.png')
pygame.display.set_icon(icon)

# Main event loop
# This loop contains everything that has to stay consistent, infinitely
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            event.key = pygame.K_ESCAPE
            running = False

        elif event.type == pygame.QUIT:
            running = False
# Adds background color to screen
    SCREEN_SIZE.fill((28, 79, 66))
    pygame.display.update()