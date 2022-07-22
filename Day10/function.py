def format_name(f_name, l_name):
    formated_f_name = f_name.title();
    formated_l_name = l_name.title();
    # print(f"{formated_f_name} {formated_l_name}");
    return (f"{formated_f_name} {formated_l_name}");


data = format_name(f_name="MaHesH",l_name="BunaGE");
print(data)