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

    CANVAS.blit(player_img, (x, y))


