import pygame
from pygame import *
import os
import sys

WIN_WIDTH = 1300
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

PLATFORM_WIDTH = 3000
PLATFORM_HEIGHT = 30
PLATFORM_COLOR = pygame.Color("Green")


class SecondPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

"""
class MainPlatform:
    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Mario - MishaDashaNarekEdition")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    BACKGROUND_COLOR = load_image("Фон.png")
    bg.blit(BACKGROUND_COLOR, (0, 0))
    running = True

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться (проверка на пересечение с платформой)
    ## entities.add(Персонаж) ТУТ ДОБАВЛЯЕТСЯ ПЕРСОНАЖ


    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()

    screen.blit(bg, (0, 0))
    x = y = 0
    for row in range(PLATFORM_WIDTH):  # вся строка
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

"""
Класс главной платформы игры
"""
