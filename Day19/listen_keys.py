from turtle import Turtle, Screen, backward
tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def clear():
    tim.clear()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward,"s" )
screen.onkeypress(turn_left,"a" )
screen.onkeypress(turn_right,"d" )
screen.onkeypress(clear, "c")
screen.onkeypress(pen_up, "u")
screen.onkeypress(pen_down, "j")


screen.exitonclick()