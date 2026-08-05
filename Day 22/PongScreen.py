from turtle import Screen
from Paddel import Paddle
from Ball import Ball
import time

screen =  Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.tracer(0)


screen.title("Pong Game")
paddle1 = Paddle(450, 0)
paddle2 = Paddle(-450, 0)
ball = Ball()
def go_up():
    new_y=paddle1.ycor()+20
    paddle1.goto(paddle1.xcor(), new_y)
def go_down():
    new_y=paddle1.ycor()-20
    paddle1.goto(paddle1.xcor(), new_y)
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_on=True
while game_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(paddle1)<50 and ball.distance(paddle2)>320 or ball.distance(paddle2)<50 and ball.ycor()>-320:
        ball.bounce_x()
screen.exitonclick()