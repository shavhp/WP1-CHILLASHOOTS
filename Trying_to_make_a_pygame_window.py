# Imports all the available pygame modules into the pygame package
import pygame

# Initialize all imported pygame modules
pygame.init()

# Making a variable for the background and screensize
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (0, 0, 0)

# The name that will be displayed on the pygame
pygame.display.set_caption("Werkplaats 1: PyGame")

# This function is used to create a clock object which can be used to keep track of time
clock = pygame.time.Clock()

# This Initialize a window or screen for display (How big u want the screen to be)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Gives u the option to change the background color
canvas.fill(BACKGROUND_COLOR)

# Allows only a portion of the screen to updated, instead of the entire area
pygame.display.flip()

# It runs code that deactivates the Pygame library ( kind of the opposite of pygame.init() )
pygame.quit()
