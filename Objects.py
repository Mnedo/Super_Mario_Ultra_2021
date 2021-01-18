import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Mob(pygame.sprite.Sprite):  # класс героя(далее - моба), бегающего по нижней платформе и мешающего Марио
    image_run = load_image("Mob_Cupa.png")
    image_run1 = load_image("Mob_Cupa1.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.coll = 0  # счетчик для того, чтобы узнать, соприкоснулись ли Марио и моб
        self.count_mus = 0  # счетчик для музыки
        self.picture = 0  # счетчик для того, чтобы менять спрайты, т.е. создавать ощущение, что моб бежит
        self.image = Mob.image_run
        self.mob_mask = pygame.mask.from_surface(self.image)  # маска спрайта
        self.rect = self.image.get_rect()
        self.rect.x = -900  # начальная позиция
        self.rect.y = 506  # начальная позиция
        self.check = 0  # счетчик для того, чтобы узнать, соприкоснулись ли Марио и моб
        self.killed = False  # переменная для того, чтобы узнать, умер моб или нет
        self.snd = True  # дополнительная переменная для музыки

    def move(self):
        if not self.killed:
            self.rect.x += 10  # ход моба, если он жив

    def again(self):  # обновление моба. Его ход, по сути, представляет собой бег по кругу
        self.coll, self.count_mus = 0, 0
        self.image = Mob.image_run
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = 506
        self.rect.x = -100
        self.check = 0
        self.killed = False

    def fall(self, hero, shoting, pos):
        pos_m_x, pos_m_y = pos[0], pos[1]  # позиция Марио для того, чтобы узнать, соприкоснулись ли Марио и моб
        # по верху, тк в этом случае умирает моб
        if not shoting and pygame.sprite.collide_mask(self, hero) and self.rect.y in list(
                range(pos_m_y, pos_m_y + 50)) and self.rect.x in list(range(pos_m_x - 50, pos_m_x + 50)):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            self.killed = True
            self.check = 1
            self.rect.y += 10
            self.rect.x -= 13

    def check_fall(self):  # проверка, коснулся ли Марио моба по верху
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):  # координаты моба и значение переменной, обозначающее убийство моба
        return [self.rect.x, self.rect.y, self.coll]

    def sound(self):  # для правильной работы музыки
        self.snd = False

    def update(self):  # смена спрайтов
        if self.picture:
            self.image = Mob.image_run1
            self.picture = 0
            self.mob_mask = pygame.mask.from_surface(self.image)
        else:
            self.image = Mob.image_run
            self.picture = 1
            self.mob_mask = pygame.mask.from_surface(self.image)


class MobGumba(pygame.sprite.Sprite):  # класс мобов, которые катаются туда-сюда по главной и "летающим" платформам
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = load_image("Mob_Gumba.png")
        self.mob_mask = pygame.mask.from_surface(self.image)  # то же самое, что и в классе выше
        self.group = groups  # для появления множества мобов в игре
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.h
        self.check = 0
        self.xod = 0
        self.coll = 0
        self.killed = False
        self.traectory = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                          3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                          -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                          -3, -3, -3, -3, -3, -3, -3, -3, -3, -3]  # траектория "езды" мобов
        self.count_mus = 0  # то же самое, что и в классе выше
        self.snd = True  # то же самое, что и в классе выше

    def update(self):  # движение моба по платформе
        if not self.killed:
            self.rect.x += -self.traectory[self.xod]
            self.xod += 1
        if self.xod == 40:
            self.xod = 0

    def move(self):  # нужна для того, чтобы не было ошибки в Main.py
        pass

    def fall(self, hero, shoting, pos):  # тот же принцип и назначение, что и в классе выше
        pos_m_x, pos_m_y = pos[0], pos[1]
        if not shoting and pygame.sprite.collide_mask(self, hero) and self.rect.y in list(
                range(pos_m_y, pos_m_y + 50)) and self.rect.x in list(range(pos_m_x - 50, pos_m_x + 50)):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            self.killed = True
            self.check = 1
            self.rect.y += 9
            if self.rect.y >= 800:  # удаление последнего спрайта на поле, тк он больше не нужен и вернуться к нему нет
                # возможности
                self.remove(self.group)

    def check_fall(self):  # то же самое, что и в классе выше
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):  # то же самое, что и в классе выше
        return [self.rect.x, self.rect.y, self.coll]

    def again(self):  # нужна для того, чтобы не было ошибки в Main.py
        pass

    def sound(self):  # то же самое, что и в классе выше
        self.snd = False


class MobBonus(pygame.sprite.Sprite):  # класс бонуса - сундучка, который дает 200 очков и 1 жизнь
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = load_image("bonus.png")
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.group = groups
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.h
        self.check = 0
        self.xod = 0
        self.coll = 0
        self.killed = False
        self.count_mus = 0
        self.snd = True
        # то же самое, что и в классе выше

    def update(self):  # то же самое, что и в классе выше
        if not self.killed:
            self.xod += 1
        if self.xod == 40:
            self.xod = 0

    def move(self):  # нужна для того, чтобы не было ошибки в Main.py
        pass

    def fall(self, hero, shoting, *args):  # то же самое, что и в классе выше
        if not shoting and pygame.sprite.collide_mask(self, hero):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            self.image = load_image("text_bonus.png")
            self.killed = True
            self.check = 1
            self.rect.y -= 9
            if self.rect.y >= 800:
                self.remove(self.group)

    def check_fall(self):  # то же самое, что и в классе выше
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):  # то же самое, что и в классе выше
        return [self.rect.x, self.rect.y, self.coll]

    def again(self):  # то же самое, что и в классе выше
        pass

    def sound(self):  # то же самое, что и в классе выше
        self.snd = False


class MobMushroom(pygame.sprite.Sprite):  # класс мобов - грибочков, которые стоят на одном месте и при его убийстве
    # "складываются гармошкой"
    image_run = load_image("Mob_mushroom.png")
    kill = ["Mob_mushroom_kill1.png", "Mob_mushroom_kill2.png", "Mob_mushroom_kill3.png", "Mob_mushroom_kill4.png",
            "Mob_mushroom_kill5.png", "Mob_mushroom_kill6.png", "Mob_mushroom_kill7.png", "Mob_mushroom_kill8.png",
            "Mob_mushroom_kill9.png", "Mob_mushroom_kill10.png", "Mob_mushroom_kill11.png",
            "Mob_mushroom_kill12.png", "Mob_mushroom_kill13.png", "Mob_mushroom_kill14.png",
            "Mob_mushroom_kill15.png", "Mob_mushroom_kill16.png", "Mob_mushroom_kill17.png", ]

    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = load_image("Mob_mushroom.png")
        self.mob_mask = pygame.mask.from_surface(self.image)
        self.group = groups
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.h
        self.check = 0
        self.xod = 0
        self.coll = 0
        self.killed = False
        self.count_mus = 0
        self.snd = True
        self.picture = 0
        # то же самое, что и в классе выше

    def update(self):  # то же самое, что и в классе выше
        if not self.killed:
            self.xod += 1
        if self.xod == 40:
            self.xod = 0

    def move(self):  # нужна для того, чтобы не было ошибки в Main.py
        pass

    def fall(self, hero, shoting, pos):  # то же самое, что и в классе выше
        pos_m_x, pos_m_y = pos[0], pos[1]
        if not shoting and pygame.sprite.collide_mask(self, hero) and self.rect.y in list(
                range(pos_m_y, pos_m_y + 50)) and self.rect.x in list(range(pos_m_x - 50, pos_m_x + 50)):
            if self.check == 0:
                self.coll = 1
        if self.coll == 1:
            if self.picture == -1:
                self.image = MobMushroom.image_run
            self.image = load_image(MobMushroom.kill[self.picture])
            self.mob_mask = pygame.mask.from_surface(self.image)
            if self.picture != 17 and self.picture != -1:
                if self.picture == 16:
                    self.rect.y += 3
                else:
                    self.rect.y += 3
            self.picture += 1
            if self.picture == 17:
                self.picture = -1
                self.coll = 0
                self.check = 0
            self.killed = True
            self.check = 1
            if self.rect.y >= 400:
                self.remove(self.group)

    def check_fall(self):  # то же самое, что и в классе выше
        if self.count_mus == 0:
            if self.coll == 1:
                self.count_mus = 1
                return True
        return False

    def get_coords(self):  # то же самое, что и в классе выше
        return [self.rect.x, self.rect.y, self.coll]

    def again(self):  # нужна для того, чтобы не было ошибки в Main.py
        pass

    def sound(self):  # то же самое, что и в классе выше
        self.snd = False


"""
КЛАССЫ ОБЪЕКТОВ
"""