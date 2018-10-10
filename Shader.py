# *****************************************************************************
# * Filename : shader.py
# * Date : 11-Oct-2018
# * Author : Ram
# * Email : ramkalath@gmail.com
# * Breif Description : automatic vertex and fragment shader loading, compiling and linking
# * Detailed Description :
# *****************************************************************************
import glob, os
from OpenGL import GL

class shader:
    def __init__(self, vs_path=None, fs_path=None):
        self.vertex_shader_path = vs_path
        self.fragment_shader_path = fs_path
        self.vs_code = None
        self.fs_code = None
        self.vs = None
        self.fs = None
        self.shaderProgram = None

    def process_shader(self):
        self.vs_code = self.parse_shader(self.vertex_shader_path)
        self.fs_code = self.parse_shader(self.fragment_shader_path)
        self.vs = self.compile_shader(self.vs_code, "vertex")
        self.fs = self.compile_shader(self.fs_code, "fragment")
        self.shaderProgram = self.link_shader(self.vs, self.fs)

    def parse_shader(self, shader_path):
        f = open(shader_path, "r")
        return ''.join(f.readlines())

    def compile_shader(self, s_code, type="vertex"):
        if(type=="vertex"):
            s = GL.glCreateShader(GL.GL_VERTEX_SHADER)
            GL.glShaderSource(s, s_code)
            GL.glCompileShader(s)
            if(GL.glGetShaderiv(s, GL.GL_COMPILE_STATUS) != GL.GL_TRUE):
                print('\x1b[0;37;41m' + "Vertex Shader Compilation Failed" + '\x1b[0m')
                print('\x1b[0;37;41m' + GL.glGetShaderInfoLog(s) + '\x1b[0m')

        elif(type=="fragment"):
            s = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
            GL.glShaderSource(s, s_code)
            GL.glCompileShader(s)
            if(GL.glGetShaderiv(s, GL.GL_COMPILE_STATUS) != GL.GL_TRUE):
                print('\x1b[0;37;41m' + "Fragment Shader Compilation Failed" + '\x1b[0m')
                print('\x1b[0;37;41m' + GL.glGetShaderInfoLog(s) + '\x1b[0m')
        return s

    def link_shader(self, vs, fs):
        shaderProgram = GL.glCreateProgram()
        GL.glAttachShader(shaderProgram, vs)
        GL.glAttachShader(shaderProgram, fs)

        # link, validate and use
        GL.glLinkProgram(shaderProgram)
        if(GL.glGetProgramiv(shaderProgram, GL.GL_LINK_STATUS) != GL.GL_TRUE):
            print('\x1b[0;37;41m' + "Shader Linking Failed" + '\x1b[0m')
            print('\x1b[0;37;41m' + GL.glGetProgramInfoLog(shaderProgram) + '\x1b[0m')

        GL.glValidateProgram(shaderProgram)

        del self.vertex_shader_path
        del self.fragment_shader_path
        del self.vs_code
        del self.fs_code

        return shaderProgram

if __name__ == "__main__":
    s1 = shader("./shaders/vertex_shader.vert", "./shaders/fragment_shader.frag")

