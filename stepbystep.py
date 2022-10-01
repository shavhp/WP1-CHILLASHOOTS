# Importing and initializing PyGame resources and a randomizer module
import pygame
import random
pygame.init()

# Screen, background and canvas variables
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# The color order is: Red, Green, and Blue. The max values are 255
BACKGROUND_COLOR = (0, 0, 255)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# This sets the window bar text
pygame.display.set_caption("Test with randomizer")

# Test rectangle position variable, now randomized on each run
obj_x = random.randint(100, 900)
obj_y = random.randint(100, 600)

# Test rectangle size variable, now randomized too
obj_width = random.randint(100, 900)
obj_height = random.randint(100, 600)


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
        elif event.type == pygame.KEYDOWN:
            # if the user presses the Escape key, it quits the program like the "QUIT" event above
            event.key = pygame.K_ESCAPE
            halting = True
            break

    # Loops back to the "halting" variable
    return halting


# Create a window while the previous function is still running
while not quit_game_requested():
    # The canvas gets filled with whatever the background color is (currently blue)
    canvas.fill(BACKGROUND_COLOR)

    # Draw a object
    pygame.draw.rect(canvas, (255, 255, 0), (obj_x, obj_y, obj_width, obj_height))

    # Despite what the "flip" part suggests, it's not actually flipping the display
    # It is to actually update the display to have a (currently blue) background
    # Items that are drawn must be before this command in order to show up on the display
    pygame.display.flip()


# When the program quits, this text will be printed before termination
print("Program Terminated")
