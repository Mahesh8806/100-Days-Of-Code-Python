from hashlib import md5
import imp
from pydoc import visiblename
from tkinter import CENTER
from turtle import Turtle, update


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = open("data.txt",mode='r')
        self.high_score = (self.file.read())
        self.hideturtle()
        self.penup()
        self.goto(0 , 260)
        self.color('green')
        self.update_score_board()

    def update_score_board(self):
        self.goto(-250 , 260)
        self.write(f"Score: {self.score}",False,align='left',font=("Arial",20,"normal"))
        self.goto(250 , 260)
        self.write(f"Hight Score: {self.high_score}",False,align='right',font=("Arial",20,"normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
       
    def reset(self):
        if self.score > int(self.high_score):
            self.file = open("data.txt",mode='w')
            self.file.write(str(self.score))
            self.high_score = self.score
        self.score = 0 
        self.goto(0,0)
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.penup()
        self.goto(0 , 0)
        self.color("red")
        self.write("Game is Over",False,align='center',font=("Arial",20,"normal"))

