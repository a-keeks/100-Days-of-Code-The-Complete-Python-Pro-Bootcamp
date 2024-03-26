# Make Timmy draw a 100x100 square
 
from turtle import Turtle, Screen
screen = Screen()

timmy = Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen.mainloop()