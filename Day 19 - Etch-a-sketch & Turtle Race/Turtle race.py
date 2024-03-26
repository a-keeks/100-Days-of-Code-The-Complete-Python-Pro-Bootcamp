import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400) # resets the screen wisth and height
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


turtle_colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def build_turtle(color):
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    t.penup()
    return t

all_turtles = []
def start():
    lap_tracks()
    for colour in turtle_colours:
        all_turtles.append(build_turtle(colour))
        for i in range(len(all_turtles)):
            ycoord = 120 - (40 * i)
            all_turtles[i].goto(-200, ycoord)

            


def movement():
    for move in range(100):
        for t in all_turtles:
            t.forward(random.random()*10)

def lap_tracks():
    lap = Turtle()
    lap.ht()
    lap.penup()
    lap.speed(0)
    for i in range(15):
        xcoord = -180 + (25*i)
        lap.goto(xcoord , 155)
        lap.write(f"{i}", move = False, align = "center")
        lap.setheading(0)
        lap.bk(2)
        lap.setheading(270)

        for _ in range(16):
            lap.speed(0)
            lap.fd(10)
            lap.pendown()
            lap.fd(10)
            lap.penup()
    

if user_bet:
    is_race_on = True

while is_race_on:
    start()


    go = Turtle()
    start_race = 'go.gif'
    turtle.register_shape(start_race)
    go.shape(start_race)
    go.hideturtle()

    for colour in all_turtles:
        if colour.xcor() >= 148:

            finished = Turtle()
            race_over = 'finish.gif'
            turtle.register_shape(race_over)
            finished.shape(race_over)
                        
            is_race_on = False
            winning_colour = colour.pencolor()
            if user_bet == winning_colour:
                print(f"You Win! The {winning_colour} turtle is the winner!") 
            else:
                print(f"You Lose! The {winning_colour} turtle is the winner!")
        movement()       


screen.mainloop()