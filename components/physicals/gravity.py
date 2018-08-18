from maths import *
from components.component import *

class Gravity(Component):
    def __init__(self, g, s):
        super().__init__()

        self.shift = Vec3(0, 0, 0)
        self.gravity = g
        self.speed = s

    def init(self, components):
        super().init(components)
        self.collision = self.components['collision']

    def apply_effect(self, position, targets):
        if not self.enable:
            return

        self.shift.y += self.gravity + self.speed

        for target in targets:
            is_collision, status = self.collision.detect(target)

            if is_collision:
                if self.collision.get_first():
                    print('bomb')
                if status is 'BOTTOM':
                    if self.collision.get_still():
                        self.shift.y = 0
            # print(self.shift.y)

        position =  position + self.shift

    def add_force(self, value):
        self.shift.y += value
