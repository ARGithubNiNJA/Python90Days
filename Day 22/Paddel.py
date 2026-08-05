from turtle import Turtle

PADDLE_SHAPE = "square"
PADDLE_BG_COLOR = "white"
PADDLE_LEN = 1
PADDLE_WIDTH = 5
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.color(PADDLE_BG_COLOR)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.penup()
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)