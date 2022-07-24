# from turtle import Turtle, Screen

# timmy  = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("coral")
# timmy.forward(100)




# my_screen = Screen();
# print(my_screen.canvheight)
# my_screen.exitonclick();
from matplotlib.pyplot import table
from prettytable import PrettyTable

table = PrettyTable();

print(table)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmandar"]) 
table.add_column("type",["Electric","Water","Fire"])
table.add_row(["mahesh","rahul"])
table.align = "l"
print(table)


