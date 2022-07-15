# Write your code below this line 👇
# Create a Greeting for your Program.
print("Welcome To Tip Calculator.")
# Ask User for the total bill.
total_bill = float(input("What was the total bill?\n$"));
# Ask user to what tip would you like to give...
tip = int(input("What tip would you like to give? 10 %, 12 % and 15 % \n"));

total_amount = total_bill * tip / 100;
total_amount += total_bill;
print(type(total_amount));

how_many_people = int(input("How many people to split the bill?\n"));
amount_each = float(total_amount / how_many_people)

print("Each person should pay $"+str(round(amount_each,2)))

