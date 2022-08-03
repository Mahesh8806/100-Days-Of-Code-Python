from turtle import Screen, Turtle
import turtle
from wsgiref.util import guess_scheme
import pandas

from torch import align_tensors

turtle = Turtle()

screen = Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")

data_states = data.state.to_list()
guessed_states = []
# print(data_states)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 State Correct",prompt="What's Another State's name?").title()
    
    if answer_state == 'Exit':
        # missing_state =[]
        # for state in data_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        
        missing_state = [state for state in data_state if state not in guessed_states]
        print(missing_state)    

        construct_dict={
            'States Name':missing_state,
        }    
        df = pandas.DataFrame(construct_dict)
        df.to_csv("missing_states")

        break;
        
    if answer_state in data_states:
        guessed_states.append(answer_state)
        t = Turtle()
        # t.shape('circle')
        t.hideturtle()
        t.penup()
        data_state = data[answer_state == data["state"]]
        # print(data_state)
        t.goto(int(data_state['x']), int(data_state['y']))
        t.write(data_state['state'].item())

    

screen.mainloop()