from random import random,randint
from turtle import Turtle, Screen, position

tim = Turtle()
tim.speed(1)
tim.hideturtle()

screen = Screen();
screen.setup(width=500,height=500)
user_guess = screen.textinput(title="Make your bet",prompt="Whick turtle will win the race? Enter the color:")
colors = ['red','yellow','violet','green','blue','orange']
all_turtle = []
position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, position[turtle_index])
    all_turtle.append(new_turtle)

if user_guess:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race = False
            winner_turtle = turtle.pencolor()
            if winner_turtle == user_guess:
                print(f"You have won!, The {winner_turtle} turtle is the winner!")
            else:
                print(f"You have Lost!, The {winner_turtle} turtle is the winner!")
                
        rand_dist = randint(1,10)
        turtle.forward(rand_dist)

screen.exitonclick()