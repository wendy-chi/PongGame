from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((475, 0))
l_paddle = Paddle((-480, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

score_l = Score((-100, 350))
score_r = Score((100, 350))

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    print(f"xcor{ball.xcor()}")
    print(f"ycor{ball.ycor()}")
    print(f"1_ball.distance(r_paddle){ball.distance(r_paddle)}")
    score_l.update_scoreboard()
    score_r.update_scoreboard()
    #球碰到上面顶或者下面底
    if ball.ycor() >= 380 or ball.ycor() <= -380:
        ball.bounce()

    #球碰到右边的paddle
    if ball.xcor() >= 450 and 20 <= ball.distance(r_paddle) <= 50:
        print(f"2_ball.distance(r_paddle){ball.distance(r_paddle)}")
        ball.right_bounce()
        score_r.add_score()

    #球碰到左边的paddle
    if ball.xcor() <= -450 and 20 <= ball.distance(l_paddle) <= 50:
        ball.left_bounce()
        score_l.add_score()

    #球miss掉右边的paddle
    if ball.xcor() > 480:
        ball.r_reset_position()
        score_l.add_score()

    # 球miss掉左边的paddle
    if ball.xcor() < -480:
        ball.l_reset_position()
        score_r.add_score()

screen.exitonclick()