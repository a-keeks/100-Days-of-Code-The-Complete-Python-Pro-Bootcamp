from turtle import Turtle

ALIGNMENT = "center"
WINNING_SCORE = 11

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 200)
        self.write(self.l_score, align = ALIGNMENT, font = ("Agency FB", 60, "bold"))
        self.goto(60, 200)
        self.write(self.r_score, align = ALIGNMENT, font = ("Agency FB", 60, "bold"))

    def winner(self):
        if self.l_score == WINNING_SCORE:
            return "Player 1"
        elif self.r_score == WINNING_SCORE:
            return "Player 2"
        

            

    def game_over(self):
        self.teleport(0,-40)
        self.write("Game Over.", align = ALIGNMENT, font = ("Courier", 10, "bold") )