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


# Incomplete merging
'''player_x = 25
player_y = 320
player_speed = 20
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('../images', 'chinchilla_sprite_light.png'))
        self.rect = self.image.get_rect()
        self.rect.top = player_x
        self.rect.bottom = player_y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        userinput = pygame.key.get_pressed()
        if userinput[pygame.K_LEFT]:
            self.speed_x = -player_speed
        if userinput[pygame.K_RIGHT]:
            self.speed_x = +player_speed
        if userinput[pygame.K_UP]:
            self.speed_y = -player_speed
        if userinput[pygame.K_DOWN]:
            self.speed_y = +player_speed

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0

class Bullet(pygame.sprite.Sprite)
    bulletImg = pygame.image.load('../images/bullet.png')
    bulletX = player_x
    bulletY = player_y
    bulletX_change = 50
    bulletY_change = 0
    bullet_state = "ready"'''



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
