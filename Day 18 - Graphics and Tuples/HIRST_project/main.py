from turtle import Turtle,Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
# screen.bgcolor("black")

colour_list = [(233, 226, 216), (233, 157, 69), (39, 115, 155), (217, 173, 10), (164, 57, 72), (109, 165, 196), 
               (245, 202, 79), (218, 82, 65), (49, 132, 73), (126, 188, 144), (209, 227, 217), (230, 213, 221), 
               (199, 67, 82), (211, 132, 145), (141, 63, 57), (206, 223, 231), (22, 90, 71), (50, 154, 184), 
               (73, 164, 131), (236, 160, 184), (68, 49, 46), (100, 49, 61), (235, 174, 161), (97, 52, 50), 
               (69, 47, 50), (169, 206, 173), (157, 204, 216), (120, 117, 157), (246, 196, 5), (45, 66, 59)]

timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
timmy.goto(-300, -280)
total_dots = 90
each_line = 9
diam_of_dot = 30
steps = 2 * diam_of_dot
lines = total_dots / each_line

def two_lines():
    make_dots()
    turn_right()
    make_dots()
    turn_left()

def make_dots():
    for _ in range(each_line-1):
        timmy.dot(diam_of_dot, random.choice(colour_list))
        timmy.forward(steps)
        timmy.dot(diam_of_dot, random.choice(colour_list))

def turn_right():
    timmy.setheading(90)
    timmy.forward(steps)
    timmy.setheading(180)

def turn_left():
    turn_right()
    timmy.setheading(0)

for line in range(int(lines/2)):
    two_lines()


screen.mainloop()