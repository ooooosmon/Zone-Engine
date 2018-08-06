import glfw
from maths.vec3 import *

class Camera:
    def __init__(self, pos=Vec3()):
        self.position = pos

    def update(self, window):
        self._handle_events(window)

    def _handle_events(self, window):
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.position.z += 0.3
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.position.z -= 0.3
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.position.x += 0.3
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.position.x -= 0.3
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.position.y -= 0.3
        if glfw.get_key(window, glfw.KEY_LEFT_CONTROL) == glfw.PRESS:
            self.position.y += 0.3