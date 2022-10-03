# Imports all the available pygame modules into the pygame package
import pygame

# Initialize all imported pygame modules
pygame.init()


# Defining a function (Make a variable false, if u)
def quit_game_requested():
    stopping_game = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # if i press ESC-button then the program will close.
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            stopping_game = True
            break
    return stopping_game

# Making a text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    canvas.blit(img, (x, y))


# Making a game loop. While the The Stopping_game is not True, it keeps going to loop
while not quit_game_requested():
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
