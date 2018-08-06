from OpenGL.GL import *

class VertexArrayBuffer:
    def __init__(self):
        self.id = glGenVertexArrays(1)

    def add_buffer(self, index, count, buffer):
        self.bind()
        buffer.bind()

        glVertexAttribPointer(index, count, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
        glEnableVertexAttribArray(index)

        buffer.unbind()
        self.unbind()

    def bind(self):
        glBindVertexArray(self.id)

    def unbind(self):
        glBindVertexArray(0)