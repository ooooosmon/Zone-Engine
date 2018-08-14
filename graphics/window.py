# @Author: ooooosmon
# @Date: 2018-08-05 16:34:53
# @Last Modified by:   ooooosmon
# @Last Modified time: 2018-08-05 16:34:53

import glfw
from OpenGL.GL import glViewport
from maths.vec2 import *

MSG_FAILED_CREATE_WINDOW = '[ERROR] window.py: Failed to create GLFW window !'

class Window:
    def __init__(self, width, height, title):
        if not glfw.init():
            glfw.terminate()
            return

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.width = width
        self.height = height
        self.title = title
        self.mouse_pos = Vec2(0, 0)

    def create(self):
        self.window = glfw.create_window(self.width, self.height, self.title, None, None)

        if self.window is None:
            print(MSG_FAILED_CREATE_WINDOW)
            glfw.terminate()
            return False

        glfw.make_context_current(self.window)
        glfw.swap_interval(0)
        glfw.set_framebuffer_size_callback(self.window, self._framebuffer_size_callback)
        glfw.set_cursor_pos_callback(self.window, self._get_cursor_position_callback)
        return True

    def loop(self):
        self._handle_input_events()
        glfw.poll_events()
        glfw.swap_buffers(self.window)

    def close(self):
        glfw.terminate()

    def should_close(self):
        return glfw.window_should_close(self.window)

    def get_mouse_position(self):
        return self.mouse_pos

    # Process any input about this window
    def _handle_input_events(self):
        if glfw.get_key(self.window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(self.window, True)

    # Callback functions
    def _framebuffer_size_callback(self, window, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, width, height)

    def _get_cursor_position_callback(self, window, xpos, ypos):
        self.mouse_pos = Vec2(xpos, ypos)
