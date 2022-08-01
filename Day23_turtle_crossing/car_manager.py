import random
from turtle import Turtle
import turtle
from venv import create
COLORS = ['red','yellow','orange','violet','blue','green','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_initial_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.create_car()
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:    
            new_car  = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-270,270)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_initial_speed)

    def level_up(self):
        self.car_initial_speed += MOVE_INCREMENT 