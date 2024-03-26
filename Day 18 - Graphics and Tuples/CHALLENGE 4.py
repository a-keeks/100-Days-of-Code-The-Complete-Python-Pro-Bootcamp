# Draw a random walk

import turtle as t
from turtle import Turtle, Screen
import random
from colours import all_colours_wthout_white as wthout_white

timmy = Turtle()
screen = Screen()

t.colormode(255)
def random_colour():
    r = random.randrange(255)
    b = random.randrange(255)
    g = random.randrange(255)
    my_tuple = (r, b, g)
    return my_tuple
random_colour()

steps = 100
movements = ["forward", "backward"]
directions = [90, 180, 270, 360]


def random_walk():
    timmy.pensize(15)
    movement = random.choice(movements)
    direction = random.choice(directions)
    speed = "fastest"
    timmy.right(direction)
    if movement == "forward":
        timmy.forward(steps)
    elif movement == "backward":
        timmy.backward(steps)


    timmy.speed(speed)
    timmy.pencolor(random_colour())


for i in range(200):
    random_walk()

screen.mainloop()


