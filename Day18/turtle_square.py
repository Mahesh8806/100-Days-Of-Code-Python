from turtle import Turtle, Screen

timmy_the_turtle = Turtle();
timmy_the_turtle.shape("turtle");
# timmy_the_turtle.color('red')
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)


timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()

# installing heroes packge using command line - pip install heroes;
# using heroes package...
import heroes
print(heroes.gen())