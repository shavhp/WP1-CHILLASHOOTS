import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

#Icon and caption
pygame.display.set_caption("Beast shooter")
icon = pygame.image.load("chinchilla_icon_sha.png")
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 350
textY = 300

def show_text(x, y):
    text = font.render("Hello", True, (255, 255, 255))
    screen.blit(text, (x, y))

#Loop game
running = True
while running:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False

    #Background color
    screen.fill((0, 0,0))
    show_text(textX, textY)
    pygame.display.update()
