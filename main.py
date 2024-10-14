import pygame
import time
from Zombies import Zombie
from Plants import PeaShooter, SunFlower, WallNut
import config
from config import WIDTH, HEIGHT, FPS


def main():
    pygame.init()
    pygame.display.set_caption("植物大战僵尸")
    background = pygame.image.load(config.BackGroundPath)
    sunback = pygame.image.load(config.SunBackPath)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    myfont = pygame.font.Font(None, 60)
    all_sprites = pygame.sprite.Group()

    zombie = Zombie(*config.ZombiePath)
    all_sprites.add(zombie)

    peashooter = PeaShooter(*config.PeaShooterPath, (250, 100))
    all_sprites.add(peashooter)

    sunflower = SunFlower(*config.SunFlowerPath, (250, 200))
    all_sprites.add(sunflower)    

    wallnut = WallNut(*config.WallNutPath, (250, 300))
    all_sprites.add(wallnut)

    Running = True

    while Running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        screen.fill(config.WHITE)
        screen.blit(background, (0, 0))
        screen.blit(sunback,(250,0))

        for sprite in all_sprites:
            if type(sprite).__name__ == "PeaShooter":
                sprite.update(all_sprites)
            else:sprite.update()

        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
