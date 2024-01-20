from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1.0, stretch_len=3.0)
        self.goto_start_position()
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_forward(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT

    def goto_start_position(self):
        self.goto(randint(250, 300), randint(-280, 280))

