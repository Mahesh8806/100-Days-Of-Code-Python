from telnetlib import DO
from tkinter import LEFT
from turtle import Turtle, Screen, down, forward
import turtle
import time
game_is_on = True
POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
# screen = Screen()
class Sneke:
    def __init__(self):
        self.list_turtle = []
        self.create_sneke()
        self.screen = Screen()
        # self.list_turtle[0].shape("turtle")
        self.head = self.list_turtle[0]

    def create_sneke(self):
        for turtle_num in POSITIONS:
            self.add_sneke(turtle_num)
    
    def add_sneke(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.width(20)
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.list_turtle.append(new_turtle)

    def extend_sneke(self):
        self.add_sneke(self.list_turtle[-1].position())        

    def move_left(self):
        print("Move left")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        print("Move right")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        print("Move Up")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): 
        print("Move Down")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def where_to_turn(self):
        self.screen.onkey(self.move_left,"Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")

    def move(self):
            for turtle_idx in range(len(self.list_turtle)-1, 0, -1):
                new_x = self.list_turtle[turtle_idx - 1].xcor()
                new_y = self.list_turtle[turtle_idx - 1].ycor()
                self.list_turtle[turtle_idx].goto(new_x, new_y)

            self.head.forward(20)
       
    def reset_sneke(self):
        for sneke in self.list_turtle:
            sneke.goto(1000,1000)
        self.list_turtle.clear()
        self.create_sneke()
        self.head = self.list_turtle[0]
