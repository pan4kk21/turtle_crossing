from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-285, y=260)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="left")

    def write_game_over(self):
        self.home()
        self.write(arg="Game Over.", font=FONT, align="center")