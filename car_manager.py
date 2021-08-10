import random
from turtle import Turtle

COLORS = ["green", "red", "yellow", "blue", "cyan", "purple"]
CAR_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class Car:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = CAR_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def car_speed_increment(self):
        self.car_speed += MOVE_INCREMENT
