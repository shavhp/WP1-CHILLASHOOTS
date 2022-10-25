from lib.Screen import *
import pygame
import os

player_x = 25
player_y = 320
player_x_change = 0
player_y_change = 0
player_speed = 20
def player_sprite(x, y):
    player_img = pygame.image.load(os.path.join('../images', 'chinchilla_sprite_light.png'))
    # Creates function for player to draw image of sprite icon on given coordinates
    # rect_of_chinchilla_sprite = player_img.get_rect()
    CANVAS.blit(player_img, (x, y))


'''def player_move():
    for event in pygame.event.get():
        # Checks whether keystroke is left, right, up or down when pressed
        if event.type == pygame.KEYDOWN:
            global player_x_change, player_y_change
            if event.key == pygame.K_LEFT:
                player_x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_UP:
                player_y_change = -player_speed
            if event.key == pygame.K_DOWN:
                player_y_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_x_change = 0
                player_y_change = 0

    global player_x, player_y
    player_x += player_x_change
    player_y += player_y_change'''


'''def player_borders():
    # Diagonal movement makes sprite disappear in corners
    # Value of 736 = width of screen - width of sprite (800px - 64px)
    global player_x, player_y
    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736
    elif player_y < 0:
        player_y = 0
    # Value of 536 = height of screen - height of sprite (600px - 64px)
    elif player_y > 536:
        player_y = 536'''
