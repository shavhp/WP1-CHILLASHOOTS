# Importing and initializing PyGame resources and a randomizer module
import pygame
from enemy import *

pygame.init()

# Screen, background and canvas variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# The color order is: Red, Green, and Blue. The max values are 255
BACKGROUND_COLOR = (0, 0, 255)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# This sets the window bar text and logo
pygame.display.set_caption("Test enemy")
icon = pygame.image.load("../images/chinchilla_icon_sha.png")
pygame.display.set_icon(icon)

# Clock and speed
GAME_SPEED = 60
clock = pygame.time.Clock()


# The game looping until the program is exited
def quit_game_requested():
    # Boolean variable determining if the program may keep running
    halting = False
    for event in pygame.event.get():
        # If the user quits the game, the "halting" variable boolean gets set to "True" and the program quits
        if event.type == pygame.QUIT:
            halting = True
            break
        # Event checking if you press a certain key
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # if the user presses the Escape key, it quits the program like the "QUIT" event above
            halting = True
            break

    # Loops back to the "halting" variable
    return halting


# Defining enemies
enemytest = DummyEnemy()
line_enemy = Line()
enemy = Bouncer()

# Create a window while the previous function is still running
while not quit_game_requested():
    # The canvas gets filled with whatever the background color is (currently blue)
    canvas.fill(BACKGROUND_COLOR)

    # Draw the enemies, it will be random each time the application starts
    enemytest.update(canvas)
    line_enemy.update(canvas)
    enemy.update(canvas)


    # Despite what the "flip" part suggests, it's not actually flipping the display
    # It is to actually update the display to display the items we want to draw on screen
    # Items that are drawn must be before this command in order to show up on the display
    pygame.display.flip()

    # Clock ticking to the game speed
    clock.tick(GAME_SPEED)

# When the program quits, this text will be printed before termination
print("Program Terminated")
