# *****************************************************************************
# * Filename : ./1_sdl2_window.py
# * Date : 1-Oct-2018
# * Author : Ram
# * Email : ramkalath@gmail.com
# * Breif Description : penguin engine
# * Detailed Description : Attempt to create a my first game engine called "penguin" engine
# *****************************************************************************

import sdl2
from OpenGL import GL
import Shader
import numpy as np
import sdl_setup


if __name__ == "__main__":
    window, context = sdl_setup.setup(b"Penguin Engine")
    # yet to add other finger and mouse gestures and feed back onto the main environment. Maybe we can create a separate class for feedback and poll events.

    myshader = Shader.shader("./shaders/vertex_shader.vert", "./shaders/fragment_shader.frag")
    myshader.process_shader()

    #***************************************************************************
    vertices= np.array([-0.5, -0.5, 0.0, 
                         0.5, -0.5, 0.0,
                         0.0,  0.5, 0.0], dtype='float32')

    #***************************************************************************
    VAO = GL.glGenVertexArrays(1)
    VBO = GL.glGenBuffers(1)
    GL.glBindVertexArray(VAO)
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)

    GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices, GL.GL_STATIC_DRAW)
    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)
    GL.glEnableVertexAttribArray(0)

    GL.glBindVertexArray(0)
    #***************************************************************************

    running=True
    while running:
        GL.glClearColor(0.09, 0.105, 0.11, 1.0);
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glUseProgram(myshader.shaderProgram) 
        GL.glBindVertexArray(VAO)
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        GL.glBindVertexArray(0)

        running = sdl_setup.poll_events()
        sdl2.SDL_GL_SwapWindow(window)
