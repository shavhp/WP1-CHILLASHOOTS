import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load('chinchilla_icon_sha.png')
pygame.display.set_icon(icon)

# Player sprite
player_img = pygame.image.load("chinchilla_sprite_sha.png")
player_X_axis = 25
player_Y_axis = 320
player_X_axis_change = 0
player_Y_axis_change = 0

# Creates function for player to draw image of sprite icon
def player(x, y):
    SCREEN.blit(player_img, (x, y))

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Adds background color to screen
    # Gets drawn first
    SCREEN.fill((28, 79, 66))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

        # Checks whether keystroke is left, right, up or down when pressed

        if event.type == pygame.KEYDOWN:
            print("A keystroke")
            if event.key == pygame.K_LEFT:
                player_X_axis_change = -0.25
            if event.key == pygame.K_RIGHT:
                player_X_axis_change = 0.25
            if event.key == pygame.K_UP:
                player_Y_axis_change = -0.25
            if event.key == pygame.K_DOWN:
                player_Y_axis_change = 0.25

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_X_axis_change = 0
                player_Y_axis_change = 0

    player_X_axis += player_X_axis_change
    player_Y_axis += player_Y_axis_change
    player(player_X_axis, player_Y_axis)
    pygame.display.update()