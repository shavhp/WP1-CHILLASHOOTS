# Importing and initializing PyGame resources
import pygame
pygame.init()

# Screen, background and canvas variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# The color order is: Red, Green, and Blue. The max values are 255
BACKGROUND_COLOR = (0, 0, 255)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# This sets the window bar text
pygame.display.set_caption("Test")


def quit_game_requested():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting


while not quit_game_requested():
    # The canvas gets filled with whatever the background color is (currently blue)
    canvas.fill(BACKGROUND_COLOR)
    pygame.display.flip()

print("Exit")
