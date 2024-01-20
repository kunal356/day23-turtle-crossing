import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
player = Player()
screen.onkey(player.move_up, "Up")
scoreboard = Scoreboard()
game_is_on = True

car_manager = CarManager()

while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.update_scoreboard()
screen.exitonclick()
