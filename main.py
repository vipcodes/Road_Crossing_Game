import time
from turtle import Screen

from car_manager import Car
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.title("Road Crossing")
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkeypress(player.move_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with wall
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car_manager.car_speed_increment()

    # Detect collision with Car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
