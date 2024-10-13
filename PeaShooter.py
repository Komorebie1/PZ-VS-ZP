import pygame
from Plants import Plants
from config import GREEN, WIDTH, HEIGHT

class PeaShooter(Plants):
    def __init__(self, image_path, image_nums, position):
        super().__init__(image_path, image_nums, position)
