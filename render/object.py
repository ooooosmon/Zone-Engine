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
        self.components = {}

        self.VAO = VertexArrayBuffer()
        self.VBO1 = Buffer(self.vertices)
        self.VBO2 = Buffer(self.color)
        self.IBO = IndexBuffer(self.indices)

        # Set attributes
        self.VAO.add_buffer(0, 3, self.VBO1)
        self.VAO.add_buffer(1, 3, self.VBO2)

    def physical_effect(self, targets):
        for target in targets:
            for comp in self.components.values():
                if isinstance(comp, Collision):
                    comp.apply_effect(self, target)
                    continue
                if isinstance(comp, Gravity):
                    comp.apply_effect(self.position, target)
                    continue

    def render(self, vertex_count):
        self.VAO.bind()
        self.IBO.bind()

        self.shader.setMat4('ml_matrix', Mat4.translation(self.position))
        glDrawElements(GL_TRIANGLES, vertex_count, GL_UNSIGNED_INT, None)

        self.IBO.unbind()
        self.VAO.unbind()

    def add_component(self, type_, component):
        self.components[type_] = component
        component.init(self)

    def get_component(self, component_name):
        return self.components[component_name]

    def get_components(self):
        return self.components