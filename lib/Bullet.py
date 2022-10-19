import pygame


bulletImg = pygame.image.load('images/bullet.png')
bulletX = player_x
bulletY = player_y
bulletX_change = 10
bulletY_change = 0
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    CANVAS.blit(bulletImg, ( x, y ))

    '''
                if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletY = player_y
                    fire_bullet(bulletY,bulletX)
    '''


    '''
    
    if bulletX >= 800:
        bulletX = player_x
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletX_change
    
    '''
