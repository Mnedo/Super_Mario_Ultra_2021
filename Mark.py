class Mario:
    def __init__(self):
        self.x_pos = 15
        self.y_pos = 500
        self.y_stage = 0
        self.is_jumping = False
        self.moving = False
        self.x_moving = False
        self.vekt = 'pass'
        self.y_pos_jump = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]

    def x_move(self, vekt):
        self.x_moving = True
        self.vekt = vekt
        self.movement(vekt)

    def jump(self):
        self.y_pos -= self.y_pos_jump[self.y_stage]
        self.y_stage += 1
        if self.y_stage == len(self.y_pos_jump):
            self.y_stage = 0
            self.is_jumping = False

    def movement(self, vekt):
        if self.is_jumping:
            self.jump()
            self.moving = True
        if vekt == 'left':
            if self.x_pos - 20 >= 0:
                self.x_pos -= 20
                self.moving = True
        elif vekt == 'right':
            if self.x_pos + 20 <= 550:
                self.x_pos += 20
                self.moving = True

    def render(self, pygame, screen):
        self.movement('pass')
        if self.x_moving:
            self.movement(self.vekt)
        pygame.draw.circle(screen, (255, 0, 0), (self.x_pos, self.y_pos), 20)

    def is_move(self):
        if self.moving:
            self.moving = False
            return True

    def set_jump(self):
        self.is_jumping = True


"""
Класс главного персонажа - марио
"""
