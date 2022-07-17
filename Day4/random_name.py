

from random import random
from tkinter.font import names
import random;

namesAsCSV = input("Enter Everybody's name, seperated by comma.\n")

names = namesAsCSV.split(", ");

print(names);

# not allow to use choice() function...
# rand_name = random.choice(names);
# print(rand_name+" is going to buy milk today");

random_int = random.randint(0 , len(names)-1);
print(names[random_int]+" is going to buy milk today");