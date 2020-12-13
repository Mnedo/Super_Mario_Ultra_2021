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
mario = Mario()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario.jump()
                mario.set_jump()
            if event.key == pygame.K_LEFT:
                mario.x_move('left')
            if event.key == pygame.K_RIGHT:
                mario.x_move('right')
        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            mario.x_moving = False
    screen.fill((0, 0, 0))
    # rendering()
    mario.render(pygame, screen)
    if mario.is_move():
        pass
        # render доски возможно
        clock.tick(18)
    pygame.display.flip()
