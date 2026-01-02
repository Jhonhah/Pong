from turtle import Turtle,Screen
from time import sleep
from ball import Ball
from paddle import Paddle
from score import Score

WINNING_SCORE = 10
screen = Screen()
screen.setup(width=800,height=600)

screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # switching to manual screen refreshing

#Paddles
left = Paddle('l')
right = Paddle('r')
ball = Ball()
score = Score()
screen.update()

#screen events
screen.listen()
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")

go = True
while go:
    sleep(ball.m_speed)
    screen.update()
    ball.move()

    #detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    #collision with right paddle paddles
    if ((ball.distance(right) < 60 and ball.xcor() > 320) or
            (ball.distance(left) < 60 and ball.xcor() < -320)):
        ball.bounce_x()
        ball.m_speed = ball.m_speed *0.9

    #Updating score when ball beyond side walls
    if ball.xcor() > 380:
        ball.restart()
        score.increase_l()

    if ball.xcor() < -380:
        ball.restart()
        score.increase_r()

    if score.l_score >= WINNING_SCORE or score.r_score >= WINNING_SCORE:
        score.winner()
        go = False


screen.exitonclick()
