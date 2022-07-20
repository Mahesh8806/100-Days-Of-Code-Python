from random import randint
from art import logo

from torch import true_divide
# Function to Guess the User's Answer...
EASY_LEVEL_TURNS = 10;
HARD_LEVEL_TURNS = 5;

def check_answer(guess, answer,turns):
    if guess > answer:
        print("Too high");
        return turns - 1;
    elif guess < answer:
        print("Too low");
        return turns - 1;

    else:
        print(f"You got it!!!, The answer was {answer}");
        return 0;
def set_difficulty():
    global chance;
    level = input("Choose Difficulti level. Type 'easy' or 'hard':\n");
    if level == 'easy':
        return EASY_LEVEL_TURNS;
    elif level == 'hard':
        return HARD_LEVEL_TURNS;
    else:
        print("You enter invalid data...");

def game():
    print(logo)
    print("Welcome to number gussing Game...");
    print("I am thinking of number between 1 to 100...");
    turns = set_difficulty();
    # print(f"You have {turns} to guess the number...");

    answer = randint(1, 100);
    print("------------The number to guess is :",answer);

    while turns >= 1:
        print(f"You have {turns} chances to guess the number...");
        guess = int(input("Make a Guess...\n"));
        turns = check_answer(guess , answer, turns);
        if turns == 0:
            print("You loss the number of chance to guess the number...");
game();