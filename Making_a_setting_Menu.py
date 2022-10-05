# Imports all the available pygame modules into the pygame package
import pygame

# Initialize all imported pygame modules
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (85, 180, 176)
# This Initialize a window or screen for display (How big u want the screen to be)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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


# Define fonts
font = pygame.font.SysFont("arialblack", 40)

# Define colours
TEXT_COL = (255, 255, 255)


# Making a text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    canvas.blit(img, (x, y))


# Game variables
game_paused = False

# Making a game loop. While the The Stopping_game is not True, it keeps going to loop
while not quit_game_requested():

    # Check if game is paused
    if game_paused == True:
        draw_text("Settings", font, TEXT_COL, 160, 250)
        # Display menu
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    # The name that will be displayed on the pygame
    pygame.display.set_caption("Werkplaats 1: PyGame")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
    # This function is used to create a clock object which can be used to keep track of time
    clock = pygame.time.Clock()

    # Allows only a portion of the screen to updated, instead of the entire area
    pygame.display.flip()

# It runs code that deactivates the Pygame library ( kind of the opposite of pygame.init() )
pygame.quit()
