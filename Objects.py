import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Mob_Gumba(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = load_image("Mob_Gumba.png")
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.h
        self.check = 0
        self.xod = 0
        self.coll = 0
        self.traectory = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                          3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                          -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                          -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]
        self.count_mus = 0

    def update(self):
        self.rect.x += -self.traectory[self.xod]
        self.xod += 1
        if self.xod == 68:
            self.xod = 0

    def move(self):
        pass

    def fall(self, hero, shoting, pos):
        pos_m_x, pos_m_y = pos[0], pos[1]
        if not shoting and pygame.sprite.collide_mask(self, hero) and self.rect.y in list(
                range(pos_m_y, pos_m_y + 10)):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            self.check = 1
            self.rect.y += 5
            self.rect.x -= 3

    def check_fall(self):
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):
        return [self.rect.x, self.rect.y, self.coll]

    def again(self):
        pass


class Mob(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.coll, self.count_mus = 0, 0
        self.image = load_image("Mob_Cupa.png")
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -900
        self.rect.y = 506
        self.check = 0
        self.xod = 10

    def move(self):
        self.rect.x += self.xod

    def again(self):
        self.coll, self.count_mus = 0, 0
        self.image = load_image("Mob_Cupa.png")
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = 506
        self.rect.x = -900  # зависит от размера спрайта
        self.check = 0
        self.xod = 10

    def fall(self, hero, shoting, pos):
        pos_m_x, pos_m_y = pos[0], pos[1]
        if not shoting and pygame.sprite.collide_mask(self, hero) and self.rect.y in list(
                range(pos_m_y, pos_m_y + 10)):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            self.check = 1
            self.rect.y += 5
            self.rect.x -= 3

    def check_fall(self):
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):
        return [self.rect.x, self.rect.y, self.coll]


class MobOnBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, *group):  # пока оставлю эти вводимые данным, мб потом еще
        # понадобится что-то из этого
        super().__init__(*group)
        # self.image = load_image("Mob_flower.png")  позже доделаю и этого персонажа
        self.image = load_image("Mob_mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.x = x + width // 2 - 25
        self.rect.y = y + 50
        # self.rect.x = width
        # self.rect.y = height

    def update(self, number):
        kill = ["Mob_mushroom_kill1.png", "Mob_mushroom_kill2.png", "Mob_mushroom_kill3.png", "Mob_mushroom_kill4.png",
                "Mob_mushroom_kill5.png", "Mob_mushroom_kill6.png", "Mob_mushroom_kill7.png", "Mob_mushroom_kill8.png",
                "Mob_mushroom_kill9.png", "Mob_mushroom_kill10.png", "Mob_mushroom_kill11.png",
                "Mob_mushroom_kill12.png", "Mob_mushroom_kill13.png", "Mob_mushroom_kill14.png",
                "Mob_mushroom_kill15.png", "Mob_mushroom_kill16.png", "Mob_mushroom_kill17.png", ]
        self.image = load_image(kill[number])
        self.rect.y += 2


    # def life(self):
    #     self.rect.x = self.rect.x
    #     self.rect.y = self.rect.y


# pygame.init()
# size = width, height = 700, 700
# screen = pygame.display.set_mode(size)
# screen.fill(pygame.Color('black'))
# clock = pygame.time.Clock()
# running = True
#
# all_sprites = pygame.sprite.Group()
# sprite = pygame.sprite.Sprite()
# mob = Mob(all_sprites)
#
# all_sprites2 = pygame.sprite.Group()
# sprite2 = pygame.sprite.Sprite()
# mob_on_box = MobOnBox(300, 200, 30, 30, all_sprites2)  # пример
# mob_on_box2 = MobOnBox(400, 400, 50, 50, all_sprites2)  # пример
# counter = 0
# while running:
#     screen.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     mob.move()
#     mob_on_box2.life()
#     if counter == 2000:
#         counter = 0
#         mob.again()
#     if mob.touch_jump(300, 500):  # Для примера. Позже я хочу сделать так, чтобы из класса платформы передавался
#         # "знак", что моба убили
#         for i in range(180):
#             mob.fall()
#             screen.fill((0, 0, 0))
#             all_sprites.draw(screen)
#             all_sprites2.draw(screen)
#             pygame.display.update()
#             clock.tick(100)
#     if counter == 0:  # Тоже для примера. Позже я хочу сделать так, чтобы из класса платформы передавался
#         # "знак", что моба убили
#         for i in range(17):  # кол-во картинок
#             mob_on_box.update(i)
#             screen.fill((0, 0, 0))
#             all_sprites2.draw(screen)
#             pygame.display.update()
#             clock.tick(15)
#     all_sprites.draw(screen)
#     all_sprites2.draw(screen)
#     counter += 1
#     pygame.display.update()
#     clock.tick(260)
# pygame.quit()

"""
классы объектов
"""
