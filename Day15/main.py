

MENU = {
    "espresso":{
        "ingradient":{
            "water":100,
            "coffee" :18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingradient":{
            "water":200,
            "milk": 150,
            "coffee" :24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingradient":{
            "water":250,
            "milk": 100,
            "coffee" :24,
        },
        "cost":3.0,
    },
}
resources = {
    "water":300,
    "milk" :200,
    "coffee":100,
}


is_on = True
profit = 0



def is_resource_sufficient(order_ingradients):
    """Return True when order can be made, False if ingredient are insufficient..."""
    for item in order_ingradients:
        if order_ingradients[item] >= resources[item]:
            print(f"Sorry, there is no enough {item}")
            return False
    return True

def process_coins():
    """Returns total calculated money from inserted."""
    print("\n-------Please Insert Coins...------\n");
    total = int(input("How many quarters?:\n"))* 0.25
    total += int(input("How many dimes?:\n"))* 0.1
    total += int(input("How many nickles?:\n"))* 0.05
    total += int(input("How many pennies?:\n"))* 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, thats not enough money to make order. Money refunded.\n")
        return False

def make_coffee(drink_type , ingradient):
    """This function works to update Resources...""";
    for item in ingradient:
        resources[item] -= ingradient[item]
    print(f"Here is your {drink_type} ☕ ")

while is_on:
    choice = input("What would  you like? \n1) Type (espresso/latte/cappuccino)\n2) Type 'report' To See Resources Remaining.\n3) Type 'off' to off the machine.\n").lower();
    if choice != "espresso" and choice != "cappuccino" and choice != "latte" and choice != "off" and choice != "report":
        print("You Entered invalid Choice, Please Enter Valid Choice From above...")
    elif choice == "off":
        is_on = False;
    elif choice == "report":
        print("--------------------Machine Report-----------------------")
        print(f"water: {resources['water']}ml");
        print(f"milk: {resources['milk']}ml");
        print(f"coffee: {resources['coffee']}g");
        print(f"Money: ${profit}\n\n")
    else:
        drink = MENU[choice];
        # print(drink);
        if is_resource_sufficient(drink['ingradient']):
            payment = process_coins();
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingradient'])

