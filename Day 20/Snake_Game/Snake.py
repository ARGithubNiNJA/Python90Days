from turtle import Turtle

STARTING_POSITION=starting_position = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake:
    def __init__(self):

        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in starting_position:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segment.append(new_turtle)


    def move(self):
        for new_turtle in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[new_turtle - 1].xcor()
            new_y = self.segment[new_turtle - 1].ycor()
            self.segment[new_turtle].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)