from typing import Any
import pygame
from pygame.sprite import _Group
from config import GREEN, WIDTH, HEIGHT

class Plants(pygame.sprite.Sprite):
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
        for image in self.image_list:
            pygame.transform.flip(image, True, False)