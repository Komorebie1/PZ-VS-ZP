import pygame
import time
import random

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
    myfont = pygame.font.SysFont('Arial', 30)
    all_sprites = pygame.sprite.Group()
    sunlist = pygame.sprite.Group()
    animation_index = 0

    score = '1000'
    txtImg = myfont.render(score, True, (0, 0, 0))


    # 创建僵尸和植物
    zombie = Zombie(*config.ZombiePath)
    all_sprites.add(zombie)
    peashooter = PeaShooter(*config.PeaShooterPath, (250, 100))
    all_sprites.add(peashooter)
    sunflower = SunFlower(*config.SunFlowerPath, (250, 200))
    all_sprites.add(sunflower)
    wallnut = WallNut(*config.WallNutPath, (250, 300))
    all_sprites.add(wallnut)

    Running = True

    #定义生成太阳的事件
    GENERATORSUNEVNET = pygame.USEREVENT + 1
    pygame.time.set_timer(GENERATORSUNEVNET, 2000)

    while Running:
        clock.tick(FPS)

        animation_index += 1
        animation_index = animation_index==998244353 and 0 or animation_index

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == GENERATORSUNEVNET:
                for spirit in all_sprites:
                    if isinstance(spirit, SunFlower):
                        sunlist.add(spirit.produce_sun())
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if pressed_array[0]:
                    pos = pygame.mouse.get_pos()
                    # print(pos)
                    for sun in sunlist:
                        if sun.rect.collidepoint(pos):
                            sun.isclicked = True
                            sunlist.remove(sun)
                            score = str(int(score) + 50)
                            myfont = pygame.font.SysFont('Arial', 30)
                            txtImg = myfont.render(score, True, (0, 0, 0))

        screen.blit(background, (0, 0))
        screen.blit(sunback,(250,30))
        screen.blit(txtImg, (300, 33))

        all_sprites.update(animation_index, all_sprites)
        sunlist.update(animation_index)

        all_sprites.draw(screen)
        sunlist.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
