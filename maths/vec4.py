class Vec4():
    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        return self

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        self.w -= other.w
        return self

    def multiply(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        self.w *= other.w
        return self

    def devide(self, other):
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
        self.w /= other.w
        return self

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.devide(other)
