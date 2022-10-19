# Import pygame module
import pygame
from Enemy import *

# Imports OS for file paths
import os

# Set up pygame.
pygame.init()

# Create screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
GREY = (200, 200, 200)

# Show background image
BACKGROUND = pygame.image.load(os.path.join('images', 'background-galaxy.jpg'))

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load(os.path.join('images', 'chinchilla_icon_sha.png'))
pygame.display.set_icon(icon)

player_x = 25
player_y = 320
player_x_change = 0
player_y_change = 0
player_speed = 7


bulletImg = pygame.image.load('images/bullet.png')
bulletX = player_x
bulletY = player_y
bulletX_change = 10
bulletY_change = 0
bullet_state = "ready"

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font_score = pygame.font.Font('fonts/superstar_memesbruh03.ttf', 25)

frame_count = 0
frame_rate = 60
start_time = 0

enemy_timer = 0
global enemySprites
enemySprites = pygame.sprite.RenderPlain(())

# Calculate total seconds
total_seconds = frame_count // frame_rate

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    CANVAS.blit(bulletImg, ( x, y ))

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))


    def player_sprite(x, y):
        player_img = pygame.image.load(os.path.join('images', 'chinchilla_sprite_light.png'))
        player_rect = player_img.get_rect()
        player_rect = player_rect.move(player_x_change, player_y_change)
        pygame.draw.rect(player_rect)
        print(player_rect)
        print(player_x_change, player_y_change)
        # Creates function for player to draw image of sprite icon on given coordinates
        CANVAS.blit(player_img, (x, y), player_rect)

    # String formatting to format in leading zeros
    output_time = "Score {0}".format(total_seconds)

    # Timer going up
    total_seconds = start_time + (frame_count // frame_rate)

    # Increase frame count
    frame_count += 10

    # Limit frames per second
    clock.tick(frame_rate)

    # Blit score to the screen
    text_score = font_score.render(output_time, True, GREY)
    CANVAS.blit(text_score, [650, 25])

    # Enemy timer
    enemySprites.update(CANVAS)
    enemy_timer += 1
    if enemy_timer == 50:
        enemySprites.add(BaseEnemy(random.randint(2, 2)))
        enemy_timer = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

        # Checks whether keystroke is left, right, up or down when pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_UP:
                player_y_change = -player_speed
            if event.key == pygame.K_DOWN:
                player_y_change = player_speed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletY = player_y
                    fire_bullet(bulletY,bulletX)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_x_change = 0
                player_y_change = 0

        # Diagonal movement makes sprite disappear in corners
        # Value of 736 = width of screen - width of sprite (800px - 64px)
        if player_x < 0:
            player_x = 0
        elif player_x > 736:
            player_x = 736
        elif player_y < 0:
            player_y = 0
        # Value of 536 = height of screen - height of sprite (600px - 64px)
        elif player_y > 536:
            player_y = 536

            # Bullet Movement
    if bulletX >= 800:
        bulletX = player_x
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change


    '''
    # This tracks the player's coordinates
    print({player_X_axis})
    print({player_Y_axis})
    '''

    player_x += player_x_change
    player_y += player_y_change
    player_sprite(player_x, player_y)
    pygame.display.update()
