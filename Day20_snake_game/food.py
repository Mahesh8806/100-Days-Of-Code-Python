import random
from turtle import Turtle
import turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(1,1)
        self.color('blue')
        self.refresh_food()

    def refresh_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)
        