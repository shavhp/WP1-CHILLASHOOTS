from lib.Screen import *
from lib.high_score import *

BACKGROUND = pygame.image.load('../images/background-galaxy.jpg')


def title():
    # Font and color of title
    TITLE_FONT = pygame.font.Font('../fonts/gametitle_04B_30__.ttf', 60)
    # HIGH_SCORE_FONT = pygame.font.Font('../fonts/superstar_memesbruh03.ttf', 28)
    GREY = (200, 200, 200)
    BLACK = (0, 0, 0)

    # Create text surface object
    TITLE_1 = TITLE_FONT.render('CHILLA', True, GREY, None)
    TITLE_2 = TITLE_FONT.render('SHOOTS', True, BLACK, None)
    # HIGH_SCORE = HIGH_SCORE_FONT.render(f'Highscore: 00000', True, GREY, None)

    # Create rectangular object for text surface object
    TITLE_RECT_1 = TITLE_1.get_rect()
    TITLE_RECT_2 = TITLE_2.get_rect()
    # HIGH_SCORE_RECT = HIGH_SCORE.get_rect()

    # Set center of rectangular object
    TITLE_RECT_1.center = (SCREEN_WIDTH // 3.09, SCREEN_HEIGHT // 3)
    TITLE_RECT_2.center = (SCREEN_WIDTH // 1.39, SCREEN_HEIGHT // 3)
    # HIGH_SCORE_RECT.center = (SCREEN_WIDTH // 2.3, SCREEN_HEIGHT // 1.30)

    # Title and Icon
    pygame.display.set_caption("ChillaShoots")
    icon = pygame.image.load('../images/chinchilla_icon_sha.png')
    pygame.display.set_icon(icon)

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))
    CANVAS.blit(TITLE_1, TITLE_RECT_1)
    CANVAS.blit(TITLE_2, TITLE_RECT_2)
    # CANVAS.blit(HIGH_SCORE, HIGH_SCORE_RECT)

