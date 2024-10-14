import pygame
from config import GREEN, WIDTH, HEIGHT


class Zombie(pygame.sprite.Sprite):
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

    def __init__(self, image_path, image_nums):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = [
            pygame.image.load(image_path + "_" + str(i) + ".png") for i in range(image_nums)
        ]
        self.image_idx = 0
        self.image = self.image_list[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, HEIGHT / 2)
        self.speed = (-5, 0)
        # self.convert()

    def update(self, *args, **kwargs) -> None:
        self.image = self.image_list[self.image_idx]

        self.image_idx += 1
        if self.image_idx == len(self.image_list):
            self.image_idx = 0
        
        self.rect.x += self.speed[0]

        if self.rect.right < 0:
            self.rect.left = WIDTH

    def convert(self):
        for i in range(len(self.image_list)):
            self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)


