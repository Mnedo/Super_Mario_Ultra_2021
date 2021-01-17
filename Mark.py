import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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
        self.killed = False
        self.xod = 0
        self.xod_shot = 0
        self.vekt = 0
        self.gr = []
        self.zn = False
        self.last_res = True
        self.potential = 0
        self.potential_life = 0
        self.lifes = 0
        self.dash = 0
        self.mn = [400, 580]
        self.damage = [-15, -20, -20, -20, -20, -15, -15, -10, -10, -10, 15, 20, 20, 20, 20, 15, 15, 10, 0, 0]
        self.damage_x = [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 0, 0, 0, 0, 0, 0, 0, 0]
        self.last_sprite = 0

    def set_walls(self, gr):
        self.gr = gr

    def set_group(self, gr):
        gr.add(self)

    def set_lifes(self, live):
        self.lifes = live

    def update(self):
        if not self.shoting and not self.killed:
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
                if self.y + 56 <= self.mn[0] or (self.y >= self.mn[0] + 20 and self.y + 56 <= self.mn[1]):
                    self.jumping = False
                    if self.last_res:
                        self.y -= 5
                        self.last_res = False
                else:
                    self.jumping = True
                    self.y += 15
                    self.last_res = True
                    if self.vekt == -1:
                        self.image = Mario.image_jump_l
                    else:
                        self.image = Mario.image_jump_r
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
        if pygame.sprite.spritecollideany(self, self.gr):
            if self.potential == 0:
                self.potential = 225
                # self.potential = 150
            else:
                self.potential = 120

    def get_coords(self):
        return [self.rect.x, self.rect.y + self.rect.w]

    def damage_mario(self):
        self.xod_shot += 1
        if self.xod_shot >= 20 and self.lifes != 0:
            self.shoting = False
            self.xod_shot = 0
            if self.y >= 500:
                self.y = 500
            self.lifes -= 1
            if self.lifes <= 0:
                self.killed = True
                if self.vekt == 1:
                    self.image = Mario.image_dethr
                else:
                    self.image = Mario.image_dethl
        else:
            self.shoting = True
            if self.lifes <= 0:
                self.killed = True
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
            self.rect.y -= -self.damage[self.xod_shot]
            if self.vekt == -1:
                self.rect.x -= self.damage_x[self.xod_shot]
            elif self.vekt == 1:
                self.rect.x -= -self.damage_x[self.xod_shot]
            self.x = self.rect.x
            self.y = self.rect.y

    def update_lifes(self):
        return self.lifes

    def get_dash(self):
        if self.moving:
            return self.dash
        else:
            return 0

    def fall(self, mob, pos):
        # self.check, self.coll = 0, 0
        pos_m_x, pos_m_y, m_coll = pos[0], pos[1], pos[2]
        if m_coll == 0 and pygame.sprite.collide_mask(self, mob) and self.damage == 0:
            self.coll = 1

    def check_fall(self, mob):
        if pygame.sprite.collide_mask(self, mob):
            return True
        return False

    def return_shot(self):
        return self.shoting

    def if_kill(self):
        self.damage = 0


"""
Класс главного персонажа - марио
"""
