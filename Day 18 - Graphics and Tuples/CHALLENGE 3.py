from turtle import Turtle, Screen
import random
from colours import all_colours_wthout_white

timmy = Turtle()
shape_sides = []

def starting_point():
    timmy.up()
    timmy.backward(75)
    timmy.left(90)
    timmy.forward(200)
    timmy.right(90)
    timmy.down()

for _ in range(7):
    shape_sides.append(_+4)

def draw_shape():
    for sides in shape_sides:
        colour = random.sample(all_colours_wthout_white, sides)
        timmy.color(random.choice(colour))
        for _ in range(sides):
            timmy.forward(100)
            angle = 360/sides
            timmy.right(angle)
    

starting_point()
draw_shape()
        


screen = Screen()
screen.mainloop()

