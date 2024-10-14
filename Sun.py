import pygame
import random
import numpy as np


class Sun(pygame.sprite.Sprite):
    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/Sun/Sun_0.png').convert_alpha()
        self.images = [pygame.image.load('./images/Sun/Sun_{}.png'.format(i)).convert_alpha() for i in
                       range(17)]
        self.rect = self.images[0].get_rect()
        offsetTop = random.randint(-50, 50)
        offsetLeft = random.randint(-50, 50)

        self.rect.top = rect.top
        self.rect.left = rect.left         
        self.dest = (rect.top + offsetTop, rect.left + offsetLeft)
        self.times = 4
        self.is_click = False 
        self.speed = 2

    def update(self, *args):
        if self.rect.top != self.dest[0]:
            self.rect.top += (self.dest[0] - self.rect.top) / abs(self.dest[0] - self.rect.top) * self.speed

        if self.rect.left != self.dest[1]:
            self.rect.left += (self.dest[1] - self.rect.left) / abs(self.dest[1] - self.rect.left) * self.speed

        
        self.image = self.images[args[0] % len(self.images)]
        if self.is_click:
            self.rect.left -= (self.rect.left - 250) / self.times
            self.rect.top -= (self.rect.top - 30) / self.times

            if self.rect.left <= 250 and self.rect.top <= 30:
                self.kill()
        
