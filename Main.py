from Mark import Mario
from Main_platform import Main_platform, Second_platform
from Objects import Box, Mob

"""
Код для проверки классов

В дальнейшем рабочий код
"""

import pygame

pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))
running = True
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mario_sprites = pygame.sprite.Group()
earth = pygame.sprite.Group()
mario = Mario(20, 550, all_sprites)
mario.set_walls(earth)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario.start_jump()
                #mario.set_moving()
            elif event.key == pygame.K_LEFT:
                if not mario.jumping:
                    mario.vekt = -1
                    mario.set_moving()
            elif event.key == pygame.K_RIGHT:
                if not mario.jumping:
                    mario.vekt = 1
                    mario.set_moving()
            elif event.key == pygame.K_DOWN:
                if mario.jumping:
                    mario.zn = True
        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            if mario.moving:
                mario.set_moving()

    screen.fill((0, 0, 0))
    #if mario.have_to_move_earth(width):
    #   render platfrmm
    all_sprites.update()
    all_sprites.draw(screen)

    clock.tick(30)
    pygame.display.flip()
