from OpenGL.GL import *

class IndexBuffer:
    def __init__(self, data):
        self.id = glGenBuffers(1)
        self.bind()
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, data.itemsize * len(data), data, GL_STATIC_DRAW)
        self.unbind()

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.id)

    def unbind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

