from turtle import Turtle 

tim = Turtle()
tim.shape("classic")
tim.width(5)


for i in range(100):
    if i%2 == 0:
        tim.forward(50)
        tim.pencolor('black')
        tim.forward(50)
        # tim.penup()
        # tim.pendown()
        tim.right(45)

    elif i% 5 == 0:
        tim.pencolor('red')
        tim.right(45)
        # tim.forward(50)

    # else:

