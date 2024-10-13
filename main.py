import pygame
import time
from player import Zombie
from config import WIDTH, HEIGHT, BLACK, WHITE, FPS, BackGroundPath, SunBackPath, ZombiePath


def main():
    pygame.init()
    pygame.display.set_caption("植物大战僵尸")
    background = pygame.image.load(BackGroundPath)
    sunback = pygame.image.load(SunBackPath)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    myfont = pygame.font.Font(None, 60)
    all_sprites = pygame.sprite.Group()

    zombie = Zombie(*ZombiePath)
    all_sprites.add(zombie)

    Running = True

    while Running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        screen.fill(WHITE)
        screen.blit(background, (0, 0))
        screen.blit(sunback,(250,0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
