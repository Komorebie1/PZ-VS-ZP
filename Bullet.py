import pygame
import config

class Bullet(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(config.PeaNormalPath)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = rect[0] + 45, rect[1]
        self.speed = 5

    def update(self, *args, **kwargs):
        self.rect.left += self.speed
        if self.rect.left > config.WIDTH:
            self.kill()