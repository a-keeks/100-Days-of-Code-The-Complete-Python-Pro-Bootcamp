from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, WINNING_SCORE
from net import Net
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx = None, starty = -50)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
net = Net()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
sleep_time = 0.1

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_edges()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_paddles()
        
        if ball.distance(r_paddle) < 40 and ball.xcor() > 320:
            scoreboard.r_score += 1
        
        if ball.distance(l_paddle) < 40 and ball.xcor() < -320:
            scoreboard.l_score += 1
        
        sleep_time *= 0.85
        scoreboard.update_scoreboard()

    #Detect missed collision & award point to opposing player
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.l_score += 1

        #Left
        if ball.xcor() < -380:
            scoreboard.r_score += 1

        ball.reset_position()
        scoreboard.update_scoreboard()

    # Annouce winner when either player gets to 11 pts
    if scoreboard.r_score == WINNING_SCORE or scoreboard.l_score == WINNING_SCORE:
        net.clearstamps()
        pong_winner = scoreboard.winner()
        scoreboard.teleport(0,0)
        scoreboard.write(f"Winner: {pong_winner}!", align = "center", font = ("Courier", 25, "bold") )
        
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()




