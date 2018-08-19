class CollisionDir:
    NONE    = 'NONE'
    TOP     = 'TOP'
    BOTTOM  = 'BOTTOM'
    LEFT    = 'LEFT'
    RIGHT   = 'RIGHT'

class Component:
    def __init__(self):
        self.enable = True

    def init(self, parent):
        self.parent = parent

    def set_enable(self, enable):
        self.enable = enable

    def apply_effect(self):
        pass
