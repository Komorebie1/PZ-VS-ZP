import pygame
from config import GREEN, WIDTH, HEIGHT
from Bullet import Bullet
from Sun import Sun
import random

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

    def update(self, *args, **kwargs) -> None:
        self.image_idx = args[0] % len(self.image_list)
        self.image = self.image_list[self.image_idx]
        # self.rect = self.image.get_rect()
    
    def getrect(self):  
        return self.rect

    def convert(self) -> None:
        for i in range(len(self.image_list)):
            self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)

class PeaShooter(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        if self.image_idx == 0:
            bullet = Bullet(self.rect)
            args[1].add(bullet)
            

class SunFlower(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)
    
    def produce_sun(self):
        sun = Sun(self.rect)
        return sun

class WallNut(Plants):
    def __init__(self, image_path, image_nums, position):
        Plants.__init__(self, image_path, image_nums, position)
