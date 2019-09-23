from pico2d import *
import math
x = 400
y = 90
dir = 0

def squre_move():
    global x, y, dir
    while True:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
        if x >= 780 and y <= 90:
            dir = 1
        elif y >= 560 and x >= 780:
            dir = 2
        elif x <= 20 and y >= 560:
            dir = 3
        elif y <= 90 and x <= 20:
            dir = 0

        if dir == 0:
            x += 4
        elif dir == 1:
            y += 4
        elif dir == 2:
            x -= 4
        elif dir == 3:
            y -= 4

        if x == 396 and y <= 90:
            x = 400
            return
def circle_move():
    r = 200
    radian = 0
    while True:
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = math.sin(radian / 360 * 2 * math.pi) * r
        y = math.cos(radian / 360 * 2 * math.pi) * r
        character.draw_now(x + 400, y + 300)
        delay(0.1)
        radian += 15
        if radian == 375:
            return


# fill here

if __name__=="__main__":
    open_canvas()

    grass = load_image('grass.png')
    character = load_image('character.png')

    while True:
        squre_move()
        circle_move()


    close_canvas()