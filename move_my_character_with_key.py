from pico2d import *
open_canvas()

sp = load_image('sprites.png')
ground = load_image('TUK_GROUND.png')

x = 300
y = 300
framex = 0
framey = 0
running = True
dirX = 0
dirY = 0
space = False

def handle_events():
    global running, dirX, dirY, framey, framex, space

    event = get_events()
    for ev in event:
        if ev.type == SDL_QUIT:
            running = False
        elif ev.type == SDL_KEYDOWN:
            if ev.key == SDLK_ESCAPE:
               running = False
            elif ev.key == SDLK_LEFT:
                dirX = -1
                dirY = 0
                framex = 0
                framey = 3
            elif ev.key == SDLK_RIGHT:
                dirX = 1
                dirY = 0
                framex = 0
                framey = 3
            elif ev.key == SDLK_UP:
                dirY = 1
                dirX = 0
                framex = 2
                framey = 6
            elif ev.key == SDLK_DOWN:
                dirY = -1
                dirX = 0
                framex = 2
                framey = 6
            elif ev.key == SDLK_SPACE:
                space = True
        elif ev.type == SDL_KEYUP:
            if ev.key == SDLK_LEFT:
                dirX = 0
                framex = 0
                framey = 0
            elif ev.key == SDLK_RIGHT:
                dirX = 0
                framex = 0
                framey = 0
            elif ev.key == SDLK_UP:
                dirY = 0
                framex = 0
                framey = 0
            elif ev.key == SDLK_DOWN:
                dirY = 0
                framex = 0
                framey = 0
            elif ev.key == SDLK_SPACE:
                space = False
    pass

while running:
    clear_canvas()
    ground.draw(400, 300)
    if space:
        sp.clip_draw(6 * 64, 2 * 64, 64, 64, x, y, 100, 100)
    elif dirX == -1:
        sp.clip_draw(framex * 64, framey * 64, 64, 64, x, y, 100, 100)
        framex = (framex + 1) % 6
    elif dirX == 1:
        sp.clip_composite_draw(framex * 64, framey * 64, 64, 64, 0, 'h', x, y, 100, 100)
        framex = (framex + 1) % 6
    elif dirY == 1:
        sp.clip_draw(framex * 64, framey * 64, 64, 64, x, y, 100, 100)
        framex = (framex + 1) % 4 + 2
    elif dirY == -1:
        sp.clip_draw(framex * 64, framey * 64, 64, 64, x, y, 100, 100)
        framex = (framex + 1) % 4 + 2
    elif dirX == 0 and dirY == 0:
        sp.clip_draw(framex * 64, framey * 64, 64, 64, x, y, 100, 100)
        framex = (framex + 1) % 4
    update_canvas()
    if framex == 0 and (dirX == 1 or dirX == -1):
        if framey == 4:
            framey = 3
        elif framey == 3:
            framey = 4
    handle_events()
    if space == False:
        x += dirX * 5
        y += dirY * 5
    delay(0.05)

close_canvas()