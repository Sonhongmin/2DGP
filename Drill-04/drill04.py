from pico2d import *

def event_handler():
    global direction
    global frame_y
    global x
    global frame_x
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x += 10
                direction = 0
            elif event.key == SDLK_LEFT:
                x -= 10
                direction = 1
            elif event.key == SDLK_SPACE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direction = 2
            elif event.key == SDLK_LEFT:
                direction = 3


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 0
frame_x = 0
frame_y = 100
direction = 2

while running:
    clear_canvas()
    grass.draw(400, 30)
    event_handler()
    character.clip_draw(frame_x * 100, frame_y, 100, 100, x, 90)
    update_canvas()
    frame_x = (frame_x + 1) % 8

    if direction == 0:
        x += 10
        frame_y = 100
    elif direction == 1:
        x -= 10
        frame_y = 0
    elif direction == 2:
        frame_y = 300
    elif direction == 3:
        frame_y = 200

    if 780 < x:
        x = 780
        direction = 0
    elif x < 20:
        x = 20
        direction = 1

    delay(0.01)

close_canvas()