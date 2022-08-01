from re import S
from turtle import Turtle

from sklearn.feature_selection import SelectKBest

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.hideturtle()
        # self.color("black")
        self.color('green')
        self.penup()
        self.update_score_board()

    def update_score_board(self):

        self.goto(-270, 260)
        self.write(f"Left Score: {self.score}",False,align='left',font=("Arial",18,"normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()