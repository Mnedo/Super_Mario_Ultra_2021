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

    def __init__(self, x, y, *gr):
        super().__init__(gr)
        self.image = Mario.image_start
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.jumping = False
        self.moving = False
        self.xod = 0
        self.vekt = 0
        self.y_jump = 0
        self.k_jump = 0
        self.gr = []
        self.zn = False

    def set_walls(self, *gr):
        self.gr = gr

    def update(self):
        if self.jumping:
            self.jump()
            if self.vekt == 1:
                if self.x + 6 <= 600:
                    self.x += 6
            elif self.vekt == -1:
                if self.x - 6 >= 0:
                    self.x -= 6
        elif self.moving:
            self.move_x(self.vekt)
        self.rect = self.rect.move(self.x - self.rect.x, self.y - self.rect.y)

    def have_to_move_earth(self, witdh):
        if self.x >= witdh - 100:
            return True
        else:
            return False

    def move_x(self, x):
        self.xod += 1
        self.vekt = x
        if x == 1:
            if self.vekt != 0:
                if self.x + 7 <= 540:
                    self.x += 7
            if self.xod % 2 == 1:
                self.image = Mario.image_run1_r
            else:
                self.image = Mario.image_run2_r
        elif x == -1:
            if self.x - 7 >= 0:
                self.x -= 7
            if self.xod % 2 == 1:
                self.image = Mario.image_run1_l
            else:
                self.image = Mario.image_run2_l

    def jump(self):
        if self.y_jump - 180 <= self.y and self.k_jump == 1 and self.y - 10 >= 0 and not self.zn:
            self.y -= 15
            if self.vekt == -1:
                self.image = Mario.image_jump_l
            else:
                self.image = Mario.image_jump_r
        else:
            self.k_jump = 0
            if self.y <= self.y_jump and not pygame.sprite.spritecollideany(self, self.gr):
                if self.y + 15 <= 530:
                    self.y += 15
                    if self.vekt == -1:
                        self.image = Mario.image_jump_l
                    else:
                        self.image = Mario.image_jump_r
                else:
                    self.zn = False
                    self.jumping = False
                    # self.moving = False
                    if self.vekt == -1:
                        self.image = Mario.image_stay_l
                    else:
                        self.image = Mario.image_stay_r

            else:
                self.zn = False
                self.jumping = False
                #self.moving = False
                if self.vekt == -1:
                    self.image = Mario.image_stay_l
                else:
                    self.image = Mario.image_stay_r

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
        self.y_jump = self.y
        self.y -= 5
        if not self.moving:
            self.vekt = 0
        self.k_jump = 1
        self.jumping = True

    def clear(self):
        self.xod = 0
        if self.vekt == 1:
            self.image = Mario.image_stay_r
        elif self.vekt == -1:
            self.image = Mario.image_stay_l
        self.jumping = False


"""
Класс главного персонажа - марио
"""
