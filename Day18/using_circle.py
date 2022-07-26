from random import random
import random
from turtle import Screen, Turtle, exitonclick
import turtle

how_many = int(input("How many Circle do you want to draw...\n"));

tim = Turtle();
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def fun(no): 
    for _ in range(int(360/no)):
        tim.color(random_color())
        tim.circle(50)
        tim.left(no);

fun(how_many)
screen = Screen()
screen = exitonclick()