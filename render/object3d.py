from render.object import *

class Object3D(Object):

    def __init__(self, shader, position, size, color, texture_path=None):
        self.vertices = [
            -size.x / 2, -size.y / 2,  size.z / 2,
             size.x / 2, -size.y / 2,  size.z / 2,
             size.x / 2,  size.y / 2,  size.z / 2,
            -size.x / 2,  size.y / 2,  size.z / 2,

            -size.x / 2, -size.y / 2, -size.z / 2,
             size.x / 2, -size.y / 2, -size.z / 2,
             size.x / 2,  size.y / 2, -size.z / 2,
            -size.x / 2,  size.y / 2, -size.z / 2,

             size.x / 2, -size.y / 2, -size.z / 2,
             size.x / 2,  size.y / 2, -size.z / 2,
             size.x / 2,  size.y / 2,  size.z / 2,
             size.x / 2, -size.y / 2,  size.z / 2,

            -size.x / 2,  size.y / 2, -size.z / 2,
            -size.x / 2, -size.y / 2, -size.z / 2,
            -size.x / 2, -size.y / 2,  size.z / 2,
            -size.x / 2,  size.y / 2,  size.z / 2,

            -size.x / 2, -size.y / 2, -size.z / 2,
             size.x / 2, -size.y / 2, -size.z / 2,
             size.x / 2, -size.y / 2,  size.z / 2,
            -size.x / 2, -size.y / 2,  size.z / 2,

             size.x / 2,  size.y / 2, -size.z / 2,
            -size.x / 2,  size.y / 2, -size.z / 2,
            -size.x / 2,  size.y / 2,  size.z / 2,
             size.x / 2,  size.y / 2,  size.z / 2,]
        self.color = [
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,

            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,

            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,

            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,

            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,

            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z,
            color.x , color.y, color.z]
        self.indices = [
             0,  1,  2,  2,  3,  0,
             4,  5,  6,  6,  7,  4,
             8,  9, 10, 10, 11,  8,
            12, 13, 14, 14, 15, 12,
            16, 17, 18, 18, 19, 16,
            20, 21, 22, 22, 23, 20]
        self.tex_coords = [
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0]
        super().__init__(shader, position, self.vertices, self.indices, self.color, self.tex_coords, texture_path)

    def render(self):
        super().render(36)