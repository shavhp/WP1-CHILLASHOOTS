# Imports pygame module
import pygame

# Initializes pygame library
pygame.init()

# Create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Show background image
BACKGROUND = pygame.image.load('images/background-galaxy.jpg')

# Font and color of title
TITLE_FONT = pygame.font.SysFont('bauhaus93', 90)
TITLE_COLOR = (255, 255, 255)
# elephant.ttf, extra.ttf,

# Create text surface object
TITLE = TITLE_FONT.render('CHILLASHOOTS', True, TITLE_COLOR, None)

# Create rectangular object for text surface object
TITLE_RECT = TITLE.get_rect()

# Set center of rectangular object
TITLE_RECT.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load('chinchilla_icon_sha.png')
pygame.display.set_icon(icon)

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(TITLE, TITLE_RECT)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
