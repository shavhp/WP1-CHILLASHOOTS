import pygame
from pygame.sprite import Sprite
import random


class DummyEnemy(Sprite):
    def __init__(self, enemy_image="../images/test.png"):
        entity_count = pygame.sprite.Group()
        entity_visible = pygame.sprite.Group()

        enemy_speed_x = random.randint(2, 4)
        enemy_speed_y = 6
        x_start = 864
        y_start = random.randint(0, 536)

        # Create index thing of the speed variables for reversing
        super().__init__()
        self.enemy_speed_x = -enemy_speed_x
        self.enemy_speed_y = enemy_speed_y
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # Load the image
        self.image = pygame.image.load(enemy_image).convert_alpha()

        # Object rectangle needed for collision and starting position
        self.rect = self.image.get_rect()
        self.rect.x = x_start
        self.rect.y = y_start

    # Draw the object on the display, collision rectangle checking canvas size,
    # and equalling object speed to the rectangle
    def update(self, canvas):
        self.bounce_if_required(canvas.get_width(), canvas.get_height())
        self.rect = self.rect.move(self.current_speed)
        canvas.blit(self.image, self.rect)

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy reverses when hitting the top side of the display.
        if self.rect.top <= 0:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy reverses when hitting the bottom side of the display.
        elif self.rect.bottom >= screen_height:
            self.current_speed[1] = -self.enemy_speed_y

    def reverse(self):
        self.current_speed[0] = -self.current_speed[0]
        self.current_speed[1] = -self.current_speed[1]


class Bouncer(DummyEnemy):
    def __init__(self, enemy_image="../images/chinchilla_sprite_light.png"):
        super().__init__()
        x_start = 400
        y_start = random.randint(0, 536)

        # For some reason, it is okay to have the enemy speed variables to be this simple
        self.enemy_speed_x = 6
        self.enemy_speed_y = 6
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # These lines are always needed when creating enemy derivatives with different images or starting positions
        self.image = pygame.image.load(enemy_image).convert_alpha()
        self.rect.x = x_start
        self.rect.y = y_start

    def bounce_if_required(self, screen_width, screen_height):
        # Enemy reverses when hitting the left side of the display.
        if self.rect.left <= 0:
            self.current_speed[0] = self.enemy_speed_x
        # Enemy reverses when hitting the right side of the display.
        elif self.rect.right >= screen_width:
            self.current_speed[0] = -self.enemy_speed_x

        # Enemy reverses when hitting the top side of the display.
        if self.rect.top <= 0:
            self.current_speed[1] = self.enemy_speed_y
        # Enemy reverses when hitting the bottom side of the display.
        elif self.rect.bottom >= screen_height:
            self.current_speed[1] = -self.enemy_speed_y

class Line(DummyEnemy):
    def __init__(self, enemy_image="../images/chinchilla_sprite_light.png"):
        super().__init__()
        x_start = 864
        y_start = random.randint(0, 536)

        self.enemy_speed_x = -random.randint(4, 8)
        self.enemy_speed_y = 0
        self.current_speed = [self.enemy_speed_x, self.enemy_speed_y]

        # These lines are always needed when creating enemy derivatives with different images or starting positions
        self.image = pygame.image.load(enemy_image).convert_alpha()
        self.rect.x = x_start
        self.rect.y = y_start

