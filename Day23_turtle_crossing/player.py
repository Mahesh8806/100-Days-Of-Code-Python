from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
class Player(Turtle):
    def __init__(self):
        super().__init__();
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_backward()
        self.move_forward()

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor() , new_y)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)
        