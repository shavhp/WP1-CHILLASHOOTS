import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("ChillaShoots")
icon = pygame.image.load('chinchilla_icon_sha.png')
pygame.display.set_icon(icon)

# Player sprite
player_img = pygame.image.load("chinchilla_sprite_sha.png")
player_X_axis = 25
player_Y_axis = 320

# Creates function for player to draw image of sprite icon
def player(x,y):
    SCREEN.blit(player_img, (x, y))

# Main event loop, contains everything that has to stay infinitely consistent
running = True
while running:

    # Adds background color to screen
    # Gets drawn first
    SCREEN.fill((28, 79, 66))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.QUIT:
            running = False

        # Checks whether keystroke is left or right when pressed

        '''
        
        I have to fix this if-statement, because the screen closes
        
        everytime I press an arrow key. I don't get to see the print
        
        that says I have pressed left or right arrow or have let key
        
        back up.
        
        '''

        if event.type == pygame.KEYDOWN:
            print("A keystroke")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")

    player(player_X_axis, player_Y_axis)
    pygame.display.update()