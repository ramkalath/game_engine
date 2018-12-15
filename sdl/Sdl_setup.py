import sdl2
import ctypes
''' Handles windowing '''

def setup(title = "SDL window", width = 640, height = 480):
    ''' creates and SDL window and context '''

    if sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING):
        print('\x1b[0;37;41m' + sdl2.SDL_GetError() + '\x1b[0m')
        sdl2.SDL_Quit()

    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 3) 
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 3) 
    sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)

    window = sdl2.SDL_CreateWindow(title,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   width, height,
                                   sdl2.SDL_WINDOW_OPENGL)

    context = sdl2.SDL_GL_CreateContext(window)
    return window, context

def poll_events():
    ''' 1) checks for window quit events '''

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
    window, context = setup()
