import pygame
from Plants import Plants
from config import GREEN, WIDTH, HEIGHT

class PeaShooter(Plants):
    def __init__(self, image_path, image_nums, position = (0, 0)):
        super().__init__(image_path, image_nums, position)
        self.rect.top = 100
        self.rect.left = 250