
# add to player class
def creat_bullet(self):
    return Bullet(player_X_axis,player_Y_axis)

#bullet speed
bullet_speed = 5


class Bullet(pygame.sprite.Sprite):
    # creats de bullet at the player axis
    def __intit__(self,player_X_axis,player_Y_axis):
        super().__intit__()
        self.image = pygame.Surface((50,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (player_X_axis,player_Y_axis))

    # makes the bullet move forward
    def update(self):
        self.rect.x += bullet_speed


# makes it posible to have more then one bullet
bullet_group = pygame.sprite.Group()

# add to gameloop (drawing bullet)
bullet_group.draw(CANVAS)
bullet_group.update()

# add to for event loop
if event.type == pygame.MOUSEBUTTONDOWN:
    bullet_group.add(creat_bullet())



 # bron : https://www.youtube.com/watch?v=JmpA7TU_0Ms&t=354s

