# Make Timmy draw a dashed line

from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.mainloop()