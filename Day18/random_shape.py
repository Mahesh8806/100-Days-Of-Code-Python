from random import random
import random
import turtle as t

tim = t.Turtle()
tim.width(10)
tim.speed("fastest")
t.colormode(255)

color = ['red','yellow','green','violet','blue','orange','black','purple','pink']
direction = [0, 90, 180, 270, 360];

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors= [r, g, b]
    return colors

for i in range(200):
    tim.color(random_color())
    tim.forward(20)
    s= tim.setheading(random.choice(direction))