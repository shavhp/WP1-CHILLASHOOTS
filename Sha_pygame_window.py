import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((1024, 768))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False