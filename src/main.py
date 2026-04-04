from pygame import *

init()

WIGHT, HEIGHT = 800, 600

screen = display.set_mode((WIGHT, HEIGHT))
clock = time.Clock()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill("black")
    display.flip()
    clock.tick()

quit()
