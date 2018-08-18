class Component:
    def __init__(self):
        self.enable = True

    def init(self, components):
        self.components = components

    def set_enable(self, enable):
        self.enable = enable

    def apply_effect(self):
        pass