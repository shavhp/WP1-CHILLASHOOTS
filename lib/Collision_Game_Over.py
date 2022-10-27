import pygame.sprite
from lib.Button import *
from lib.Setting_menu import *
from lib.Enemy import *
from lib.Moving_Background_1 import *
from lib.Sound import sound_maker
from lib.Player import *
from lib.Setting_menu import setting_page
import os

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

GREY = (200, 200, 200)

# Make button
start_img = pygame.image.load(os.path.join('../images', 'button_start.png')).convert_alpha()
more_img = pygame.image.load(os.path.join('../images', 'button_more.png')).convert_alpha()

start_button = Button(250, 300, start_img, 1)
more_button = Button(460, 430, more_img, 1)
font_score = pygame.font.Font('../fonts/superstar_memesbruh03.ttf', 25)

high_score = 0
high_score_file = open("../high_score.txt", "r")
high_score = int(high_score_file.read())
high_score_file.close()

HIGH_SCORE_FONT = pygame.font.Font('../fonts/superstar_memesbruh03.ttf', 28)
HIGH_SCORE = HIGH_SCORE_FONT.render(f'Highscore:{high_score}', True, GREY, None)

HIGH_SCORE_RECT = HIGH_SCORE.get_rect()
HIGH_SCORE_RECT.center = (SCREEN_WIDTH // 2.3, SCREEN_HEIGHT // 1.30)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((800, 600))
enemy_timer = 0
bouncer_enemy_timer = 0
enemySprites = pygame.sprite.Group()
frame_count = 0
frame_rate = 60
start_time = 0
player_speed = 20

# Calculate total seconds
total_seconds = frame_count // frame_rate


def get_high_score():
    # Default high score
    high_score = 0

    # Try to read high score from file
    try:
        high_score_file = open("../high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print(high_score)

    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There is a file, but we don't understand the number
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):
    try:
        # Write file to disk
        high_score_file = open("../high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Can't write it
        print("Unable to save high score.")


def high_score_main():
    ''' Main program here '''
    # Get high score
    high_score = get_high_score()

    # Get score from current game
    current_score = total_seconds

    # See if we have a new high score
    if current_score > high_score:
        # There is a new high score, save to disk
        save_high_score(current_score)


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
        self.speed = random.randint(5, 10)

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
        self.speedx = 1
        self.speedy = 1

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

        # Player stays within the screen boundaries
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 736:
            self.rect.x = 736
        elif self.rect.y < 0:
            self.rect.y = 0
        # Value of 536 = height of screen - height of sprite (600px - 64px)
        elif self.rect.y > 536:
            self.rect.y = 536

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y + 25
        self.rect.centerx = x + 33
        self.speedx = +10

    def update(self):
        self.rect.x += self.speedx
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()


running = True
while running:
    title()
    sound_maker()
    CANVAS.blit(HIGH_SCORE, HIGH_SCORE_RECT)
    if more_button.draw(CANVAS):
        running = True
        while running:
            setting_page()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

    if start_button.draw(CANVAS):
        # Player sprite
        player_sprite(player_x, player_y)
        run = True
        scroll = 0
        while run:
            quit_game()
            # Gets drawn first
            # Background image and coordinates of image appearance
            CANVAS.blit(BACKGROUND, (0, 0))
            clock.tick(FPS)
            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
            scroll -= 10
            if abs(scroll) > bg_width:
                scroll = 0

            test = 0
            if test == 0:
                get_high_score()
                high_score_main()

            # String formatting to format in leading zeros
            output_time = "Score {0}".format(total_seconds)

            # Timer going up
            total_seconds = start_time + (frame_count // frame_rate)

            # Increase frame count
            frame_count += 22

            # Limit frames per second
            clock.tick(frame_rate)

            # Blit score to the screen
            text_score = font_score.render(output_time, True, GREY)
            CANVAS.blit(text_score, [650, 25])

            # Spawning enemies
            enemySprites.update(CANVAS)
            enemy_timer += 1
            if enemy_timer == 30:
                enemySprites.add(Upper(random.randint(7, 12)))
                enemySprites.add(Lower(random.randint(7, 12)))
            elif enemy_timer >= 60:
                enemySprites.add(BaseEnemy(random.randint(8, 12)))
                enemy_timer = 0

            # Time-triggered enemy spawning
            if total_seconds >= 200:
                bouncer_enemy_timer += 1
                if bouncer_enemy_timer == 90:
                    enemySprites.add(Bouncer(10))
                    bouncer_enemy_timer = 0

            # Increase spawn frequency of existing timer
            if total_seconds >= 400:
                enemy_timer += 1

            pygame.time.delay(30)
            all_sprites.update()

            hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
            for hit in hits:
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)
            hit = pygame.sprite.groupcollide(enemySprites, bullets, True, True)

            hits = pygame.sprite.spritecollide(player, mobs, False)
            if hits:
                run = False
                running = False

            hit = pygame.sprite.spritecollide(player, enemySprites, False)
            if hit:
                run = False
                running = False
            all_sprites.draw(screen)
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

if run == False:
    endgame = True
    while endgame:
        Game_Over()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                endgame = False

            if event.type == pygame.QUIT:
                endgame = False
        pygame.display.update()
