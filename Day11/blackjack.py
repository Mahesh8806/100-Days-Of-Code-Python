from ast import Compare
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];
    return random.choice(cards);

def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0;

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11);
        cards.append(1);
    return sum(cards) 

def campare(user_score , computer_score):
    if user_score == computer_score:
        return "Draw ";
    elif computer_score == 0 :
        return "Lose, opponent has BlackJack...";
    elif user_score == 0 :
        return "Win with a BlackJack...";
    elif user_score > 21 :
        return "You went over. You lose..."
    elif computer_score > 21:
        return "Opponent went over. You win...";
    elif user_score > computer_score:
        return "You Win...";
    else:
        return "You Lose...";

user_cards = [];
computer_cards = [];
is_game_over = False;

for _ in range(2):
    user_cards.append(deal_card());
    computer_cards.append(deal_card());

while not is_game_over:
    user_score = calculate_score(user_cards);
    computer_score = calculate_score(computer_cards);
    print(f"Your cards: {user_cards}, Current score: {user_score}");
    print(f"Computers first cards: {computer_cards}, Current score: {computer_score}");


    if user_score==0 or computer_score == 0 or user_score>21:
        is_game_over = True;
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:\n");
        if user_should_deal == "y":
            user_cards.append(deal_card());
        else:
            is_game_over = True;

while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card());
    computer_score = calculate_score(computer_cards);

ans = campare(user_score , computer_score);



print(ans)


