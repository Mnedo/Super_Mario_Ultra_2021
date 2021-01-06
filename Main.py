from Mark import Mario
from Main_platform import SecondPlatform
# from Objects import MobOnBox, Mob

"""
Код для проверки классов

В дальнейшем рабочий код
"""


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x)
        self.dy = -(target.rect.y)

import pygame


pygame.init()
size = width, height = 700, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mario_sprites = pygame.sprite.Group()
earth = pygame.sprite.Group()
entities = pygame.sprite.Group()
mario = Mario(20, 500, all_sprites)
camera = Camera()
platform = SecondPlatform(0, 576)
entities.add(platform)
mario.set_walls(entities)
mario.set_group(mario_sprites)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario.start_jump()
            elif event.key == pygame.K_LEFT:
                mario.vekt = -1
                mario.set_moving()
            elif event.key == pygame.K_RIGHT:
                mario.vekt = 1
                mario.set_moving()
            elif event.key == 1073742048:
                mario.potential = 0
        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            if mario.moving:
                mario.set_moving()

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    entities.draw(screen)

    clock.tick(30)
    pygame.display.flip()
