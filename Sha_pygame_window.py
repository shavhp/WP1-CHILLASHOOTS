import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load('chinchilla_icon_sha.png')
pygame.display.set_icon(icon)

# Player sprite
player_img = pygame.image.load("chinchilla_sprite_sha.png")
player_X_axis = 50
player_Y_axis = 320

# Creates function for player to draw image of sprite icon
def player():
    SCREEN.blit(player_img, (player_X_axis, player_Y_axis))

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
# Gets drawn first
    SCREEN.fill((28, 79, 66))

    player()
    pygame.display.update()