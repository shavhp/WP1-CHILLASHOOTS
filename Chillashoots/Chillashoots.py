from lib.Button import *
from lib.Setting_menu import *
from lib.Enemy import *
from lib.Moving_Background_1 import *
from lib.Sound import sound_maker
from lib.Player import *
# from lib.Title import *
from lib.Setting_menu import setting_page
from lib.high_score import *
import os

# Initializes pygame library
pygame.init()

# Make button
start_img = pygame.image.load(os.path.join('../images', 'button_start.png')).convert_alpha()
more_img = pygame.image.load(os.path.join('../images', 'button_more.png')).convert_alpha()
start_button = Button(250, 300, start_img, 1)
more_button = Button(460, 430, more_img, 1)

# Define colors
GREY = (200, 200, 200)


bulletImg = pygame.image.load('../images/bullet.png')
bulletX = player_x
bulletY = player_y
bulletX_change = 50
bulletY_change = 0
bullet_state = "ready"

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Enemy spawn timers
enemy_timer = 0
bouncer_enemy_timer = 0

font_score = pygame.font.Font('../fonts/superstar_memesbruh03.ttf', 25)

# Game speed and frame counter
frame_count = 0
frame_rate = 60
start_time = 0

# Calculate total seconds
total_seconds = frame_count // frame_rate

# For infinite enemy spawning
global enemySprites
enemySprites = pygame.sprite.RenderPlain(())
# Pre-places an enemy, speed can be modified (x,y)
enemySprites.add(Upper(10))
enemySprites.add(Lower(10))




def get_high_score():
    # Default high score
    high_score = 0

    # Try to read high score from file
    try:
        high_score_file = open("../high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print (high_score)

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



def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    CANVAS.blit(bulletImg, (x + 50, y + 10 ))

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:
    title()
    sound_maker()
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
    # if high_score_button.draw(CANVAS):
       # print("NO highscore")
    if start_button.draw(CANVAS):

        # Player sprite
        player_sprite(player_x, player_y)


        # Main event loop, contains everything that has to stay infinitely consistent
        running = True
        scroll = 0
        while running:

            # Gets drawn first
            # Background image and coordinates of image appearance
            CANVAS.blit(BACKGROUND, (0, 0))
            clock.tick(FPS)
            for i in range(0, tiles):
                screen.blit(bg, (i * bg_width + scroll, 0))
            scroll -= 10
            if abs(scroll) > bg_width:
                scroll = 0

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
            elif enemy_timer >= 50:
                enemySprites.add(BaseEnemy(random.randint(8, 12)))
                enemy_timer = 0

            # Time-triggered enemy spawning
            if total_seconds >= 90:
                bouncer_enemy_timer += 1
                if bouncer_enemy_timer == 90:
                    enemySprites.add(Bouncer(10))
                    bouncer_enemy_timer = 0

            # Increase spawn frequency of existing timer
            if total_seconds >= 400:
                enemy_timer += 1

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
                            bulletX = player_x
                            bulletY = player_y
                            fire_bullet(bulletY, bulletX)

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

            if bulletX >= 800:
                bullet_state = "ready"

            if bullet_state == "fire":
                fire_bullet(bulletX, bulletY)
                bulletX += bulletX_change


            '''
            # This tracks the player's coordinates
            print({player_x})
            print({player_y})
            print (total_seconds)
            '''

            test = 0
            if test == 0:
                get_high_score()
                high_score_main()

            player_x += player_x_change
            player_y += player_y_change
            player_sprite(player_x, player_y)
            pygame.display.update()

            # Clock ticking to the game speed
            clock.tick(frame_rate)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
