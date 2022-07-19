from turtle import clear

from pygments import highlight


bids = {

}
def find_highest_bidder(bid_record):
    heighest_bid = 0 ; 
    winner = ""
    for bidder in bid_record:
        bidder_price = int(bid_record[bidder]);
        if bidder_price > heighest_bid:
            heighest_bid = bidder_price;
            winner  = bidder;
    print(f"The winner is {winner} with a bid of ${heighest_bid}")

flag = False;
while not flag:
    name = input("Enter Your Name?\n");
    price = input("What is Your Bid? \n$");
    bids[name] = price;
    choice = input("Do you want to continue or not typw 'yes' or 'no'?");
    if choice == "no":
        flag = True;
        find_highest_bidder(bids);
    else :
        clear();


# print(bid);