# Write your code below this line 👇
# Get age From User
age = input("What is your current age\n");

age_as_int = int(age);
years_remaining = 90 - age_as_int;
days_remaining = years_remaining * 365;
weeks_remaining = years_remaining * 52;
month_remaining = years_remaining * 12;
# final output
message = f"You have {days_remaining} Days, {weeks_remaining} Weeks and {month_remaining} Months left.";
print(message);
