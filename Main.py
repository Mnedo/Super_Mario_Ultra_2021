import os
import pygame
import random
import sys

from Main_platform import MainPlatform
from Mark import Mario
from Objects import Mob
from Start import Start, Settings, Info, Match

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

    # позиционировать камеру на объекте target
    def update(self, target):
        if target.rect.x == old:
            self.dx = 0
        else:
            if target.rect.x > old:
                self.dx = -15
            else:
                self.dx = + 15


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


LENTH = 5000
LIFES = 1
WIDTH, HEIGHT = 700, 600
running = True
FPS = 30


def start_screen(LENTH):
    fon = pygame.transform.scale(load_image('start_screen.jpg'), (WIDTH, HEIGHT))
    pygame.init()
    writer = False
    wix = False
    mn1 = []
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Добро пожаловать !')
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    clock = pygame.time.Clock()
    screen.blit(fon, (0, 0))
    all_sp = pygame.sprite.Group()
    msp = pygame.sprite.Group()
    play_but = Start(all_sp)
    inf_but = Info(all_sp)
    set_but = Settings(all_sp)
    mn = [play_but, inf_but, set_but]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                zn = True
                for el in mn:
                    if el.vekt == 3:
                        zn = False
                if zn:
                    for el in mn:
                        x, y = event.pos
                        el.is_on(x, y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_but.click(x, y) and play_but.vekt != 3:
                    for el in mn:
                        el.vekt = 3
                    return LENTH
                elif inf_but.click(x, y):
                    for el in mn:
                        el.vekt = 3
                    writer = True
                elif set_but.click(x, y):
                    for el in mn:
                        el.vekt = 3
                    wix = True
                    for i in range(1, 4):
                        mn1.append(Match(i, LENTH))
                    for el in mn1:
                        el.set_gr(msp)
                c = 0
                for el in mn1:
                    if el.k == 0:
                        c += 1
                if c == 3:
                    for el in mn1:
                        st = el.click(x, y)
                        if st == 'done':
                            el.set_dot()
                            if el.i == 1:
                                LENTH = 5000
                            elif el.i == 2:
                                LENTH = 30000
                            elif el.i == 3:
                                LENTH = 50000
                            for el1 in mn1:
                                if el != el1:
                                    el1.del_dot()
            elif event.type == pygame.KEYDOWN:
                zn = True
                if event.key == pygame.K_ESCAPE:
                    for el in mn:
                        if el.vekt == 3:
                            pass
                        else:
                            zn = False
                    if zn:
                        for el in mn:
                            el.vekt = 0
                    writer = False
                    wix = False
                    for el in mn1:
                        el.clear()
        all_sp.update()
        screen.blit(fon, (0, 0))
        all_sp.draw(screen)
        msp.draw(screen)
        if writer:
            intro_text = ["                                                          Авторы:", "", "",
                          "             Дарья Иващенко       Нарек Абрамян       Михаил Недосекин"]
            font = pygame.font.Font(None, 27)
            text_coord = 222
            for line in intro_text:
                string_rendered = font.render(line, 4, pygame.Color('yellow'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        elif wix:
            intro_text = ["                                            Выберите cложность :", "", "",
                          "                                                                                    Лёгкая",
                          "", "", "", "",
                          "                                                                                    Средняя",
                          "", "", "", "",
                          "                                                                                    Хард"]
            font = pygame.font.Font(None, 27)
            text_coord = 75
            for line in intro_text:
                string_rendered = font.render(line, 1, (100, 0, 0))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        clock.tick(30)


counter = 0
camera = Camera()
while running:
    LENTH = start_screen(LENTH)
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound('death_mob.wav')
    music = pygame.mixer.music.load('fon_music.mp3')
    pygame.mixer.music.play(-1)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Mario ultra 2021')
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    screen.fill(pygame.Color('black'))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    mario_sprites = pygame.sprite.Group()
    earth = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    mob_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite()
    mario = Mario(20, 500, all_sprites)
    mob = Mob(mob_sprites)

    platform = MainPlatform(0, 580, True, LENTH)
    entities.add(platform)
    all_sprites.add(platform)
    bg = 100
    end = 200
    for i in range((LENTH - 100) // 135):
        x = random.randint(bg, end)
        y = random.randint(200, 500)
        platform = MainPlatform(x, y, False, LENTH)
        entities.add(platform)
        all_sprites.add(platform)
        bg += 135
        end += 135
    mario.set_walls(entities)
    mario.set_group(mario_sprites)
    old = 20
    while LIFES != 0:
        camera.update(mario)
        old = mario.rect.x
        for sp in entities:
            camera.apply(sp)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
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
        mob.move()
        counter += 1
        if counter == 1000:
            counter = 0
            mob.again()
        mob.fall(mario, mario.get_coords())
        if mob.check_fall():
            sound.play()
        mob_sprites.update()
        mob_sprites.draw(screen)
        all_sprites.update()
        all_sprites.draw(screen)
        entities.draw(screen)

        clock.tick(30)
        pygame.display.flip()
