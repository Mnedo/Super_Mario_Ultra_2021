from Mark import Mario
from Main_platform import SecondPlatform
from Objects import MobOnBox, Mob

"""
Код для проверки классов

В дальнейшем рабочий код
"""

import pygame


pygame.init()
size = width, height = 700, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))
running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# mario_sprites = pygame.sprite.Group()

mob_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
mob = Mob(mob_sprites)

earth = pygame.sprite.Group()
entities = pygame.sprite.Group()
mario = Mario(20, 500, all_sprites)
platform = SecondPlatform(0, 576)
entities.add(platform)
mario.set_walls(entities)
counter = 0
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
    mob.move()
    counter += 1
    if counter == 2000:
        counter = 0
        mob.again()
    mob_sprites.update()
    mob_sprites.draw(screen)
    # mob.touch_jump(350, 350) # должны передаваться координаты марио
    # mob.fall()  # потом будет проверять, коснулся ли Марио моба
    all_sprites.update()
    all_sprites.draw(screen)
    entities.draw(screen)
    clock.tick(330)
    pygame.display.flip()
