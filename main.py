from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect colision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    #Detect colision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect L paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()