import tkinter

from torch import round_

FONT = ("Arial",24, "bold")

window = tkinter.Tk()
window.title("Miles to Km Converter...")
window.config(padx=20,pady=20)

window.minsize(width=200,height=100)

def calculate_km():
    print("calculate cliked..")
    km = int(round(float(miles_input.get()) * 1.609))
    km_result_table.config(text= f"{km}")


miles_input  = tkinter.Entry(width=8)
miles_input.grid(column=1, row=0)

lable = tkinter.Label(text="Miles")
lable.grid(column=2, row=0)


is_lable_equal = tkinter.Label(text="Is equal to ...")
is_lable_equal.grid(column=0, row=1)


km_result_table = tkinter.Label(text="0")
km_result_table.grid(column=1, row=1)


kilometer_result = tkinter.Label(text="Km")
kilometer_result.grid(column=2, row=1)


button = tkinter.Button(text="Clicked Me", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()