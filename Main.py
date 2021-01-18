import os
import pygame
import random
import sys

from Main_platform import MainPlatform
from Mark import Mario
from Objects import Mob, MobGumba, MobBonus, MobMushroom
from Start import Start, Settings, Info, Match, Reload, Exit, Heart, Quit, Next, Finish, Clouds

x_fin = 400


class Camera:  # камера для движения поля
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.dash = 0

    def apply(self, obj):
        obj.rect.x += self.dx

    def update(self, sp):
        self.mario_vekt = sp[0]
        self.mario_x = sp[1]
        if self.mario_x >= 250:
            if self.mario_vekt == 1:
                self.dx = -8
                self.dash = 8
            elif self.mario_vekt == -1:
                self.dx = 8
                self.dash = -8
        else:
            self.dx = 0
            self.dash = mario.get_dash()

    def get_lent(self):
        return self.dash


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


LENTH = 5000
LIFES = 3  # количество жизней
WIDTH, HEIGHT = 700, 600  # размер поля
running = True
FPS = 30
fps_cahnge = 0
wons = 0


def start_screen(LENTH):  # начальный экран + вкладка "авторы" + вкладка "выбор сложности"
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
                elif inf_but.click(x, y) and inf_but.vekt != 3:
                    for el in mn:
                        el.vekt = 3
                    writer = True
                elif set_but.click(x, y) and set_but.vekt != 3:
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
            intro_text = ["                         Авторы:", "", "",
                          "  Михаил Недосекин    Нарек Абрамян      Дарья Иващенко"]
            font = pygame.font.Font('Data/Mario_font.ttf', 12)
            text_coord = 230
            for line in intro_text:
                string_rendered = font.render(line, 4, pygame.Color('yellow'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
            intro_text = ["Press esc to leave"]
            font = pygame.font.Font('Data/Mario_font.ttf', 8)
            text_coord = 230
            for line in intro_text:
                string_rendered = font.render(line, 4, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = HEIGHT - 25
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        elif wix:
            intro_text = ["             Выберите cложность :", "", "",
                          "                            Лёгкая",
                          "", "", "", "", "",
                          "                            Средняя",
                          "", "", "", "", "",
                          "                            Хард"]
            font = pygame.font.Font('Data/Mario_font.ttf', 15)
            text_coord = 75
            for line in intro_text:
                string_rendered = font.render(line, 1, (100, 0, 0))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
            intro_text = ["Press esc to leave"]
            font = pygame.font.Font('Data/Mario_font.ttf', 8)
            text_coord = 230
            for line in intro_text:
                string_rendered = font.render(line, 4, pygame.Color('blue'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = HEIGHT - 25
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        clock.tick(30)


def lost(fps):
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Mario ultra 2021')
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    fps_cahnge = fps
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
            if reload_but.click(x, y) and reload_but.vekt != 3:
                for el in mn:
                    el.vekt = 3
                return 3
            elif exit_but.click(x, y) and exit_but.vekt != 3:
                for el in mn:
                    el.vekt = 3
                print("U just can't win...")
                pygame.quit()
                sys.exit()
    screen.fill((0, 0, 0))
    if LENTH <= 5000:
        screen.blit(load_image("fon_level1.png"), (0, 0))
    elif LENTH == 30000:
        screen.blit(load_image("fon_level2.jpg"), (0, 0))
    elif LENTH >= 50000:
        screen.blit(load_image("fon_level3.png"), (0, 0))
    mob_sprites.draw(screen)
    all_sprites.draw(screen)
    entities.draw(screen)
    if fps_cahnge == 1:
        image_lost = load_image('game_over.png')
        screen.blit(image_lost, (0, 0))
    elif fps_cahnge == 2:
        image_lost1 = load_image('game_over1.png')
        screen.blit(image_lost1, (0, 0))
    elif fps_cahnge == 3:
        image_lost1 = load_image('game_over2.png')
        screen.blit(image_lost1, (0, 0))
    button_end_sprites.update()
    button_end_sprites.draw(screen)
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    clock.tick(10)
    pygame.display.flip()
    return 0


def won(LENTH):
    pygame.init()
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    pygame.mouse.set_visible(True)
    FONT = pygame.font.Font('Data/Mario_font.ttf', 20)
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Mario ultra 2021')
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    buttons = pygame.sprite.Group()
    quit_but = Quit(buttons)
    next_but = Next(buttons)
    mn = [quit_but, next_but]
    while running:
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
                if next_but.click(x, y) and next_but.vekt != 3:
                    for el in mn:
                        el.vekt = 3
                    if LENTH == 5000:
                        LENTH = 30000
                    elif LENTH == 30000:
                        LENTH = 50000
                    elif LENTH == 50000:
                        LENTH = 3 * LENTH
                    return LENTH, 3
                elif quit_but.click(x, y) and quit_but.vekt != 3:
                    for el in mn:
                        el.vekt = 3
                    print("Thank you for the game!")
                    pygame.quit()
                    sys.exit()
        screen.fill((0, 0, 0))
        screen.blit(load_image("Won_screen.png"), (0, 0))
        sound_mario_victory.play()
        pygame.mixer.music.stop()
        font = FONT
        text_coord = 218
        intro_text = ["YOUR SCORE: " + str(round(SCORE))]
        for line in intro_text:
            string_rendered = font.render(line, 4, pygame.Color('gold'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 400
            intro_rect.x = text_coord - (len(str(SCORE)) - 1)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        text_coord = 218
        intro_text = ["BEST SCORE: " + str(round(BEST_SCORE))]
        for line in intro_text:
            string_rendered = font.render(line, 4, pygame.Color('gold'))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 430
            intro_rect.x = text_coord - (len(str(SCORE)) - 1)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        buttons.update()
        buttons.draw(screen)
        clock.tick(10)
        pygame.display.flip()


BEST_SCORE = 0  # счет
SCORE = 0  # счет
while running:  # основной код, где происходит все, что видит пользователь
    pygame.mixer.init()  # музыка
    if BEST_SCORE == 0 or BEST_SCORE <= SCORE:
        BEST_SCORE = SCORE
    image = load_image("mario_start.png")
    pygame.display.set_icon(image)
    # далее музыка для каждого случая
    sound_mob_death = pygame.mixer.Sound('death_mob.wav')
    sound_mario_damage = pygame.mixer.Sound('mario_damage.mp3')
    sound_mario_losing = pygame.mixer.Sound('mario_losing.mp3')
    sound_mario_victory = pygame.mixer.Sound('mario_victory.mp3')
    sound_bonus = pygame.mixer.Sound('mus_bonus.mp3')
    pygame.mixer.music.load('fon_music.mp3')
    der = True
    if LIFES == 0:
        pygame.mouse.set_visible(True)
        if fps_cahnge == 0:
            for el in mn:
                el.vekt = 0
        fps_cahnge += 1
        if fps_cahnge > 3:
            fps_cahnge = 1
        LIFES = lost(fps_cahnge)
        pygame.mixer.music.stop()
    else:
        SCORE = 0
        KOEF = 0.1
        fps_cahnge = 0
        actual_lenth = 0
        if wons == 0:
            LENTH = start_screen(LENTH)
        if LENTH >= 50000:
            LIFES = 1
            KOEF = 0.8
        elif LENTH >= 30000:
            KOEF = 0.4
        elif LENTH >= 80000:
            KOEF = 1
        camera = Camera()
        pygame.init()
        pygame.mouse.set_visible(False)
        FONT = pygame.font.Font('Data/Mario_font.ttf', 15)
        size = WIDTH, HEIGHT
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Mario ultra 2021')
        image = load_image("mario_start.png")
        pygame.display.set_icon(image)
        screen.fill(pygame.Color('black'))
        clock = pygame.time.Clock()
        button_end_sprites = pygame.sprite.Group()
        reload_but = Reload(button_end_sprites)
        exit_but = Exit(button_end_sprites)
        mn = [reload_but, exit_but]
        all_sprites = pygame.sprite.Group()
        mario_sprites = pygame.sprite.Group()
        earth = pygame.sprite.Group()
        entities = pygame.sprite.Group()
        mob_sprites = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        mario = Mario(20, 500, all_sprites)
        mario.potential_life = LIFES
        mob = Mob(mob_sprites)
        platform = MainPlatform(0, 580, True, LENTH)
        entities.add(platform)
        all_sprites.add(platform)
        bg = 100
        end = 305
        counter = 0
        finish = Finish(LENTH - 455, 298, clouds)
        x_cloud = 0
        if LENTH == 50000:
            cloud = False
            z = 330
        else:
            cloud = True
            z = 330
        while x_cloud <= LENTH:
            rrr = Clouds(x_cloud, cloud, clouds)
            x_cloud += z
        if LENTH == 5000:
            while end <= LENTH - 350:
                x = random.randint(bg, end)
                y = 400
                bg = end
                platform = MainPlatform(x, y, False, LENTH)
                entities.add(platform)
                all_sprites.add(platform)
                bg += 360
                end += 780
        elif LENTH == 30000:
            while end <= LENTH - 200:
                x = random.randint(bg, end)
                y = 400
                bg = end
                platform = MainPlatform(x, y, False, LENTH)
                entities.add(platform)
                all_sprites.add(platform)
                bg += 290
                end += 700
        elif LENTH == 50000:
            while end <= LENTH - 200:
                x = random.randint(bg, end)
                y = 370
                bg = end
                platform = MainPlatform(x, y, False, LENTH)
                entities.add(platform)
                all_sprites.add(platform)
                bg += 220
                end += 650
        i = 0
        for ent in entities:  # формирование всех дполнтиельных героев
            i += 1
            x, y = ent.rect.x, ent.rect.y
            if i == 1:
                if LENTH <= 5000:
                    z = 3
                elif LENTH == 30000:
                    z = 16
                elif LENTH >= 50000:
                    z = 30
                rec_len = (LENTH - 600) / z
                for j in range(z):
                    elemental = MobGumba(x + j * rec_len + 350, y, mob_sprites)
            else:
                if i % 5 == 0:
                    elemental = MobGumba(x + 50, y, mob_sprites)
                elif i % 6 == 0:
                    elemental = MobBonus(x + random.randint(0, 30), y, mob_sprites)
                elif i % 11 == 0:
                    elemental = MobMushroom(x + random.randint(10, 60), y + 3, mob_sprites)

        mario.set_walls(entities)
        mario.set_group(mario_sprites)
        mario.set_lifes(LIFES)
        image = load_image("mario_start.png")
        pygame.display.set_icon(image)
        old = 20
        if LIFES != 0:
            pygame.mixer.music.play(-1)
        while LIFES != 0:
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
            if LENTH <= 5000:
                screen.blit(load_image("fon_level1.png"), (0, 0))
            elif LENTH == 30000:
                screen.blit(load_image("fon_level2.jpg"), (0, 0))
            elif LENTH >= 50000:
                screen.blit(load_image("fon_level3.png"), (0, 0))

            LIFES = mario.update_lifes()
            hearts_gp = pygame.sprite.Group()  # новая группа спрайтов
            for i in range(1, LIFES + 1):
                heart = Heart(WIDTH - 40 - i * 40, 10, hearts_gp)
            if mario.moving and not mario.shoting:
                actual_lenth += camera.get_lent()
                if camera.get_lent() >= 0:
                    SCORE += camera.get_lent() * KOEF
            if mario.jumping:
                SCORE += 0.1
            if mario.moving and not mario.shoting:
                camera.update([mario.vekt, mario.x])
                for sp in entities:
                    camera.apply(sp)
                for sp in clouds:
                    camera.apply(sp)
                for sp in mob_sprites:
                    if str(type(sp)) != "<class 'Objects.Mob'>":
                        if not sp.killed:
                            camera.apply(sp)

            if actual_lenth >= LENTH - 500:
                wons += 1
                if BEST_SCORE == 0 or BEST_SCORE <= SCORE:
                    BEST_SCORE = SCORE
                LENTH, LIFES = won(LENTH)
                break
            else:
                for mob in mob_sprites:
                    if mario.shoting and mario.last_sprite != mob:
                        mob.move()
                    else:
                        mob.move()
                        counter += 1
                        if counter >= int(20000 * KOEF) and str(type(mob)) == "<class 'Objects.Mob'>":
                            counter = 0
                            mob.again()
                        mob.fall(mario, mario.shoting, mario.get_coords())
                        if mob.killed and str(type(mob)) != "<class 'Objects.MobBonus'>":
                            if mob.snd:
                                mob.sound()
                                SCORE += 20 * KOEF
                        elif mob.killed and str(type(mob)) == "<class 'Objects.MobBonus'>":
                            if mob.snd:
                                mob.sound()
                                if LIFES != 3:
                                    LIFES += 1
                                    mario.lifes += 1
                                    mario.potential_life += 1
                                    LIFES = mario.update_lifes()
                                SCORE += 200
                        if mario.check_fall(mob) and not mob.killed and not mario.shoting:
                            mario.potential_life = LIFES - 1
                        if mario.potential_life != LIFES:
                            mario.damage_mario()
                            if mario.potential_life == 0:
                                sound_mario_losing.play()
                            else:
                                sound_mario_damage.play()
                            mario.last_sprite = mob
                            break
                        if mob.check_fall():
                            if str(type(mob)) == "<class 'Objects.MobBonus'>":
                                sound_bonus.play()
                            else:
                                sound_mob_death.play()
                clouds.update()
                clouds.draw(screen)
                mob_sprites.update()
                mob_sprites.draw(screen)
                mario_sprites.update()
                mario_sprites.draw(screen)
                hearts_gp.draw(screen)
                entities.draw(screen)
                font = FONT
                text_coord = 614
                intro_text = ["   XP"]
                for line in intro_text:
                    string_rendered = font.render(line, 4, pygame.Color('red'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.top = 18
                    intro_rect.x = text_coord
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)
                text = round(SCORE)
                pr = " " * len(str(text))
                intro_text = [str(text), *pr, "SCORE"]
                for line in intro_text:
                    string_rendered = font.render(line, 4, pygame.Color('gold'))
                    intro_rect = string_rendered.get_rect()
                    intro_rect.top = 51
                    intro_rect.x = text_coord - 30 - len(str(text)) * 15
                    text_coord += intro_rect.height
                    screen.blit(string_rendered, intro_rect)
                clock.tick(30)
                pygame.display.flip()
