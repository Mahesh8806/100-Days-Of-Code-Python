import time
from turtle import Screen
from game_over import GameOver
from score_board import Score_Board
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Score_Board()
game_over = GameOver()

screen.update()

screen.listen()
screen.update()

screen.onkeypress(player.move_forward , "Up")
screen.onkeypress(player.move_backward , "Down")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            game_over.match_over()

   
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        score_board.update_score()

    


screen.exitonclick()