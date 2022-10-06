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
        ball.bounce()

screen.exitonclick()