
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
FONT_SMALL = ("Courier", 24, "normal")
LEFT = (-100, 200)
RIGHT = (100, 200)
CENTER = (0, 0)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.pendown()
        self.teleport(x=0,y=-300)
        self.goto(0, 300)
        self.penup()
        self.goto(LEFT)
        self.write(f'{self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(RIGHT)
        self.write(f'{self.r_score}', align=ALIGNMENT, font=FONT)

    def increase_l(self):
        self.l_score += 1
        self.update_scores()

    def increase_r(self):
        self.r_score += 1
        self.update_scores()

    def winner(self):
        self.goto(CENTER)
        self.clear()
        if self.l_score > self.r_score:
            self.write(f'  GAME OVER\n     {self.l_score}:{self.r_score}\nPlayer 1 Wins', align=ALIGNMENT, font=FONT_SMALL)
        else:
            self.write(f' GAME OVER\n{self.l_score}:{self.r_score}\nPlayer 2 Wins', align=ALIGNMENT, font=FONT_SMALL)

