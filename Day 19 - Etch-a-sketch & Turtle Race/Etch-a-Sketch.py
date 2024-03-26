import turtle as t
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(5)

def move_backwards():
    timmy.backward(5)


def counter_clockwise():
    timmy.circle(120,-5)

def clear():
    timmy.reset()
    
def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def pen_up():
    timmy.penup()

def pen_down():
    timmy.pendown()

def undo():
    timmy.undo()

def right_angle():
    timmy.right(90)
    

screen.listen()
screen.onkey(key = "w", fun = move_forwards) 
screen.onkey(key = "s", fun = move_backwards) 
screen.onkey(key = "a", fun = turn_right) 
screen.onkey(key = "d", fun = turn_left)
screen.onkey(key = "c", fun = clear)
screen.onkey(key = "u", fun = pen_up)
screen.onkey(key = "p", fun = pen_down)
screen.onkey(key = "r", fun = right_angle)
screen.onkey(key = "BackSpace", fun = undo)



screen.exitonclick()