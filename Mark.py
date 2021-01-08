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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.jumping = False
        self.moving = False
        self.xod = 0
        self.vekt = 0
        self.gr = []
        self.zn = False
        self.last_res = True
        self.potential = 0

    def set_walls(self, gr):
        self.gr = gr

    def set_group(self, gr):
        gr.add(self)

    def update(self):
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
            self.y -= 15
            self.jumping = True
            self.potential -= 15
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
                self.x += 8
            if self.xod % 2 == 1:
                self.image = Mario.image_run1_r
            else:
                self.image = Mario.image_run2_r
        elif x == -1:
            if self.x - 8 >= 0:
                self.x -= 8
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
        self.potential = 225

    def get_coords(self):
        return [self.rect.x, self.rect.y + self.rect.w]


"""
Класс главного персонажа - марио
"""
