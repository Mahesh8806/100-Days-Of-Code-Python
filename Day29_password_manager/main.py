from ast import operator
from cProfile import label
import email
import json
from textwrap import indent
from tkinter import *
from tkinter import messagebox
from turtle import textinput
from typing import Literal
from idna import ulabel
import pyperclip
import json
# ---------------------------- SEARCH OPERATION ------------------------------- #
def search():
    # print("Search is working...")
    search_w = w_entry.get().title()
    try:
        with open("data.json",'r') as data_file:
            data = json.load(data_file)
            # print(data["Mahesh"])

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message = "No data file found...")

    else:
        keys = [k_name.title() for (k_name, word) in data.items()]
        # print(keys)
        if search_w in keys:
            search_info = data[search_w]
            # print(search_info)
            messagebox.showinfo(title=f"{search_w}.",message = f"Email : {search_info['email']} \n Password: {search_info['password']}")
        else:
            messagebox.showinfo(title="Opps",message = f"No data found with website {search_w}")
  
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_pass():
    p_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    p_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = w_entry.get()
    email = e_entry.get()
    password = p_entry.get()
    new_data = {
        website.title():{
            "email":email,
            "password":password,
        },
    }

    if len(website)==0 or len(password) == 0:
        messagebox.showinfo(title="Opps",message="Please make sure you haven't left any field empty...")
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the detailed entered:\n Email: {email} \n Password: {password}\n Is it ok to save?")

        if is_ok:
            try:    
                with open("data.json","r") as data_file:
                    # data_file.write(f"{website} | {email} | {password}\n")
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    json.dump(new_data,data_file)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data, data_file,indent=4)
            finally:
                w_entry.delete(0,END)
                p_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- # 

window = Tk()
window.title("Password Manager...")
window.config(padx=30, pady=30)
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

w_label = Label(text="Website")
w_label.grid(column=0, row=1)
w_label.config(padx=10,pady=10)

u_label = Label(text="Email/Username")
u_label.grid(column=0,row=2)
u_label.config(padx=10,pady=10)


p_label = Label(text="Password")
p_label.grid(column=0,row=3)
p_label.config(padx=10,pady=10)


# Entry
w_entry = Entry(width=34)
w_entry.grid(column=1, row=1)
# w_entry.config(padx=10,pady=10)
w_entry.focus()

e_entry = Entry(width=55)
e_entry.grid(column=1, row=2, columnspan=2)
e_entry.insert(0,"maheshbunage@gmail.com")
# e_entry.config(padx=10,pady=10)


p_entry = Entry(width=34)
p_entry.grid(column=1, row=3)
# p_entry.config(padx=10,pady=10)

# Buttons
generate_pass_btn = Button(text="Generate Password",width=16,command=generate_pass,bg="white")
generate_pass_btn.grid(column=2, row=3)

btn_add = Button(text='Add', width=46, command=save,bg="white")
btn_add.grid(column=1, row=4, columnspan=2)


s_entry = Button(text="Search",width=16,command=search,bg="white")
s_entry.grid(column=2,row=1)

window.mainloop()
