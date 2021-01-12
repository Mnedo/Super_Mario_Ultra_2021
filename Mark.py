import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Mario(pygame.sprite.Sprite):
    image_run1_r = load_image("mario_run1_r.png")
    image_run2_r = load_image("mario_run2_r.png")
    image_run1_l = load_image("mario_run1_l.png")
    image_run2_l = load_image("mario_run2_l.png")
    image_jump_r = load_image("mario_jump_r.png")
    image_jump_l = load_image("mario_jump_l.png")
    image_stay_r = load_image("mario_stay_r.png")
    image_stay_l = load_image("mario_stay_l.png")
    image_start = load_image("mario_start.png")
    image_damgel = load_image("damgel.png")
    image_damgel1 = load_image("damge1l.png")
    image_dethl = load_image("image_dethl.png")
    image_damger = load_image("damger.png")
    image_damger1 = load_image("damge1r.png")
    image_dethr = load_image("image_dethr.png")

    def __init__(self, x, y, *gr):
        super().__init__(gr)
        self.image = Mario.image_start
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.jumping = False
        self.moving = False
        self.shoting = False
        self.xod = 0
        self.xod_shot = 0
        self.vekt = 0
        self.gr = []
        self.zn = False
        self.last_res = True
        self.potential = 0
        self.lifes = 0
        self.dash = 0

    def set_walls(self, gr):
        self.gr = gr

    def set_group(self, gr):
        gr.add(self)

    def set_lifes(self, live):
        self.lifes = live

    def update(self):
        if not self.shoting:
            if self.moving:
                self.move_x(self.vekt)
            else:
                if not self.jumping:
                    if self.vekt == -1:
                        self.image = Mario.image_stay_l
                    else:
                        self.image = Mario.image_stay_r
            if not pygame.sprite.spritecollideany(self, self.gr) and self.potential == 0:
                self.jumping = True
                self.y += 15
                self.last_res = True
                if self.vekt == -1:
                    self.image = Mario.image_jump_l
                else:
                    self.image = Mario.image_jump_r
            elif self.potential != 0:
                if self.y >= 0:
                    self.y -= 15
                    self.jumping = True
                    self.potential -= 15
                else:
                    self.potential = 0
                if self.vekt == -1:
                    self.image = Mario.image_jump_l
                else:
                    self.image = Mario.image_jump_r
            else:
                self.jumping = False
                if self.last_res:
                    self.y -= 5
                    self.last_res = False
            self.rect = self.rect.move(self.x - self.rect.x, self.y - self.rect.y)

    def move_x(self, x):
        self.xod += 1
        self.vekt = x
        if x == 1:
            if self.vekt != 0:
                if self.x <= 350:
                    self.x += 8
                    self.dash = 8
                else:
                    self.x += 0
            if self.xod % 2 == 1:
                self.image = Mario.image_run1_r
            else:
                self.image = Mario.image_run2_r
        elif x == -1:
            if self.x - 8 >= 0:
                self.x -= 8
                self.dash = -8
            if self.xod % 2 == 1:
                self.image = Mario.image_run1_l
            else:
                self.image = Mario.image_run2_l

    def set_moving(self):
        if self.moving:
            self.moving = False
            if self.vekt == -1:
                self.image = Mario.image_stay_l
            else:
                self.image = Mario.image_stay_r
        else:
            self.moving = True

    def start_jump(self):
        if self.potential == 0:
            self.potential = 225
        else:
            self.potential = (300 - self.potential)

    def get_coords(self):
        return [self.rect.x, self.rect.y + self.rect.w]

    def damage_mario(self):
        self.xod_shot += 1
        if self.xod_shot >= 20 and self.lifes != 0:
            self.shoting = False
            self.xod_shot = 0
            self.lifes -= 1
        else:
            self.shoting = True
            if self.lifes <= 0:
                if self.vekt == 1:
                    self.image = Mario.image_dethr
                else:
                    self.image = Mario.image_dethl
            else:
                if self.xod_shot % 2 == 1:
                    if self.vekt == 1:
                        self.image = Mario.image_damger
                    else:
                        self.image = Mario.image_damgel
                else:
                    if self.vekt == 1:
                        self.image = Mario.image_damger1
                    else:
                        self.image = Mario.image_damgel1


    def update_lifes(self):
        return self.lifes

    def get_dash(self):
        if self.moving:
            return self.dash
        else:
            return 0


"""
Класс главного персонажа - марио
"""
