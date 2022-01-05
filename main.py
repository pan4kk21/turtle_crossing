import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle_pl = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(turtle_pl.move_forward, "Up")

i = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if i % 6 == 0:
        car_manager.create_car()
        car_manager.move()
    i += 1
    for car in car_manager.all_cars:
        if turtle_pl.distance(car) <= 30:
            score.write_game_over()
            game_is_on = False
    if turtle_pl.is_at_finish_line():
        turtle_pl.goto(x=0, y=-280)
        car_manager.increase_speed()
        score.level += 1
        score.write_score()

screen.exitonclick()