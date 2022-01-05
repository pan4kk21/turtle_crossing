from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(x=300, y=random.randint(-250, 250))
        new_car.seth(180)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
