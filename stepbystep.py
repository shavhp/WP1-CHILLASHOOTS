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


# Create a lasting window while the previous function is still running
while not quit_game_requested():
    # The canvas gets filled with whatever the background color is (currently blue)
    canvas.fill(BACKGROUND_COLOR)

    # Despite what the "flip" part suggests, it's not actually flipping the display
    # It is to actually update the display to have a (currently blue) background
    pygame.display.flip()


# When the program quits, this text will be printed before termination
print("Exit")
