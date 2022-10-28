from lib.Game_Over import *


def setting_page():
    # Font and color of title
    title_font = pygame.font.Font('../fonts/gametitle_04B_30__.ttf', 60)
    grey = (200, 200, 200)

    # Create text surface object
    title_1 = title_font.render('Settings', True, grey, None)

    # Create rectangular object for text surface object
    title_rect_1 = title_1.get_rect()

    # Set center of rectangular object
    title_rect_1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5)

    # Title and Icon
    pygame.display.set_caption("ChillaShoots")
    icon = pygame.image.load('../images/chinchilla_icon.png')
    pygame.display.set_icon(icon)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(title_1, title_rect_1)

    color_white = (0.2, 0.4, 0.6)
    pygame.draw.rect(CANVAS, color_white, pygame.Rect(50, 200, 700, 350), 0, 7)
