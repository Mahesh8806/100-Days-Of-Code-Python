from re import S
from turtle import Turtle

from sklearn.feature_selection import SelectKBest

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0 
        self.r_score = 0 
        self.hideturtle()
        self.color("green")
        self.penup()
        self.update_score_board()

    def  update_score_board(self):

        self.goto(-100, 250)
        # self.update_score_left()
        self.write(f"Left Score: {self.l_score}",False,align='center',font=("Arial",18,"normal"))

        # self.update_score_right()
        self.goto(100,250)
        self.write(f"Right Score: {self.r_score}",False,align='center',font=("Arial",18,"normal"))

    def update_score_left(self):
        self.l_score += 1
        self.color('green')
        self.clear()
        self.update_score_board()

    def update_score_right(self):
        self.r_score += 1
        self.color('green')
        self.clear()
        self.update_score_board()