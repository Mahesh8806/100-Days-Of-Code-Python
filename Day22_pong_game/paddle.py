from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def move_up(self):
        print("Moving Up")
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        print("Moving Down")
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
