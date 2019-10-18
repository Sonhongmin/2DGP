from pico2d import *

import game_framework

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.check = 0

    def update(self):
        self.image.draw(400, 300)

    def draw(self):
        self.image.draw(400, 300)

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def update():
    pause.update()


def draw():
    clear_canvas()
    pause.draw()
    update_canvas()


