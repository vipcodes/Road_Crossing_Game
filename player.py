from turtle import Turtle

STARTING_POINT = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(STARTING_POINT)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
