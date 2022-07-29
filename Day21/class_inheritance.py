from matplotlib.pyplot import cla
from numpy import eye


class Animal:
    def __init__(self,eye,name) -> None:
        self.number_of_eyes = eye
        self.name = name
    def breath(self):
        print(f"Enhale, Exhale the number eyes of{self.name} is {self.number_of_eyes}")

class Fish(Animal):

    def __init__(self, eye,name) -> None:
        super().__init__(eye, name)
        self.name = name
    def move(self):
       
        print(f"{self.name} move in water... Having {self.number_of_eyes} number of eyes")
        
fish = Fish(4,"Rahul")
jack = Fish(6,"Mahesh")
fish.move()
jack.move()
fish.breath()
jack.breath()
print(fish.__dict__)
print(jack.__dict__)