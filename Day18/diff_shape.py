from turtle import Screen, Turtle
import random

from torch import randint

num =int(input("How many shape do want to draw...\n"))

tim = Turtle()
tim.penup()
tim.setpos(-40,30)
tim.pendown()
angle = 360
def fun(part, color):
    global angle
    degree = angle/part
    for _ in range(part):
        tim.pencolor(color)
        tim.forward(100)
        tim.right(degree)


color = ['red','yellow','green','violet','blue','orange','black','purple','pink']
for i in range(1,num):
    rand= random.randint(0,10)
    fun(i+1, color[rand])

# screen = Screen()
# screen.exitonclick()