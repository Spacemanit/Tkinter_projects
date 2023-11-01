from tkinter import *
from tkinter.ttk import *
import random

# FUNCTIONS
def add():
    a = complex(t1.get())
    b = complex(t2.get())
    c = a + b
    if str(c)[-4:-1:1] == "+0j":
        txt = "Answer: " + str(c)[1:-4]
    else:
        txt = "Answer: " + str(c)[0:-1]
    ans.configure(text = txt)

def diff():
    a = complex(t1.get())
    b = complex(t2.get())
    c = a - b
    if str(c)[-4:-1:1] == "+0j":
        txt = "Answer: " + str(c)[1:-4]
    else:
        txt = "Answer: " + str(c)[1:-1]
    ans.configure(text = txt)

def prod():
    a = complex(t1.get())
    b = complex(t2.get())
    c = a * b
    if str(c)[-4:-1:1] == "+0j":
        txt = "Answer: " + str(c)[1:-4]
    else:
        txt = "Answer: " + str(c)[1:-1]
    ans.configure(text = txt)

def div():
    a = complex(t1.get())
    b = complex(t2.get())
    try:
        c = a / b
        if str(c)[-4:-1:1] == "+0j":
            txt = "Answer: " + str(c)[1:-4]
        else:
            txt = "Answer: " + str(c)[1:-1]
    except(ZeroDivisionError):
        txt = "Answer: NOT POSSIBLE"
    
    ans.configure(text = txt)

def quiz():
    root = Tk()
    root.geometry("200x200")
    root.title("Quiz")
    
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    ch = ["+", "-", "*", "/"]
    op = random.choice(ch)
    question = "What is: " + str(x) + op + str(y) + "\nRounded to two decimal places"
    def Take_input(x, y, op):
        INPUT = int(inputtxt.get())
        if op == "+" and INPUT == (x + y):
            Output.configure(text = 'Correct')
        elif op == "-" and INPUT == x - y:
            Output.configure(text = 'Correct')
        elif op == "*" and INPUT == x * y:
            Output.configure(text = 'Correct')
        elif op == "/" and INPUT == round(x / y, 2):
            Output.configure(text = 'Correct')
        else:
            Output.configure(text = "Wrong answer")
    
    # STYLES
    style = Style()
    style.configure('TButton', font = ('calibri', 20, 'bold'), foreground = 'Black')
    style.configure('TLabel', font = ('calibri', 20), foreground = 'Black')
    style.configure('Entry', font = ('calibri', 20, 'bold'), foreground = 'Black')
    style.map('TButton', foreground = [('active', 'disabled', 'Blue')], background = [('disabled', '')])
    
    l = Label(root, text = question, style = "TLabel")
    inputtxt = Entry(root)
    Output = Label(root, style = "TLabel")
    Display = Button(root, style = "TButton", text ="Show", command = lambda:Take_input(x, y, op))
    l.grid(row = 0, column = 0)
    inputtxt.grid(row = 1, column = 0, padx = 10, pady = 10)
    Output.grid(row = 3, column = 0, padx = 10, pady = 10)
    Display.grid(row = 2, column = 0, padx = 10, pady = 10)
    root.mainloop()

def cBO():
    op = operation.get()
    if op == "Addition":
        b.configure(text = "Sum", command = add)
    if op == "Subtraction":
        b.configure(text = "Difference", command = diff)
    if op == "Multiplication":
        b.configure(text = "Product", command = prod)
    if op == "Division":
        b.configure(text = "Division", command = div)
    if op == "Quiz":
        quiz()

# FRAME INITIALIZATION
frame = Tk()
frame.geometry("600x600")
frame.title("Calculator")

# STYLES
style = Style()
style.theme_use("classic")

# INITIALISATION
n = StringVar()
operation = Combobox(frame, width = 27, textvariable = n, font = ("calibri", 10))
l1 = Label(frame, text = "Enter first number: ")
l2 = Label(frame, text = "Enter second number: ")
t1 = Entry(frame, font = ("calibri", 20))
t2 = Entry(frame, font = ("calibri", 20))
go = Button(frame, text = "GO", command = cBO)
quitb = Button(frame, text = "Quit", command = frame.destroy)
b = Button(frame, text = "Sum", command = add).grid(row = 3, column = 1, padx = 10, pady = 10)
ans = Label(frame)

# POSITIONS
operation.grid(row = 0, column = 0, padx = 10, pady = 10)
l1.grid(row = 1, column = 0, padx = 10, pady = 10)
l2.grid(row = 2, column = 0, padx = 10, pady = 10)
t1.grid(row = 1, column = 1, padx = 10, pady = 10)
t2.grid(row = 2, column = 1, padx = 10, pady = 10)
quitb.grid(row = 3, column = 0, padx=10, pady=10)
go.grid(row = 0, column = 1, padx = 10, pady = 10)
ans.grid(row = 4, column = 1, padx = 10, pady = 10)

operation['values'] = ("Addition", "Subtraction", "Multiplication", "Division", "Quiz")
operation.current(0)

frame.mainloop()