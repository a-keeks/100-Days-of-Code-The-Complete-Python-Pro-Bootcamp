from turtle import Turtle, Screen

STEPS = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()

class Snake(Turtle): 
    def __init__(self): 
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segmt = Turtle("square")
        snake_segmt.color("green")
        snake_segmt.penup()
        snake_segmt.goto(position)
        self.segments.append(snake_segmt)

    def extend(self):
        for _ in range(2):
            self.add_segment(self.segments[-1].position())


    def move(self):
        for snake_segmt in range(len(self.segments)-1, 0, -1): #range(starts, stops, step) ## going from the last segm. to the first so range is last index of list to 0
            new_x = self.segments[snake_segmt-1].xcor() # finds x coord....
            new_y = self.segments[snake_segmt-1].ycor() # ... and y coord of prev. segment
            self.segments[snake_segmt].goto(new_x, new_y) # moves each segm. into place of prev. segment
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

    def reset(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        