from turtle import Turtle, Screen
from snake import Snake, Food
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) #any code after this is run behind a blank screen (we don't see the turtles being made)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() #brings code onto screen
    time.sleep(0.1) # 0.1 sec delay between loops

    snake.move()
    

screen.exitonclick()
