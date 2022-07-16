print("* * *..Welcome to RollerCoaster..* * * ");

height = int(input("Enter your height in cm...\n"));
bill = 0;

if height>=120:
    print("You can ride the RollerCoster\n");
    age = int(input("Enter Your Age\n"));

    if age<12:
        bill = 5;
        print("Plese pay $5.\n")
    elif age<=18:
        bill = 10;
        print("Please pay $10.\n");
    else:
        bill = 12;
        print("Adults tickets are $12.\n");

    wants_photo = input("Do you want photo taken? Y or N.\n");
    if wants_photo == "Y":
        bill += 3;

        print(f"Your final bill is ${bill}");

    

else:
    print("Sorry, You have to Grow Taller to ride rollerCoster.\n");

