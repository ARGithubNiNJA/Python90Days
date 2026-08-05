from turtle import Turtle
ALIGNMENT = "center"
FONT= "arial.ttf"
FONT_SIZE = 20
FONT_COLOR = "white"
FONT_STYLE = "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,260)
        self.color(FONT_COLOR)
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()