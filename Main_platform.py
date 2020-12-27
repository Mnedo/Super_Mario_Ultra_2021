import pygame
from pygame import *
import os
import sys


WIN_WIDTH = 1200
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


class SecondPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class MainPlatform:
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario Boy")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    running = True

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться (проверка на пересечение с платформой)
    ## entities.add(Персонаж) ТУТ ДОБАВЛЯЕТСЯ ПЕРСОНАЖ

    level = [
        "--------------------------------------",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                      ",
        "                                  ----",
        "              ----                    ",
        "                                      ",
        "                         ----         ",
        "    ---                               ",
        "                                      ",
        "--------------------------------------"]

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()

    screen.blit(bg, (0, 0))
    x = y = 0
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = SecondPlatform(x, y)
                entities.add(pf)
                platforms.append(pf)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
        entities.draw(screen)
        pygame.display.update()




"""
Класс главной платформы игры
"""