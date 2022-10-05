from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")

paddle_1 = Turtle("square")
paddle_1.color("white")
paddle_1.penup()
paddle_1.setpos(350, 0)
paddle_1.shapesize(stretch_wid=5, stretch_len=1, outline=1)

screen.listen()





screen.exitonclick()