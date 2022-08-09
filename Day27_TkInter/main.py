import tkinter

from numpy import pad

window = tkinter.Tk()
window.minsize(500,500)
window.config(padx=50, pady=50)

window.title("My First GUI Program...")

my_label = tkinter.Label(text="I am Mahesh\n",font=("Arial") )
my_label.grid(row=0 , column=0)
my_label.config(padx=50, pady=50)

def button_clicked():
    print("Button got cliked...")
    # input = tkinter.Entry()
    # input.pack()
    # print(input.get())

    my_label.config(text=f"{input.get()}")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry
# print("\n\n")

input = tkinter.Entry()
input.grid(row=0,column=2)
print(input.get())
window.mainloop()