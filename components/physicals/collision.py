from maths import *
from components.component import *
import copy


class ObjectState:
    def __init__(self, target, enter=False, still=False, leave=False):
        self._states = {
            'target': target,
            'states': [],
            'enter': enter,
            'still': still,
            'leave': leave }

    def set_target(self, target):
        self._states['target'] = target
    def set_states(self, states):
        self._states['states'] = states
    def set_enter(self, value):
        self._states['enter'] = value
    def set_still(self, value):
        self._states['still'] = value
    def set_leave(self, value):
        self._states['leave'] = value

    def compare(self, target):
        if target is self.get_target():
            return True
        return False

    def get_target(self):
        return self._states['target']
    def get_states(self):
        return self._states['states']
    def get_enter(self):
        return self._states['enter']
    def get_still(self):
        return self._states['still']
    def get_leave(self):
        return self._states['leave']

class Collision(Component):
    def __init__(self):
        super().__init__()

        self.triggered_objs = []

    def init(self, parent):
        super().init(parent)

    def apply_effect(self, obj, target):
        if not self.enable: return

        self.position = obj.position
        self.size = obj.size
        self.target = None

        self.detect(target)

    def collision_detect(self, target):
        x_distance = abs(self.position.x - target.position.x)
        y_distance = abs(self.position.y - target.position.y)
        x_keep_dis = (self.size.x / 2) + (target.size.x / 2)
        y_keep_dis = (self.size.y / 2) + (target.size.y / 2)
        x_offset = abs((self.size.x / 2 + target.size.x / 2) - abs(self.position.x - target.position.x))
        y_offset = abs((self.size.y / 2 + target.size.y / 2) - abs(self.position.y - target.position.y))
        states = []

        # FIXME: detect collision direction
        def find_direction():
            if self.position.x < target.position.x and abs(x_distance - x_keep_dis) < 0.1:
                # right happen
                states.append(CollisionDir.RIGHT)
            elif self.position.x > target.position.x and abs(x_distance - x_keep_dis) < 0.1:
                # left happen
                states.append(CollisionDir.LEFT)

            if self.position.y < target.position.y and abs(y_distance - y_keep_dis) < 0.1:
                # top happen
                states.append(CollisionDir.TOP)
            elif self.position.y > target.position.y and abs(y_distance - y_keep_dis) < 0.1:
                # bottom happen
                states.append(CollisionDir.BOTTOM)
        def offset_pos():
            for status in states:
                if status is CollisionDir.TOP:
                    self.position.y -= y_offset
                if status is CollisionDir.BOTTOM:
                    self.position.y += y_offset
                if status is CollisionDir.LEFT:
                    self.position.x += x_offset
                if status is CollisionDir.RIGHT:
                    self.position.x -= x_offset

        # 1. Detect has any collision happen
        if x_distance <= x_keep_dis and y_distance <= y_keep_dis:
            # Collision happen
            # 2. Find out collision happen where direction.
            find_direction()
            # 3. Fix up offset
            offset_pos()
        else:
            # Collision no happen
            states.append(CollisionDir.NONE)

        return states

    def detect(self, target):
        states = self.collision_detect(target)
        is_collision = False

        if not self.is_exist_in_triggered_objects(target):
            self.triggered_objs.append(ObjectState(target))
        target_index = self.get_triggered_obj_index(target)

        self.triggered_objs[target_index].set_states(states)

        if states[0] is not CollisionDir.NONE:
            # Has collision happen
            self.triggered_objs[target_index].set_target(target)
            self.triggered_objs[target_index].set_leave(False)

            is_collision = True
        else:
            # Has no any collision
            self.triggered_objs[target_index].set_enter(False)
            self.triggered_objs[target_index].set_still(False)
            self.triggered_objs[target_index].set_leave(True)

            is_collision = False

        # The object still trigger collision
        if self.triggered_objs[target_index].get_enter() and not self.triggered_objs[target_index].get_still() and not self.triggered_objs[target_index].get_leave():
            self.triggered_objs[target_index].set_enter(False)
            self.triggered_objs[target_index].set_still(True)
            self.triggered_objs[target_index].set_leave(False)
        # The object is first trigger collision
        if not self.triggered_objs[target_index].get_enter() and not self.triggered_objs[target_index].get_still() and not self.triggered_objs[target_index].get_leave():
            self.triggered_objs[target_index].set_enter(True)
            self.triggered_objs[target_index].set_still(False)
            self.triggered_objs[target_index].set_leave(False)
        # The object leave trigger
        if self.triggered_objs[target_index].get_leave():
            self.triggered_objs[target_index].set_enter(False)
            self.triggered_objs[target_index].set_still(False)
            self.triggered_objs[target_index].set_leave(True)

        result = (is_collision, states)
        return result

    def get_states(self, target=None):
        if target:
            return self.triggered_objs[self.get_triggered_obj_index(target)]

        states = []
        for elem in self.triggered_objs:
            for state in elem.get_states():
                states.append(state)
        return states
    def get_first(self, target):
        return self.triggered_objs[self.get_triggered_obj_index(target)].get_enter()
    def get_still(self, target):
        return self.triggered_objs[self.get_triggered_obj_index(target)].get_still()
    def get_leave(self, target):
        return self.triggered_objs[self.get_triggered_obj_index(target)].get_leave()

    def is_exist_in_triggered_objects(self, target):
        for elem in self.triggered_objs:
            if elem.compare(target):
                return True
        return False

    def get_triggered_obj_index(self, target):
        for i, elem in enumerate(self.triggered_objs):
            if elem.compare(target):
                return i
        return -1
