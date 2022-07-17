import random

from matplotlib.style import use;

scissor = '''

    ________
---'     ___)_____
            ______)  
         __________)
        (_____)   
---.___(_____)
''';

rock  = '''
    _________
---'     ____)
        (_____) 
        (_____) 
        (____)   
---.____(___)
''';
paper = '''
    ________
---'     ___)___
           _____)
           ______)  
         _______)   
---._________)
''';

# print(rock);
# print(paper);
# print(scissor);
list  = [rock , paper, scissor];

computer = random.randint(0, len(list));
# print(computer);

user  = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor.\n"));

if computer == user:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("Match Drow...");
elif computer == 0 and user == 1:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("You Win..");
elif computer == 0 and user == 2:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("Computer Win..");  
elif computer == 1 and user == 0:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("Computer Win..");
elif computer == 1 and user == 2:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("You Win..");
elif computer == 2 and user == 0:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("You Win..");
elif computer == 2 and user == 1:
    print(f"Computer Choice \n {list[computer]} \n User Choice {list[user]}");
    print("Computer Win..");
else:
    print("You Enter wrong Number...");



