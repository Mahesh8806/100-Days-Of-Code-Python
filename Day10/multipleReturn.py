def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "Heyy!!! You didn't provide valid inputs..."
    formated_f_name = f_name.title();
    formated_l_name = l_name.title();
    # print(f"{formated_f_name} {formated_l_name}");
    return (f"---------------Formated string is---------------\n{formated_f_name} {formated_l_name}");


data = format_name(input("What is your first name?\n"),input("What is your last name?\n"));
print(data);