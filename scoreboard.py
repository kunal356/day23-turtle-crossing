from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align="center", font=FONT)