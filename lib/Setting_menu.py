
from lib.Game_Over import *

def setting_page():
    # Font and color of title
    TITLE_FONT = pygame.font.Font('../fonts/gametitle_04B_30__.ttf', 60)
    GREY = (200, 200, 200)
    BLACK = (0, 0, 0)

    # Create text surface object
    TITLE_1 = TITLE_FONT.render('Setting', True, GREY, None)


    # Create rectangular object for text surface object
    TITLE_RECT_1 = TITLE_1.get_rect()

    # Set center of rectangular object
    TITLE_RECT_1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

    # Title and Icon
    pygame.display.set_caption("ChillaShoots")
    icon = pygame.image.load('../images/chinchilla_icon_sha.png')
    pygame.display.set_icon(icon)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(TITLE_1, TITLE_RECT_1)