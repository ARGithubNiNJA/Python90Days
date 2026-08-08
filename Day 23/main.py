import time
from _pyrepl import console
from turtle import Turtle,Screen
from Player import Player
from CarsManager import*
from ScoreBoard import scoreboard

screen = Screen()
screen.setup(width=600,height=600)

screen.tracer(0)

player=Player()
screen.listen()
car_Manager=CarManager()
screen.onkey(player.go_up,"Up")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_Manager.create_car()
    car_Manager.move_cars()
    score_board=scoreboard()
    score_board.update_scoreboard()

    for car in car_Manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over_screen()
            game_is_on=False

    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_Manager.level_up()
        score_board.increase_level()

screen.exitonclick()


