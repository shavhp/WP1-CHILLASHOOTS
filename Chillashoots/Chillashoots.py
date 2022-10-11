from lib.Button import Button
from lib.Titel import *

# Initializes pygame library

pygame.init()

# Show background image
BACKGROUND = pygame.image.load('../images/background-galaxy.jpg')
start_img = pygame.image.load('../images/start_button.png').convert_alpha()
start_button = Button(300, 300, start_img, 0.5)

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:
    titel()

    if start_button.draw(CANVAS):
        # Create screen
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Show background image
        BACKGROUND = pygame.image.load('../images/background-galaxy.jpg')

        # Title and Icon
        pygame.display.set_caption("ChillaShoots")
        icon = pygame.image.load('../images/chinchilla_icon_sha.png')
        pygame.display.set_icon(icon)

        # Player sprite

        player_img = pygame.image.load("../images/chinchilla_sprite_light.png")
        player_X_axis = 25
        player_Y_axis = 320
        player_X_axis_change = 0
        player_Y_axis_change = 0
        player_speed = 0.25


        # Creates function for player to draw image of sprite icon
        def player(x, y):
            CANVAS.blit(player_img, (x, y))


        # Main event loop, contains everything that has to stay infinitely consistent
        running = True
        while running:

            # Gets drawn first
            # Background image and coordinates of image appearance
            CANVAS.blit(BACKGROUND, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

                if event.type == pygame.QUIT:
                    running = False

                # Checks whether keystroke is left, right, up or down when pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_X_axis_change = -player_speed
                    if event.key == pygame.K_RIGHT:
                        player_X_axis_change = player_speed
                    if event.key == pygame.K_UP:
                        player_Y_axis_change = -player_speed
                    if event.key == pygame.K_DOWN:
                        player_Y_axis_change = player_speed

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_X_axis_change = 0
                        player_Y_axis_change = 0

            # Diagonal movement makes sprite disappear in corners

            # Value of 736 = width of screen - width of sprite (800px - 64px)
            if player_X_axis < 0:
                player_X_axis = 0
            elif player_X_axis > 736:
                player_X_axis = 736
            elif player_Y_axis < 0:
                player_Y_axis = 0
            # Value of 536 = height of screen - height of sprite (600px - 64px)
            elif player_Y_axis > 536:
                player_Y_axis = 536

            '''
            # This tracks the player's coordinates
            print({player_X_axis})
            print({player_Y_axis})
            '''

            player_X_axis += player_X_axis_change
            player_Y_axis += player_Y_axis_change
            player(player_X_axis, player_Y_axis)
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
