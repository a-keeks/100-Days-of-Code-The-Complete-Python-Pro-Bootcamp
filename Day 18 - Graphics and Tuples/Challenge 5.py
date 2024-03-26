# Draw a spirograph

import turtle as t
from turtle import Turtle, Screen
import random

timmy= Turtle()

t.colormode(255)
def random_colour():
    r = random.randrange(255)
    b = random.randrange(255)
    g = random.randrange(255)
    my_tuple = (r, b, g)
    return my_tuple
random_colour()



def make_circle():
    timmy.color(random_colour())
    timmy.speed("fastest")
    timmy.circle(100)
    timmy.right(10)

for _ in range(100):
    make_circle()


screen = Screen()
screen.mainloop()

