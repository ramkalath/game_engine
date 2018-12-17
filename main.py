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
import glm

# user defined
import shaders.Shader as sh
import sdl.Sdl_setup as ss


def getLookAtMatrix(_eye, _lookat, _up):
    ez = _eye - _lookat
    ez = ez / np.linalg.norm(ez)
    ex = np.cross(_up, ez)
    ex = ex / np.linalg.norm(ex)
    ey = np.cross(ez, ex)
    ey = ey / np.linalg.norm(ey)

    rmat = np.eye(4)
    rmat[0][0] = ex[0]
    rmat[0][1] = ex[1]
    rmat[0][2] = ex[2]

    rmat[1][0] = ey[0]
    rmat[1][1] = ey[1]
    rmat[1][2] = ey[2]

    rmat[2][0] = ez[0]
    rmat[2][1] = ez[1]
    rmat[2][2] = ez[2]

    tmat = np.eye(4)
    tmat[0][3] = -_eye[0]
    tmat[1][3] = -_eye[1]
    tmat[2][3] = -_eye[2]

    # numpy.array * is element-wise multiplication, use dot()
    lookatmat = np.dot(rmat, tmat).transpose()
    return lookatmat

if __name__ == "__main__":
    width = 800
    height = 600
    window, context = ss.setup(b"Penguin Engine", width, height)
    myshader = sh.shader("./shaders/vertex_shader.vert", "./shaders/fragment_shader.frag")
    myshader.process_shader()

    GL.glEnable(GL.GL_DEPTH_TEST);
    GL.glViewport(0, 0, width, height);
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

    model = np.array([1.0, 0.0, 0.0, 0.0,
                      0.0, np.sin(45), -np.sin(45), 0.0,
                      0.0, np.sin(45),  np.cos(45), 0.0,
                      0.0, 0.0, 0.0, 1.0], dtype='float32')

    view = getLookAtMatrix(np.array([0.0, 0.0, 1.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))

    angle = 45.0;
    n = 0.1
    f = 100.0
    ar = width/height

    projection_perspective = np.array([1/(ar*np.tan(angle/2)), 0, 0, 0,
                                        0, 1/np.tan(angle/2), 0, 0,
                                        0, 0, -(f+n)/(f-n), -2*f*n/(f-n),
                                        0, 0, -1, 0]);

    colorvalues = np.array([1, 0, 1], dtype=np.float32)

    running=True
    while running:
        running = ss.poll_events()

        GL.glClearColor(0.09, 0.105, 0.11, 1.0);
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glUseProgram(myshader.shaderProgram) 

        GL.glUniformMatrix4fv(GL.glGetUniformLocation(myshader.shaderProgram, "model"), 1, GL.GL_FALSE, model) 
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(myshader.shaderProgram, "view"), 1, GL.GL_FALSE, view) 
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(myshader.shaderProgram, "projection"), 1, GL.GL_FALSE, projection_perspective) 
        GL.glUniform3fv(GL.glGetUniformLocation(myshader.shaderProgram, "clr"), 1, colorvalues) 

        GL.glBindVertexArray(VAO)
        GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)
        GL.glDrawElements(GL.GL_TRIANGLES, 36, GL.GL_UNSIGNED_INT, None)
        GL.glBindVertexArray(0)

        sdl2.SDL_GL_SwapWindow(window)
