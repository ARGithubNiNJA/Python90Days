from turtle import Screen
import time
from Snake import Snake
from Food import  Food
from Scoreboard import  Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.tracer(0)
#todo step 1 create a initial snake body
# turtle_1=Turtle()
# turtle_1.shape("square")
# turtle_1.color("white")
#
# turtle_2=Turtle()
# turtle_2.shape("square")
# turtle_2.color("white")
# turtle_1.goto(-20,0)
#
# turtle_3=Turtle("square")
# turtle_3.color("white")
# turtle_3.goto(-40,0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#todo Moving the turtle in sync

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect the collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()




screen.exitonclick()