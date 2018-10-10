# *****************************************************************************
# * Filename : ./1_sdl2_window.py
# * Date : 1-Oct-2018
# * Author : Ram
# * Email : ramkalath@gmail.com
# * Breif Description : sld window
# * Detailed Description : learning sdl
# *****************************************************************************

import ctypes
import sdl2
from OpenGL import GL
from OpenGL.arrays import vbo
import numpy as np
import Shader

def sdl_poll_events():
    event = sdl2.SDL_Event()
    if sdl2.SDL_PollEvent(ctypes.byref(event)):
        # check for escape key press
        if (event.type == sdl2.SDL_KEYDOWN and event.key.keysym.sym == sdl2.SDLK_ESCAPE):
            return False
        # check for other forms of quit
        if (event.type == sdl2.SDL_QUIT):
            return False
    return True

if __name__ == "__main__":
    window_width = 640
    window_height = 480

    if sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING):
        print sdl2.SDL_GetError()
        sdl2.SDL_Quit()

    # sdl2 set context properties
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3) 
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3) 
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)

    # create a window
    window = sdl2.SDL_CreateWindow("python sdl2 window",
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   640, 480,
                                   sdl2.SDL_WINDOW_OPENGL)

    context = sdl2.SDL_GL_CreateContext(window)
    
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

        running = sdl_poll_events()
        sdl2.SDL_GL_SwapWindow(window)
