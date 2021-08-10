from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=("courier", 16, "normal"))

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("courier", 20, "normal"))
