from lib.Screen import *
import pygame
import os

# Coordinates of where character sprite spawns in screen
player_x = 25
player_y = 320
# Defines variables for movement when no keys are pressed
player_x_change = 0
player_y_change = 0
# Defines the speed that the character sprite moves when keys are pressed
player_speed = 20

# Creates function for player to draw image of sprite icon on given coordinates
def player_sprite(x, y):
    player_img = pygame.image.load(os.path.join('../images', 'chinchilla_sprite_light.png'))
    CANVAS.blit(player_img, (x, y))
