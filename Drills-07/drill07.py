import random

from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        self.image = load_image('ball21x21.png')
        self.distance = random.randint(5, 20)
        self.type = 0

    def update(self):
        self.y -= self.distance
        if self.y <= 60:
            self.y = 60
            self.distance = 0

    def draw(self):
        self.image.draw(self.x, self.y, 21, 21)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 7)
        self.distance = random.randint(5, 20)
        self.image = load_image('ball41x41.png')
        self.type = 1

    def update(self):
        self.y -= self.distance
        if self.y <= 70:
            self.y = 70
            self.distance = 0

    def draw(self):
        self.image.draw(self.x, self.y, 41, 41)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
grass = Grass()
running = True
team = [Boy() for i in range(11)]
balls = []
i = 0

for _ in range(20):
    temp = random.randint(0, 1)
    if temp == 0:
        balls.append(SmallBall())
    else:
        balls.append(BigBall())

while running:
    handle_events()

    for ball in balls:
        ball.update()
    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)

close_canvas()