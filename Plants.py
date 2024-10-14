import pygame
from config import GREEN, WIDTH, HEIGHT
from Bullet import Bullet

class Plants(pygame.sprite.Sprite):
    '''
    rect

    (x, y) --- top --- topright
        |                   |
        |                   |
        |                   |
    left --- center --- right
        |                   |
        |                   |
        |                   |
    bottom --- bottomleft --- bottomright

    '''
    def __init__(self, image_path, image_nums, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = [
            pygame.image.load(image_path + "_" + str(i) + ".png") for i in range(image_nums)
        ]
        self.image_idx = 0
        self.image = self.image_list[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self) -> None:
        self.image = self.image_list[self.image_idx]
        self.image_idx += 1
        if self.image_idx == len(self.image_list):
            self.image_idx = 0

    def convert(self) -> None:
        for i in range(len(self.image_list)):
            self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)

class PeaShooter(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)

    def update(self, all_sprites) -> None:
        super().update()
        if self.image_idx == 0:
            bullet = Bullet(self.rect)
            all_sprites.add(bullet)
            pygame.display.flip()
            

class SunFlower(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)

class WallNut(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)

