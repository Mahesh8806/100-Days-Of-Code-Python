import imp
from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__();
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)

    def match_over(self):
        self.write("Game is Over",False,align='center',font=("Arial",20,"normal"))
    