import imp
import time
from turtle import Screen
import turtle
from paddle import Paddle
from numpy import pad
from ball import Ball
from game_over import GameOver
from score_board import Score_Board
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("-----------------------Pong Game----------------------")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
game_over = GameOver()
score_board = Score_Board()

screen.listen()
screen.update()


screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        # ball.bounce_y()
        ball.bounce_x()
            # ball.bounce_x()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset()
        score_board.update_score_left()

    if ball.xcor() < -380 :
        ball.reset()
        score_board.update_score_right()

    if score_board.l_score == 2:
        game_is_on = False
        print("Left User is the winner...")

    if score_board.r_score == 2:
        game_is_on = False
        print("Right User is the winner...")

screen.exitonclick()
