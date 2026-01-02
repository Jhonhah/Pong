from configparser import MAX_INTERPOLATION_DEPTH
from turtle import Turtle

MAX_H = 280
MAX_D = -260
STRETCH_WID = 5
STRETCH_LEN = 1
LEFT_X = -350
RIGHT_X = 350
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(STRETCH_WID, STRETCH_LEN)
        self.penup()
        self.starting_side(side)

    def starting_side(self, side):
        if side == 'l':
            self.goto(LEFT_X, 0)
        else:
            self.goto(RIGHT_X, 0)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < MAX_H:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > MAX_D:
            self.goto(self.xcor(), new_y)
