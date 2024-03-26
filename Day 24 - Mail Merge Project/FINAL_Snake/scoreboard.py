from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("my_highscore.txt") as file:
            high_score = file.read()
            self.high_score = int(high_score)
        
        self.color("white")
        self.teleport(0,270)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align = ALIGNMENT, font = FONT)
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1

        self.update_score()

    def save_highscore(self):
        with open("my_highscore.txt", mode = "w") as file:
            file.write(str(self.high_score))
        
