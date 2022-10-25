import pygame.sprite

from lib.Enemy import *
from lib.Screen import *
WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
pygame.init()
screen = pygame.display.set_mode((800, 600))
enemy_timer = 0
enemySprites = pygame.sprite.RenderPlain(())
frame_count = 0
frame_rate = 60
start_time = 0
player_speed = 20

all_sprites = pygame.sprite.Group()

# Calculate total seconds
total_seconds = frame_count // frame_rate
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join('../images', 'ghost.png'))
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the enemy based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.rect = self.image.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT)
                )
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('../images', 'chinchilla_sprite_light.png'))
        self.rect = self.image.get_rect()
        self.rect.top = 25
        self.rect.bottom = 320
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        userinput = pygame.key.get_pressed()
        if userinput[pygame.K_LEFT]:
            self.speedx = -player_speed
        if userinput[pygame.K_RIGHT]:
            self.speedx = +player_speed
        if userinput[pygame.K_UP]:
            self.speedy = -player_speed
        if userinput[pygame.K_DOWN]:
            self.speedy = +player_speed

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0




all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

run = True
while run :
    quit_game()
    screen.fill((255,255,255))
    # Diagonal movement makes sprite disappear in corners



    # Enemy timer
    enemySprites.update(CANVAS)
    enemy_timer += 1
    if enemy_timer == 50:
        enemySprites.add(BaseEnemy(random.randint(2, 2)))
        enemy_timer = 0

    pygame.time.delay(30)
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        run = False
    all_sprites.draw(screen)
    pygame.display.update()