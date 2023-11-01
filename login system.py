# Login System

import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x300")

l1 = Label(root, text = "Username: ")
l1.grid(row = 0, column = 0)
l2 = Label(root, text = "Password: ")
l2.grid(row = 1, column = 0)
u = Entry(root)
u.grid(row = 0, column = 1)
p = Entry(root)
p.grid(row = 1, column = 1)

def login():
    username = str(u.get())
    password = str(p.get())
    file = open("Accounts.txt", "r")
    for line in file:
        temp = line.strip("\n").split(",")
        if username == temp[0] and password == temp[1]:
            print("Your Login Credentials have been Verified")
            return 1
    prompt = messagebox.showerror(title = "Error!", message = "Incorrect Login Details")
    return 0

def register():
    file = open("Accounts.txt", "r+")
    username = str(u.get())
    password = str(p.get())
    bol = True
    for line in file:
        temp = line.strip("\n").split(",")
        if username == temp[0] and password == temp[1]:
            bol = False
            return 0
        bol = True
    if bol:
        txt = "\n" + username + "," + password
        file.write(txt)
        file.close()
    

b = Button(root, text = "Login", command = login)
b.grid(row = 2, column = 1)
reg = Button(root, text = "Register", command = register)
reg.grid(row = 2, column = 0)

root.mainloop()