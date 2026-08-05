from turtle import Screen
PADDLE=None
class Movement:
    def __init__(self,screen,paddle,current_y,current_x):
        self.screen = screen
        self.screen.listen()
        PADDLE = paddle

        self.screen.onkey()
    def go_Up:
        new_y=PADDLE.ycor()+20
        if new_y < 0: