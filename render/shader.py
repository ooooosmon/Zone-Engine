import numpy as np
from OpenGL.GL import *

class Shader:

    def __init__(self, vs, fs):
        self.load(vs, fs)

    def _load_shader_file(self, shader_file):
        shader_source = ""
        with open(shader_file) as f:
            shader_source = f.read()

        return str.encode(shader_source)

    def _compile_shader(self, vs, fs):
        vert_shader_source = self._load_shader_file(vs)
        frag_shader_source = self._load_shader_file(fs)

        self.vert_shader = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(self.vert_shader, vert_shader_source)
        glCompileShader(self.vert_shader)
        success = glGetShaderiv(self.vert_shader, GL_COMPILE_STATUS)
        if not success:
            log = glGetShaderInfoLog(self.vert_shader)
            print('[ERROR] shader.py: Failed to compile vertex shader !\nMore info: {}'.format(log))


        self.frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(self.frag_shader, frag_shader_source)
        glCompileShader(self.frag_shader)
        success = glGetShaderiv(self.frag_shader, GL_COMPILE_STATUS)
        if not success:
            log = glGetShaderInfoLog(self.frag_shader)
            print('[ERROR] shader.py: Failed to compile fragment shader !\nMore info: {}'.format(log))

        self.ID = glCreateProgram()
        glAttachShader(self.ID, self.vert_shader)
        glAttachShader(self.ID, self.frag_shader)
        glLinkProgram(self.ID)

        glDeleteShader(self.vert_shader)
        glDeleteShader(self.frag_shader)

    def load(self, vs, fs):
        return self._compile_shader(vs, fs)

    def setBool(self, name, value):
        glUniform1i(glGetUniformLocation(self.ID, name), int(value))

    def setInt(self, name, value):
        glUniform1i(glGetUniformLocation(self.ID, name), value)

    def setFloat(self, name, value):
        glUniform1f(glGetUniformLocation(self.ID, name), value)

    def setMat4(self, name, matrix):
        glUniformMatrix4fv(glGetUniformLocation(self.ID, name), 1, GL_FALSE, np.array(matrix.elements))

    def setVec3(self, name, vec):
        glUniform3f(glGetUniformLocation(self.ID, name), vec.x, vec.y, vec.z)

    def setVec2(self, name, vec):
        glUniform2f(glGetUniformLocation(self.ID, name), vec.x, vec.y)

    def use(self):
        glUseProgram(self.ID)
