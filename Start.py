import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Info(pygame.sprite.Sprite):
    image1 = load_image("info.png")
    image2 = load_image("info1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Info.image1
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 222
        self.vekt = 0

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Info.imn
        elif self.vekt == 0:
            self.image = Info.image1
        else:
            self.image = Info.image2


class Settings(pygame.sprite.Sprite):
    image = load_image("settings.png")
    image1 = load_image("settings1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Settings.image
        self.rect = self.image.get_rect()
        self.rect.x = 75
        self.rect.y = 222
        self.vekt = 0

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Settings.imn
        elif self.vekt == 0:
            self.image = Settings.image
        else:
            self.image = Settings.image1


class Start(pygame.sprite.Sprite):
    image = load_image("play.png")
    image1 = load_image("play1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Start.image
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 222
        self.vekt = 0

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Start.imn
        elif self.vekt == 0:
            self.image = Start.image
        else:
            self.image = Start.image1


class Match(pygame.sprite.Sprite):
    image = load_image("match.png")
    imn = load_image("nothing.png")
    image1 = load_image("matched.png")

    def __init__(self, i, ln, *gr):
        super().__init__(gr)
        if ln == 5000 and i == 1:
            self.image = Match.image1
        elif ln == 30000 and i == 2:
            self.image = Match.image1
        elif ln == 50000 and i == 3:
            self.image = Match.image1
        else:
            self.image = Match.image
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 16 + i * 130
        self.i = i
        self.k = 0

    def get_name(self):
        return self.i

    def set_gr(self, gr):
        gr.add(self)

    def clear(self):
        self.image = Match.imn
        self.k = 1

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return 'done'

    def set_dot(self):
        self.image = Match.image1

    def del_dot(self):
        self.image = Match.image


class Reload(pygame.sprite.Sprite):
    image = load_image("reload.png")
    image1 = load_image("reload1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Reload.image
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 400
        self.vekt = 3

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Reload.imn
        elif self.vekt == 0:
            self.image = Reload.image
        else:
            self.image = Reload.image1


class Exit(pygame.sprite.Sprite):
    image = load_image("exit.png")
    image1 = load_image("exit1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Exit.image
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 400
        self.vekt = 3

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Exit.imn
        elif self.vekt == 0:
            self.image = Exit.image
        else:
            self.image = Exit.image1


class Heart(pygame.sprite.Sprite):
    image = load_image("heart.png")

    def __init__(self, x, y, *gr):
        super().__init__(gr)
        self.image = Heart.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Quit(pygame.sprite.Sprite):
    image = load_image("onoff.png")
    image1 = load_image("onoff1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Quit.image
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 475
        self.vekt = 0

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Quit.imn
        elif self.vekt == 0:
            self.image = Quit.image
        else:
            self.image = Quit.image1


class Next(pygame.sprite.Sprite):
    image = load_image("next.png")
    image1 = load_image("next1.png")
    imn = load_image("nothing.png")

    def __init__(self, *gr):
        super().__init__(gr)
        self.image = Next.image
        self.rect = self.image.get_rect()
        self.rect.x = 560
        self.rect.y = 475
        self.vekt = 0

    def is_on(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            self.vekt = 1
        else:
            self.vekt = 0

    def click(self, x, y):
        if x in range(self.rect.x, self.rect.x + self.rect.w + 1) and y in range(self.rect.y,
                                                                                 self.rect.y + self.rect.h + 1):
            return True

    def update(self):
        if self.vekt == 3:
            self.image = Next.imn
        elif self.vekt == 0:
            self.image = Next.image
        else:
            self.image = Next.image1


class Finish(pygame.sprite.Sprite):
    pass
    """
    image = load_image("Tree_fin.png")
    image = pygame.transform.scale(image, (300, 300))

    def __init__(self, x, y, *gr):
        super().__init__(gr)
        self.image = Finish.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    """