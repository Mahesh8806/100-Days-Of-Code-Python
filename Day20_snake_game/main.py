from turtle import Screen, forward
import time

from torch import initial_seed
from score_board import ScoreBoard
from sneke import Sneke
from food import Food

initial_sneke  = 3
SCORE = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Sneke Game")
screen.listen()

turtle_position = [0, -20, -40]
game_is_on = True

score_board = ScoreBoard()
# score_board.create_board()
sneke = Sneke()
food = Food()


# sneke.create_sneke()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    sneke.move()
    # for turtle_idx in range(len(list_turtle)-1, 0, -1):
    #     new_x = list_turtle[turtle_idx - 1].xcor()
    #     new_y = list_turtle[turtle_idx - 1].ycor()
    #     list_turtle[turtle_idx].goto(new_x, new_y)

    # list_turtle[0].forward(20)
    # where_to_turn(list_turtle)
    # sneke.where_to_turn()
    sneke.where_to_turn()

    if sneke.list_turtle[0].distance(food)<15:
        print("you got the food...")
        food.refresh_food()
        sneke.extend_sneke()
        score_board.update_score()
        
    if int(sneke.list_turtle[0].xcor()) > 280 or int(sneke.list_turtle[0].xcor()) < -280 or int(sneke.list_turtle[0].ycor()) > 280 or int(sneke.list_turtle[0].ycor()) < -280:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset()
        sneke.reset_sneke()

    for list in sneke.list_turtle:
        if sneke.list_turtle[0] == list:
            pass
        elif int(sneke.list_turtle[0].distance(list)) < 10:
            score_board.reset()
            sneke.reset_sneke()


screen.exitonclick()