from click import clear
from requests import ReadTimeout
from torch import rand
from game_data import data;
from art import logo , vs;
import random;

def format_data(account):
    acc_name = account["name"];
    acc_description = account["description"];
    acc_country = account["country"];
    return f"{acc_name}, a {acc_description}, from {acc_country}";

def check_answer(guess, a_f_count, b_f_count):
    if a_f_count > b_f_count:
        return guess == "a";
    else:
        return guess == "b";


account_b = random.choice(data);
game_continue = True;
score = 0;
# print(account_a)
print(logo)

while game_continue:
    account_a = account_b;
    account_b = random.choice(data);

    if account_a == account_b:
        account_b = random.choice(data);

    print(f"Compare A: {format_data(account_a)}")
    print(vs);
    print(f"Compare b: {format_data(account_b)}")

    guess = input("Guess, Who has more followers? Type 'A' or 'B'\n").lower();

    a_f_count = account_a["follower_count"];
    b_f_count = account_b["follower_count"];

    check = check_answer(guess, a_f_count, b_f_count);

    clear();
    print("\n",logo)
    
    if check:
        score += 1;
        print(f"You are Right!!, Current score is {score}");
    else:
        print(f"Sorry, Thats Wrong!!!, Final score is {score}");
        game_continue = False;


        