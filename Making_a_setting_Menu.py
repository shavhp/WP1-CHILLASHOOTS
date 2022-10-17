# Imports all the available pygame modules into the pygame package
import pygame

# Initialize all imported pygame modules
pygame.init()

# The name that will be displayed on the pygame
pygame.display.set_caption("Werkplaats 1: PyGame")

# Show background image
BACKGROUND = pygame.image.load('images/background-galaxy.jpg')
Setting_text = pygame.image.load('images/Puple_settings.png')
Credits_text = pygame.image.load('images/Credits.png')
Controls_text = pygame.image.load('images/Controls.png')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# This Initialize a window or screen for display (How big u want the screen to be)
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def quit_game_requested():
    stopping_game = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        # if i press ESC-button then the program will close.
        if event.type == pygame.QUIT:
            stopping_game = True
            break
    return stopping_game


# Define fonts
font = pygame.font.SysFont("arialblack", 20)

# Define colours
TEXT_COL = (255, 255, 255)


# Making a text function
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    canvas.blit(img, (x, y))


class Button1():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()


# Game variables
game_paused = False
# Making a game loop. While the The Stopping_game is not True, it keeps going to loop
while not quit_game_requested():
    # Check if game is paused
    if game_paused == True:
        canvas.blit(BACKGROUND, (0, 0))
        color_popup = (75, 0, 130)
        color = (0, 0, 0)
        color_white = (0.2, 0.4, 0.6)
        pygame.draw.rect(canvas, color_white, pygame.Rect(50, 200, 700, 350), 0, 7)
        pygame.draw.rect(canvas, color, pygame.Rect(94, 80, 143, 71), 0, 7)
        pygame.draw.rect(canvas, color, pygame.Rect(344, 80, 151, 71), 0, 7)
        pygame.draw.rect(canvas, color, pygame.Rect(594, 80, 129, 71), 0, 7)
        canvas.blit(Setting_text, (100, 80))
        canvas.blit(Controls_text, (350, 80))
        canvas.blit(Credits_text, (600, 80))
        # Display menu
    else:
        canvas.blit(BACKGROUND, (0, 0))
        draw_text("Press SPACE to continue", font, TEXT_COL, 290, 250)

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
