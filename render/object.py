import numpy as np

from PIL import Image
from OpenGL.GL import *

from maths import *
from render.buffers.vertexarraybuffer import *
from render.buffers.indexbuffer import *
from render.buffers.buffer import *
from components.physicals.gravity import *
from components.physicals.collision import *


class Object:

    def __init__(self, type_, shader, position, vertices, indices, color, tex_coords, texture_path=None):
        self.type = type_
        self.shader = shader
        self.vertices = np.array(vertices, dtype=np.float32)
        self.indices = np.array(indices, dtype=np.uint32)
        self.color = np.array(color, dtype=np.float32)
        self.position = position
        self.size = Vec2(self.vertices[3] - self.vertices[0], self.vertices[10] - self.vertices[1])
        # self.tex_coords = np.array(tex_coords, dtype=np.float32)
        self.components = {}

        # Send VBOs(pos, color, texture coords...etc) in to VAO.
        self.VAO = VertexArrayBuffer()
        self.VBO1 = Buffer(self.vertices)
        self.VBO2 = Buffer(self.color)
        # self.VBO3 = Buffer(self.tex_coords)
        self.IBO = IndexBuffer(self.indices)

        # Set attributes
        self.VAO.add_buffer(0, 3, self.VBO1)
        self.VAO.add_buffer(1, 3, self.VBO2)
        # self.VAO.add_buffer(2, 2, self.VBO3)

        # self.texture = glGenTextures(1)
        # glBindTexture(GL_TEXTURE_2D, self.texture)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # if texture_path:
        #     image = Image.open(texture_path)
        #     width, height= image.size
        #     image = np.array(list(image.getdata()), np.uint8)
        #     glGenerateMipmap(GL_TEXTURE_2D)
        #     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        #     glBindTexture(GL_TEXTURE_2D, 0)

    def physical_effect(self, targets):
        for comp in self.components.values():
            if isinstance(comp, Collision):
                comp.apply_effect(self, targets)
            if isinstance(comp, Gravity):
                comp.apply_effect(self.position, targets)
                # if self.components['collision'].get_first():
                #     print(self.components['collision'].status)

    def render(self, vertex_count):
        self.VAO.bind()
        self.IBO.bind()

        self.shader.setMat4('ml_matrix', Mat4.translation(self.position))
        # glBindTexture(GL_TEXTURE_2D, self.texture);
        glDrawElements(GL_TRIANGLES, vertex_count, GL_UNSIGNED_INT, None)


        self.IBO.unbind()
        self.VAO.unbind()

    def add_component(self, type_, component):
        self.components[type_] = component
        component.init(self.components)