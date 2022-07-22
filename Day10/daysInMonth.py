def is_leaf(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True;
            else:
                return False;
        else:
            return True;
    else:
        return False;

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if month>12 or month<1:
        return "You Enter Invalid Month...";
    if is_leaf(year) and month == 2 :
        return 29;
    return f"----------------------{month_days[month-1]}";

year = int(input("Enter Year..."));
month = int(input("Enter Month..."));
months = ["January","February","March","April","May","Jun","July","August","Saptember","October","November","December"];
days = days_in_month(year=year , month=month);
print(f"\n{days} Days in Month {months[month-1]} --------------------------");