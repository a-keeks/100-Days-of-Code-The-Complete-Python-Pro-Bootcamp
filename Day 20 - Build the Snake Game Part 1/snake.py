from turtle import Turtle, Screen
STEPS = 20


import random

class Snake(): 
    def __init__(self): 
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("green")
            snake.penup()
            snake.goto(-20*i,0)
            self.snakes.append(snake)

    
    def move(self):
        for snake in range(len(self.snakes)-1, 0, -1): #range(starts, stops, step) ## going from the last segm. to the first so range is last index of list to 0
            new_x = self.snakes[snake-1].xcor() # finds x coord....
            new_y = self.snakes[snake-1].ycor() # ... and y coord of prev. segment
            self.snakes[snake].goto(new_x, new_y) # moves each segm. into place of prev. segment
        self.head.fd(20)

    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)



class Food():

    def __init__(self): 
        self.generate_food()


    def generate_food(self):
        food = Turtle("square")
        food.ht()
        food.color("red")
        food.st()

        food.teleport(random.randrange(-300, 300, 20), random.randrange(-250, 250, 20)) #food goes to random x, y coordinates

# class Scoreboard():
#      def __init__(self):
#          scoreboard = 0 
        
        
#      def score(self):
#         score = Score()
#         score.hideturtle()
#         score.write(f"Score = {score}", align="center", font=("Century Gothic", 40, "bold"))
       

