# *****************************************************************************
# * Filename : ./1_sdl2_window.py
# * Date : 1-Oct-2018
# * Author : Ram
# * Email : ramkalath@gmail.com
# * Breif Description : penguin engine
# * Detailed Description : Attempt to create a my first game engine called "penguin" engine
# *****************************************************************************

from OpenGL import GL
import sys
import ctypes
import sdl2
import numpy as np

# user defined
import shaders.Shader as sh
import sdl.Sdl_setup as ss


if __name__ == "__main__":
    window, context = ss.setup(b"Penguin Engine", 800, 600)
    myshader = sh.shader("./shaders/vertex_shader.vert", "./shaders/fragment_shader.frag")
    myshader.process_shader()

    #***************************************************************************
    vertices= np.array([
                           -0.5, -0.5,  0.5, 0.0, 0.0,
                            0.5, -0.5,  0.5, 1.0, 0.0,
                           -0.5,  0.5,  0.5, 0.0, 1.0,
                            0.5,  0.5,  0.5, 1.0, 1.0,

                           -0.5, -0.5, -0.5, 0.0, 0.0,
                            0.5, -0.5, -0.5, 1.0, 0.0,
                           -0.5,  0.5, -0.5, 0.0, 1.0,
                            0.5,  0.5, -0.5, 1.0, 1.0,

                           -0.5, -0.5, -0.5, 0.0, 0.0,
                           -0.5, -0.5,  0.5, 1.0, 0.0,
                           -0.5,  0.5, -0.5, 0.0, 1.0,
                           -0.5,  0.5,  0.5, 1.0, 1.0,

                            0.5, -0.5,  0.5, 0.0, 0.0,
                            0.5, -0.5, -0.5, 1.0, 0.0,
                            0.5,  0.5,  0.5, 0.0, 1.0,
                            0.5,  0.5, -0.5, 1.0, 1.0,

                           -0.5, -0.5, -0.5, 0.0, 0.0,
                            0.5, -0.5, -0.5, 1.0, 0.0,
                           -0.5, -0.5,  0.5, 0.0, 1.0,
                            0.5, -0.5,  0.5, 1.0, 1.0,

                           -0.5,  0.5,  0.5, 0.0, 0.0,
                            0.5,  0.5,  0.5, 1.0, 0.0,
                           -0.5,  0.5, -0.5, 0.0, 1.0,
                            0.5,  0.5, -0.5, 1.0, 1.0], dtype='float32')

    indices = np.array([0, 1, 2, 1, 2, 3, 4, 5, 6, 5, 6, 7, 8, 9, 10, 9, 10, 11, 12, 13, 14, 13, 14, 15, 16, 17, 18, 17, 18, 19, 20, 21, 22, 21, 22, 23], dtype='uint32')

    #***************************************************************************
    VAO = GL.glGenVertexArrays(1)
    GL.glBindVertexArray(VAO)

    VBO = GL.glGenBuffers(1) 
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices, GL.GL_STATIC_DRAW)

    EBO = GL.glGenBuffers(1)
    GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, EBO)
    GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, indices, GL.GL_STATIC_DRAW)

    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 5*vertices.itemsize, ctypes.c_void_p(0))
    GL.glEnableVertexAttribArray(0)

    GL.glVertexAttribPointer(1, 2, GL.GL_FLOAT, GL.GL_FALSE, 5*vertices.itemsize, ctypes.c_void_p(3*vertices.itemsize))
    GL.glEnableVertexAttribArray(1)

    GL.glBindVertexArray(0)
    #***************************************************************************
    print(indices.itemsize)

    running=True
    while running:
        running = ss.poll_events()

        GL.glClearColor(0.09, 0.105, 0.11, 1.0);
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glUseProgram(myshader.shaderProgram) 
        GL.glBindVertexArray(VAO)
        GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)
        GL.glDrawElements(GL.GL_TRIANGLES, 36, GL.GL_UNSIGNED_INT, None)
        GL.glBindVertexArray(0)

        sdl2.SDL_GL_SwapWindow(window)
