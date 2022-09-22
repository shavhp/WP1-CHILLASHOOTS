import pygame

# Set up pygame.
pygame.init()

# Create screen
SCREEN = pygame.display.set_mode((1024, 768))

# Title and Icon
pygame.display.set_caption("ChillaShoots")

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            event.key = pygame.K_ESCAPE
            running = False

        elif event.type == pygame.QUIT:
            running = False
