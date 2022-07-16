year = int(input("Enter year..."));

if year%4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leep Year...")
        else:
            print(f"{year} Not leep Year...")
    else:
        print(f"{year} is leep Year")
        

else:
    print(f"{year} Not leep Year...")