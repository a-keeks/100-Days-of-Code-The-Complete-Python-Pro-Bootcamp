from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-240, 240, 20)
        self.teleport(random_x, random_y) #food goes to random x, y coordinates


