
import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")


def draw():
    screen.clear()
    screen.fill("light blue")
    apple.draw()
    orange.draw()
    pineapple.draw()


def place_apple():
    apple.x = randint(10, 300)
    apple.y = randint(10, 200)


def place_orange():
    orange.x = randint(90, 600)
    orange.y = randint(90, 400)


def place_pineapple():
    pineapple.x = randint(110, 800)
    pineapple.y = randint(100, 300)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shoot")
        place_apple()
    if pineapple.collidepoint(pos):
        print("Goode shoot")
        place_pineapple()
    if orange.collidepoint(pos):
        print("Goode shoot")
        place_orange()
    else:
        print("Missed")

pgzrun.go()
