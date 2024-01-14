from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(position)

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()