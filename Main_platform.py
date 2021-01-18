import pygame
from pygame import *


class MainPlatform(sprite.Sprite):
    def __init__(self, x, y, flag, LENTH):
        if LENTH == 5000: # Цвет платформы в зависимости от уровня
            PLATFORM_COLOR = pygame.Color("#8FBC8F")
        elif LENTH == 30000:
            PLATFORM_COLOR = pygame.Color("#87CEEB")
        elif LENTH == 50000:
            PLATFORM_COLOR = pygame.Color("#FF6347")
        if not flag:
            sprite.Sprite.__init__(self)
            if LENTH <= 5000: # Длина платформ в зависимости от уровня
                dl = 350
                # dl = 204
            elif LENTH == 30000:
                dl = 280
            elif LENTH >= 50000:
                dl = 210
            self.image = Surface((dl, 30))
            self.image.fill(Color(PLATFORM_COLOR))
            self.rect = Rect(x, y, dl, 20)
        else:
            sprite.Sprite.__init__(self)
            self.image = Surface((LENTH, 50))
            self.image.fill(Color(PLATFORM_COLOR))
            self.rect = Rect(x, y, LENTH, 30)


"""
Класс главной платформы игры
"""
