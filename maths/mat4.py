import math

class Mat4:
    def __init__(self, diagonal=0.0):
        # the struct of elements like below:
        # 0  0  0  0
        # 0  0  0  0
        # 0  0  0  0
        # 0  0  0  0
        self.elements = []

        for _ in range(4 * 4):
            self.elements.append(0.0)

        self.elements[0 + 0 * 4] = diagonal
        self.elements[1 + 1 * 4] = diagonal
        self.elements[2 + 2 * 4] = diagonal
        self.elements[3 + 3 * 4] = diagonal

    @staticmethod
    def identity():
        return Mat4(1.0)

    def multiply(self, other):
        for y in range(4):
            for x in range(4):
                sum = 0.0
                for e in range(4):
                    sum += self.elements[x + e * 4] * other.elements[e + y * 4]
                self.elements[x + y * 4] = sum
        return self

    def __mul__(self, other):
        return self.multiply(other)

    @staticmethod
    def orthographic(left, right, bottom, top, near, far):
        result = Mat4(1.0)

        # v1  0  0  0
		#  0 v2  0  0
		#  0  0 v3  0
		#  0  0  0  1
		# v1 is elements[0 + 0 * 4]
		# v2 is elements[1 + 1 * 4]
		# v3 is elements[2 + 2 * 4]
        result.elements[0 + 0 * 4] = 2.0 / (right - left)
        result.elements[1 + 1 * 4] = 2.0 / (top - bottom)
        result.elements[2 + 2 * 4] = 2.0 / (near - far)

        # v1  0  0 v4
        #  0 v2  0 v5
        #  0  0 v3 v6
        #  0  0  0  1
        # v4 is elements[0 + 3 * 4]
        # v5 is elements[1 + 3 * 4]
        # v6 is elements[2 + 3 * 4]
        result.elements[0 + 3 * 4] = (left + right) / (left - right)
        result.elements[1 + 3 * 4] = (bottom + top) / (bottom - top)
        result.elements[2 + 3 * 4] = (far + near) / (far - near)

        return result

    @staticmethod
    def perspective(fov, aspect_ratio, near, far):
        result = Mat4(1.0)

        q = 1.0 / math.tan(math.radians(0.5 * fov))
        a = q / aspect_ratio
        b = (near + far) / (near - far)
        c = (2.0 * near * far) / (near - far)

        # v1  0  0  0
        #  0 v2  0  0
        #  0  0 v3 v5
        #  0  0 v4  1
		# v1 is elements[0 + 0 * 4]
		# v2 is elements[1 + 1 * 4]
		# v3 is elements[2 + 2 * 4]
		# v4 is elements[3 + 2 * 4]
		# v5 is elements[2 + 3 * 4]
        result.elements[0 + 0 * 4] = a
        result.elements[1 + 1 * 4] = q
        result.elements[2 + 2 * 4] = b
        result.elements[3 + 2 * 4] = -1.0
        result.elements[2 + 3 * 4] = c

        return result

    @staticmethod
    def translation(translation):
        result = Mat4(1.0)

        # 1  0  0  x
        # 0  1  0  y
        # 0  0  1  z
        # 0  0  0  1
        # x is elements[0 + 3 * 4]
        # y is elements[1 + 3 * 4]
        # z is elements[2 + 3 * 4]
        result.elements[0 + 3 * 4] = translation.x
        result.elements[1 + 3 * 4] = translation.y
        result.elements[2 + 3 * 4] = translation.z

        return result

    @staticmethod
    def rotation(angle, axis):
        result = Mat4(1.0)

        r = math.radians(angle)
        c = math.cos(r)
        s = math.sin(r)
        omc = 1.0 - c

        x = axis.x
        y = axis.y
        z = axis.z

        result.elements[0 + 0 * 4] = x * omc + c
        result.elements[1 + 0 * 4] = y * x * omc + z * s
        result.elements[2 + 0 * 4] = x * z * omc - y * s

        result.elements[0 + 1 * 4] = x * y * omc - z * s
        result.elements[1 + 1 * 4] = y * omc + c
        result.elements[2 + 1 * 4] = y * z * omc + x * s

        result.elements[0 + 2 * 4] = x * z * omc + y * s
        result.elements[1 + 2 * 4] = y * z * omc - x * s
        result.elements[2 + 2 * 4] = z * omc + c

        return result

    @staticmethod
    def scale(scale):
        result = Mat4(1.0)

        result.elements[0 + 0 * 4] = scale.x
        result.elements[1 + 1 * 4] = scale.y
        result.elements[2 + 2 * 4] = scale.z
        # v1  0  0  0 ]
        #  0 v2  0  0 ]
        #  0  0 v3  0 ]
        #  0  0  0  1 ]
        # v1 is elements[0 + 0 * 4]
        # v2 is elements[1 + 1 * 4]
        # v3 is elements[2 + 2 * 4]

        return result
