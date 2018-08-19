from maths import *
from components.component import *

class Gravity(Component):
    def __init__(self, g, s):
        super().__init__()

        self.shift = Vec3(0, 0, 0)
        self.gravity = g
        self.speed = s

    def init(self, parent):
        super().init(parent)

    def apply_effect(self, position, target):
        if not self.enable:
            return

        collision = self.parent.get_component('collision')
        is_collision = collision.get_still(target) or collision.get_first(target)
        states = collision.get_states()

        if CollisionDir.BOTTOM not in states:
            self.shift.y += self.gravity + self.speed

        # print(states)
        # print(self.shift.y)

        if is_collision:
            if collision.get_first(target):
                print('bomb')
                if CollisionDir.BOTTOM in states:
                    self.shift.y = 0

        position += self.shift

    def add_force(self, value):
        self.shift.y += value
