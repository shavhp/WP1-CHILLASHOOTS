from lib.Title import *


def game_over():
    # Font and color of title
    title_font = pygame.font.Font('../fonts/gametitle_04B_30__.ttf', 60)
    red = (255, 0, 0)

    # Create text surface object
    title_1 = title_font.render('GAME', True, red, None)
    title_2 = title_font.render('OVER!!!', True, red, None)

    # Create rectangular object for text surface object
    title_rect_1 = title_1.get_rect()
    title_rect_2 = title_2.get_rect()

    # Set center of rectangular object
    title_rect_1.center = (SCREEN_WIDTH // 3.09, SCREEN_HEIGHT // 3)
    title_rect_2.center = (SCREEN_WIDTH // 1.39, SCREEN_HEIGHT // 3)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(title_1, title_rect_1)
    CANVAS.blit(title_2, title_rect_2)
