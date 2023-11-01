import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *

root = Tk()
root.geometry("200x320+100+100")
root.title("Tic Tac Toe")

frame = Frame(root)
frame.pack()
style = Style()
style.theme_use("classic")
style.configure('TLabel', font = ('calibri',30))
style.configure('TButton', font = ('calibri',30))
chance = StringVar()
chance = "X"
plays = 0
def bp(key):
    global chance, plays
    if chance == "Y":
        chance = "X"
        ch.configure(text = "Y Plays")
    elif chance == "X":
        chance = "Y"
        ch.configure(text = "X Plays")
    plays += 1
    if key == "11":
        b1.configure(text = chance)
    elif key == "12":
        b2.configure(text = chance)
    elif key == "13":
        b3.configure(text = chance)
    elif key == "21":
        b4.configure(text = chance)
    elif key == "22":
        b5.configure(text = chance)
    elif key == "23":
        b6.configure(text = chance)
    elif key == "31":
        b7.configure(text = chance)
    elif key == "32":
        b8.configure(text = chance)
    elif key == "33":
        b9.configure(text = chance)
    win()
    
def win():
    p1 = b1.cget('text')
    p2 = b2.cget('text')
    p3 = b3.cget('text')
    p4 = b4.cget('text')
    p5 = b5.cget('text')
    p6 = b6.cget('text')
    p7 = b7.cget('text')
    p8 = b8.cget('text')
    p9 = b9.cget('text')
    if p1==p2==p3!="   " or p4==p5==p6!="   " or p7==p8==p9!="   " or p1==p5==p9!="   " or p3==p5==p7!="   " or p1==p4==p7!="   " or p2==p5==p8!="   " or p3==p6==p9!="   ":
        showinfo("Victory", chance + " Wins!")
        root.destroy()
    elif plays == 9:
        showinfo("Tie", "Both players are of equal match")
        root.destroy()

l = Label(frame, text = " Tic Tac Toe ").grid(row=0, column=0, columnspan=3)
b1 = Button(frame, text = "   ", command = lambda:bp("11"))
b2 = Button(frame, text = "   ", command = lambda:bp("12"))
b3 = Button(frame, text = "   ", command = lambda:bp("13"))
b4 = Button(frame, text = "   ", command = lambda:bp("21"))
b5 = Button(frame, text = "   ", command = lambda:bp("22"))
b6 = Button(frame, text = "   ", command = lambda:bp("23"))
b7 = Button(frame, text = "   ", command = lambda:bp("31"))
b8 = Button(frame, text = "   ", command = lambda:bp("32"))
b9 = Button(frame, text = "   ", command = lambda:bp("33"))
ch = Label(frame, text = "Y Plays")

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
ch.grid(row=4, column=0, columnspan=3)
win()
frame.mainloop()