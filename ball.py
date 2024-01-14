from turtle import Turtle
from random import choice
TOWARD = [10, -10]
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def right_bounce(self):
        self.x_move = -10
        self.y_move = -10

    def left_bounce(self):
        self.x_move = 10
        self.y_move = 10

    def r_reset_position(self):
        self.goto(0, 0)
        self.x_move = -10
        self.y_move = choice(TOWARD)

    def l_reset_position(self):
        self.goto(0, 0)
        self.x_move = choice(TOWARD)
        self.y_move = -10
