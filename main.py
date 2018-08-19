import numpy as np
import glfw

from OpenGL.GL import *

from maths import *
from graphics.window import *
from graphics.camera import *
from render.object2d import *
from render.object3d import *
from render.shader import *
from components.physicals.gravity import *
from components.physicals.collision import *

WIDTH = 1120
HEIGHT = 630
APP_TITLE = "ZONE"
SHOW_FPS = False

class ObjectType():
    PLAYER = 0
    GROUND = 1
    WALL   = 2

class ZONE:
    def __init__(self):
        self.window = Window(WIDTH, HEIGHT, APP_TITLE)

        # Create window instance.
        if not self.window.create():
            self.window.close()
            return

        self.all_object = {}
        self.walkable_objects = []

    def run(self):
        self.camera = Camera(pos=Vec3(0, 0, 0), speed=3)
        shader2d = Shader('shaders\\basic2d.vert', 'shaders\\basic2d.frag')
        shader2d.use()

        shader2d.setMat4('pr_matrix', Mat4.orthographic(-8.0, 8.0, -4.5, 4.5, -0.1, 100.0))
        shader2d.setVec2('light_pos', Vec2(1, 1))
        shader2d.setVec3('light_color', Vec3(1, 1, 1))
        # shader.setMat4('pr_matrix', Mat4.orthographic(-8.0, 8.0, -4.5, 4.5, -0.1, 100.0))
        # shader.setMat4('pr_matrix', Mat4.perspective(45.0, self.window.width/self.window.height, -0.1, 100.0))
        # shader.setVec2('light_pos', Vec2(1, 1))
        # shader.setVec3('light_color', Vec3(1, 1, 1))
        ground_color = Vec3(1, 1, 1)

        obj_type = ObjectType()
        player  = self.all_object['player'] = Object2D('player', obj_type.PLAYER, shader2d, Vec3(0, 1.5, 0), Vec3(0.5, 1.1, 1), Vec3(81/255, 171/255, 232/255))
        quad1   = self.all_object['quad1']  = Object2D('ground', obj_type.GROUND, shader2d, Vec3(0, 0, 0), Vec3(1, 1, 1), ground_color)
        quad2   = self.all_object['quad 2']  = Object2D('robject', obj_type.WALL, shader2d, Vec3(1, 1, 0), Vec3(1, 1, 1), ground_color)
        quad2   = self.all_object['quad3']  = Object2D('lobject', obj_type.WALL, shader2d, Vec3(-1, 0, 0), Vec3(1, 1, 1), ground_color)

        for item in self.all_object.values():
            if item.type is obj_type.GROUND or item.type is obj_type.WALL:
                self.walkable_objects.append(item)

        player.add_component('collision', Collision())
        player.add_component('gravity', Gravity(0.00001, -0.0001))

        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        timer = 0.0     # for calculate show fps per second
        time = 0.0      # current time
        frames = 0.0    # fps
        while not self.window.should_close():
            deltatime = glfw.get_time() - last_time if 'last_time' in dir() else 0
            last_time = glfw.get_time()

            glClearColor(0.1, 0.1, 0.1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            # self.camera.update(self.window.window, deltatime)
            speed = 0.005
            if glfw.get_key(self.window.window, glfw.KEY_A) == glfw.PRESS:
                player.position.x -= speed
            if glfw.get_key(self.window.window, glfw.KEY_D) == glfw.PRESS:
                player.position.x += speed
            if glfw.get_key(self.window.window, glfw.KEY_SPACE) == glfw.PRESS:
                player.components['gravity'].add_force(0.0003)
            if glfw.get_key(self.window.window, glfw.KEY_Q) == glfw.PRESS:
                player.position = Vec3(0, 2, 0)

            shader2d.setMat4('vw_matrix', Mat4.translation(self.camera.position))

            # mouse_pos = self.window.get_mouse_position()
            # shader.setVec2('light_pos', Vec2(mouse_pos.x * (16.0 / self.window.width), 9.0 - mouse_pos.y * (9.0 / self.window.height)))

            for obj in self.all_object.values():
                obj.physical_effect(self.walkable_objects)
                obj.render()

            def execute_per_second():
                print(player.get_component('collision').get_states())

            self.window.loop()

            # Calculate FPS
            time += deltatime
            frames += 1.0
            if time - timer >= 1.0:
                timer += 1.0
                execute_per_second()
                if SHOW_FPS:
                    print("fps: {}".format(frames))
                frames = 0

        self.window.close()

game = ZONE()
game.run()
