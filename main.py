import numpy as np
import glfw

from OpenGL.GL import *

from maths import *
from graphics.window import *
from graphics.camera import *
from render.object2d import *
from render.object3d import *
from render.shader import *

WIDTH = 1120
HEIGHT = 630
APP_TITLE = "ZONE"

class ZONE:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT, APP_TITLE)

        # Create window instance.
        if not self.window.create():
            self.window.close()
            return

    def loop(self):
        self.camera = Camera(pos=Vec3(0, 0, -3), speed=3)
        shader = Shader('shaders\\basic.vert', 'shaders\\basic.frag')
        shader.use()

        # shader.setMat4('pr_matrix', Mat4.orthographic(0.0, 16.0, 0.0, 9.0, -0.1, 100.0))
        shader.setMat4('pr_matrix', Mat4.perspective(45.0, self.window.width/self.window.height, -0.1, 100.0))
        shader.setVec2('light_pos', Vec2(1, 1))
        shader.setVec3('light_color', Vec3(1, 1, 1))

        # quad1 = Object2D(shader, Vec3(0, 0, 0), Vec3(1, 1, 1), Vec3(1, 0, 1))
        # quad2 = Object2D(shader, Vec3(1, 1, 0), Vec3(1, 1, 1), Vec3(1, 1, 1))
        cube1 = Object3D(shader, Vec3(0, 0, 0), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube2 = Object3D(shader, Vec3(1, 1, -1), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube3 = Object3D(shader, Vec3(2, 2, -2), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube4 = Object3D(shader, Vec3(2, 2, 0), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube5 = Object3D(shader, Vec3(0, 3, 0), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube6 = Object3D(shader, Vec3(5, 5, 0), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')
        cube7 = Object3D(shader, Vec3(3, 3, 0), Vec3(1, 1, 1), Vec3(1, 1, 1), 'res\\container2.png')

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        while not self.window.should_close():
            deltatime = glfw.get_time() - last_time if 'last_time' in dir() else 0
            last_time = glfw.get_time()

            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.camera.update(self.window.window, deltatime)
            shader.setMat4('vw_matrix', Mat4.translation(self.camera.position))

            # mouse_pos = self.window.get_mouse_position()
            # shader.setVec2('light_pos', Vec2(mouse_pos.x * (16.0 / self.window.width), 9.0 - mouse_pos.y * (9.0 / self.window.height)))

            cube1.render()
            cube2.render()
            cube3.render()
            cube4.render()
            cube5.render()
            cube6.render()
            cube7.render()
            # quad1.render()
            # quad2.render()

            self.window.loop()

        self.window.close()

game = ZONE()
game.loop()
