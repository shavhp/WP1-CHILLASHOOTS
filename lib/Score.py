# Is unused at this point.
# Code is fully added to main file

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CANVAS = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
GREY = (200, 200, 200)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font_score = pygame.font.Font('../fonts/superstar_memesbruh03.ttf', 25)

def score_count():

    frame_count = 0
    frame_rate = 60
    start_time = 0

    global total_seconds

    # Calculate total seconds
    total_seconds = frame_count // frame_rate

    # String formatting to format how score is displayed
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

    print(pygame.time.get_ticks())

