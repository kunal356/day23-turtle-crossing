from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.penup()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1.0, stretch_len=3.0)
            random_y = randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
