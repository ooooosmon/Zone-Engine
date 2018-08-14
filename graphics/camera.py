import glfw
from maths.vec3 import *

class Camera:
    def __init__(self, pos=Vec3(), speed=1):
        self.position = pos
        self.speed = speed

    def update(self, window, deltatime):
        self._handle_events(window, deltatime)

    def _handle_events(self, window, deltatime):
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.position.z += self.speed * deltatime
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.position.z -= self.speed * deltatime
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.position.x += self.speed * deltatime
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.position.x -= self.speed * deltatime
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.position.y -= self.speed * deltatime
        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.position.y += self.speed * deltatime
