# Import pygame module
import pygame

# Imports OS for file paths
import os

import pygame.sprite

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
icon = pygame.image.load(os.path.join('images', 'chinchilla_icon.png'))
pygame.display.set_icon(icon)

player_x = 25
player_y = 320
player_x_change = 0
player_y_change = 0
player_speed = 20


class Player(pygame.sprite.Sprite):
    # Sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((200, 200, 200))
        # Defines rectangle around image, so program can define where spire is or needs to be
        # Auto-detect rectangle around image based on img measurements
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x
        self.rect.centery = player_y
        self.speed = 0
    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed = player_speed
        if keystate[pygame.K_RIGHT]:
            self.speed = player_speed

player_sprite = pygame.sprite.Group()
chilla_player = Player()
player_sprite.add(chilla_player)


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font_score = pygame.font.Font('fonts/superstar_memesbruh03.ttf', 25)

frame_count = 0
frame_rate = 60
start_time = 0

# Calculate total seconds
total_seconds = frame_count // frame_rate

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Gets drawn first
    # Background image and coordinates of image appearance
    CANVAS.blit(BACKGROUND, (0, 0))

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

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False


    '''
    # This tracks the player's coordinates
    print({player_X_axis})
    print({player_Y_axis})
    '''

    chilla_player.update()
    pygame.display.update()
