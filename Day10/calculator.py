from art import logo;

def add(num1, num2):
    return num1 + num2;

def sub(num1, num2):
    return num1 - num2;

def mult(num1, num2):
    return num1 * num2;

def divide(num1, num2):
    return num1 / num2;


operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : divide
}
def calculation():
    print(logo);
    print("\n\n-----------------------Calculator Operations...-----------------------\n")
    for symbol in operations:
        print(symbol,"\n");

    num1 = int(input("Enter 1st Number ...\n"));

    flag = True;

    while flag:     
        operation_symbol = input("Pick an Operation from the line above...\n");
        num2 = int(input("Enter 2nd Number...\n"));
        if (operation_symbol == "+" or operation_symbol == "-" or operation_symbol == "*" or operation_symbol == "/") and num1 != NULL and num2 != NULL:
            calculation_function = operations[operation_symbol];
            answer = calculation_function(num1,num2);
            print(f"{num1} {operation_symbol} {num2} = {answer}");
            conti = input(f"Type 'y' to continue with answer {answer}, or type 'n' to start a new calculation & Type 'e' to exit\n");
            if conti=='y':
                num1 = answer;
            elif conti == "n":
                calculation();
            else:    
                flag =False;


        else:
            print("Invalid Input");

calculation();