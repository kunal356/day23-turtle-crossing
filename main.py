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
all_cars = []


def generate_random_cars():
    car_manager = CarManager()
    all_cars.append(car_manager)


def move_car():
    for car in all_cars:
        if car.distance(player) < 40:
            return False
        elif car.xcor() < -320:
            car.goto_start_position()
        else:
            car.move_forward()
    return True


def increase_car_speed():
    for car in all_cars:
        car.increase_speed()


while game_is_on:
    if len(all_cars) < 5:
        generate_random_cars()
    if not move_car():
        game_is_on = False
        scoreboard.game_over()
    if player.ycor() >= 280:
        scoreboard.update_scoreboard()
        increase_car_speed()
        player.reset_turtle()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
