from turtle import Turtle

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.25, 0.75, 1)
        self.teleport(0, 270)
        self.seth(270)
        self.penup()

        for _ in range(19):
            self.stamp()
            self.fd(30)

        self.ht()