from turtle import width


height = float(input("Enter your height in m\n"));
weight = float(input("Enter your weight in kg\n"));

bmi = weight / height ** 2;

round_bmi   = round(bmi);
print(round_bmi);

if round_bmi < 18.5 :
    print(f"Your Bmi is {round_bmi}, you are UnderWeight.");
elif round_bmi < 25:
        print(f"Your Bmi is {round_bmi}, You are Normal Weight.");
elif round_bmi < 30:
    print(f"Your Bmi is {round_bmi}, You are Over Weight.");
elif round_bmi <35:
    print(f"Your Bmi is {round_bmi}, You are Obese.");
else:
    print(f"You Bmi is {round_bmi}, You are Clinically Obese");