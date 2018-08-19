from render.object import *
from maths import *

class Object2D(Object):

    def __init__(self, name_, type_, shader, position, size, color, texture_path=None):
        self.name = name_
        self.vertices = [
            -size.x / 2, -size.y / 2, 0.0,
             size.x / 2, -size.y / 2, 0.0,
             size.x / 2,  size.y / 2, 0.0,
            -size.x / 2,  size.y / 2, 0.0]
        self.color = [
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z]
        self.indices = [
            0, 1, 2,
            2, 3, 0]
        self.tex_coords = [
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0]
        super().__init__(type_, shader, position, self.vertices, self.indices, self.color, self.tex_coords, texture_path)

    def render(self):
        super().render(6)