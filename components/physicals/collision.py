from maths import *
from components.component import *
import copy

class CollisionDirect():
    NONE    = 'NONE'
    TOP     = 'TOP'
    BOTTOM  = 'BOTTOM'
    LEFT    = 'LEFT'
    RIGHT   = 'RIGHT'


class Collision(Component):
    def __init__(self):
        super().__init__()

        self.enter = False
        self.still = False
        self.leave = False
        self.collision_obj = None

    def init(self, components):
        super().init(components)

    def apply_effect(self, obj, targets):
        if not self.enable: return

        self.position = obj.position
        self.size = obj.size

        for target in targets:
            self.detect(target)

    # def collision_detect(self, target):
    #     self_top = round(self.position.y + self.size.y / 2, 3)
    #     self_bottom = round(self.position.y - self.size.y / 2, 3)
    #     self_left = round(self.position.x - self.size.x / 2, 3)
    #     self_right = round(self.position.x + self.size.x / 2, 3)
    #     target_top = round(target.position.y + target.size.y / 2, 3)
    #     target_bottom = round(target.position.y - target.size.y / 2, 3)
    #     target_left = round(target.position.x - target.size.x / 2, 3)
    #     target_right = round(target.position.x + target.size.x / 2, 3)

    #     # If object has no any collision below condition will true
    #     cond_ho_top    = self_top  < target_bottom > self_bottom
    #     cond_ho_bottom = self_top  > target_top    < self_bottom
    #     cond_vo_left   = self_left > target_right  < self_right
    #     cond_vo_right  = self_left < target_left   > self_right

    #     cond_hi_top    = self_top >= target_bottom >= self_bottom
    #     cond_hi_bottom = self_bottom < target_top < self_top
    #     cond_vi_left   = self_left <= target_right <= self_right or (self_left < target_right > self_right and self_left > target_left < self_right)
    #     cond_vi_right  = self_right > target_left >= self_left or (self_left < target_right > self_right and self_left > target_left < self_right)

    #     if cond_ho_top or cond_ho_bottom or cond_vo_left or cond_vo_right:
    #         # Has no any coliision happen.
    #         return CollisionDirect.NONE
    #     else:
    #         if self_bottom < target_top < self_top and (cond_vi_left or cond_vi_right):
    #             return CollisionDirect.BOTTOM # self bottom
    #         elif self_bottom < target_bottom < self_top and (cond_vi_left or cond_vi_right):
    #             return CollisionDirect.TOP # self top
    #         elif self_left < target_left < self_right and (cond_hi_top or cond_hi_bottom):
    #             return CollisionDirect.RIGHT # self right
    #         elif self_left < target_right < self_right and (cond_hi_top or cond_hi_bottom):
    #             return CollisionDirect.LEFT #self left
    #         else:
    #             return CollisionDirect.NONE
    def collision_detect(self, target):
        self_top = self.position.y + self.size.y / 2
        self_bottom = self.position.y - self.size.y / 2
        self_left = self.position.x - self.size.x / 2
        self_right = self.position.x + self.size.x / 2
        target_top = target.position.y + target.size.y / 2
        target_bottom = target.position.y - target.size.y / 2
        target_left = target.position.x - target.size.x / 2
        target_right = target.position.x + target.size.x / 2

        if abs(target_top - self_bottom) < 0.1:
            self_bottom = target_top

        cond_right  = target_right > self_right > target_left and target_right > self_left < target_left
        cond_left   = target_left < self_left < target_right and target_left < self_right > target_right
        cond_vboth  = target_right > self_left > target_left and target_left < self_right < target_right
        cond_bottom = target_bottom < self_bottom <= target_top and target_bottom <= self_top >= target_top
        cond_top    = target_top > self_top > target_bottom and target_bottom > self_bottom < target_top
        cond_hboth  = target_bottom < self_top < target_top and target_top > self_bottom > target_bottom

        # if not(cond_right) and not(cond_left) and not(cond_top) and not(cond_bottom):
        #     # Has no any coliision happen.
        #     return CollisionDirect.NONE
        # else:
        if cond_right and not(cond_left) and (cond_top or cond_bottom or cond_hboth):
            return CollisionDirect.RIGHT # self right
        if cond_left and not(cond_right) and (cond_top or cond_bottom or cond_hboth):
            return CollisionDirect.LEFT #self left
        if cond_top and not(cond_bottom) and (cond_left or cond_right or cond_vboth):
            return CollisionDirect.TOP # self top
        if cond_bottom and not(cond_top) and (cond_left or cond_right or cond_vboth):
            return CollisionDirect.BOTTOM # self bottom

        return CollisionDirect.NONE

    def detect(self, target):
        if not self.enable:
            return False

        self.status = self.collision_detect(target)
        is_collision = False
        result = is_collision, self.status, self.position

        if self.status is not CollisionDirect.NONE:
            # Has collision happen
            self.leave = False

            if not self.leave and self.enter:
                # The object still trigger collision
                self.still = True
                self.enter = False
            if not self.enter and not self.still and not self.leave:
                # The object is first trigger collision
                self.enter = True

            if self.status is CollisionDirect.LEFT:
                self.position.x = target.position.x + target.size.x / 2 + self.size.x / 2
                # self.position.x += (target.size.x / 2 + self.size.x / 2) - abs(target.position.x - self.position.x)
            if self.status is CollisionDirect.RIGHT:
                self.position.x = target.position.x - target.size.x / 2 - self.size.x / 2
                # self.position.x -= (target.size.x / 2 + self.size.x / 2) - abs(target.position.x - self.position.x)
            if self.status is CollisionDirect.TOP:
                self.position.y = target.position.y - target.size.y / 2 - self.size.y / 2
                # self.position.y -= (target.size.y / 2 + self.size.y / 2) - abs(target.position.y - self.position.y)
            if self.status is CollisionDirect.BOTTOM:
                self.position.y = target.position.y + target.size.y / 2 + self.size.y / 2
                # self.position.y += (target.size.y / 2 + self.size.y / 2) - abs(target.position.y - self.position.y)

            is_collision = True
        else:
            # Has no any collision
            self.leave = True
            self.still = False

            is_collision = False

        self.status = self.collision_detect(target)
        result = (is_collision, self.status)

        return result

    def get_first(self):
        return self.enter
    def get_still(self):
        return self.still
    def get_leave(sefl):
        return self.leave
