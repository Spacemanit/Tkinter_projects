from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
import math

root = Tk()
root.title("Marksheet")

n = StringVar
label = Label(root, text = "Enter number of students: ").grid(row = 0, column = 0)
df = pd.DataFrame()
rowAsk = Combobox(root, width = 20, textvariable = n)
rowAsk.grid(row = 0, column = 1)
rowAsk['values'] = (1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80)
rowAsk.current(4)

def generation(bol, df):
    coulson = ["R.no.", "Name", "Physics", "Chemistry", "Maths", "English", "Computer", "Percentage"]
    cols = 7
    if bol:
        rows = df.shape[0]
    else:
        rows = int(rowAsk.get())
        df = pd.DataFrame(index = range(1, rows + 1), columns = coulson)
    for i in root.grid_slaves():
        i.destroy()
    
    fileName = Entry(root)
    fileName.grid(row=rows + 2, column=0)
    
    def save_csv():
        file_name = str(fileName.get()) + ".csv"
        df.to_csv(file_name, index=False)
    save_button = Button(root, text="Save file", command=save_csv)
    save_button.grid(row=rows + 2, column=1)

    def update_df(event):
        row = event.widget.grid_info()["row"]
        col = event.widget.grid_info()["column"]
        value = event.widget.get()
        if col > 1:
            df.iloc[row - 1, col] = float(value)
        else:
            df.iloc[row - 1, col] = value
        df['Percentage'] = df[coulson[2:7]].sum(axis = 1) / 5
        for i in range(rows):
            label = Label(root, text = df.iloc[i, 7]).grid(row = i + 1, column = 7)
        print(df)
        ranker()
    
    for i in range(cols + 1):
        label = Label(root, text = coulson[i])
        label.grid(row = 0, column = i)
    for i in range(rows):
        df.iloc[i, 7] = 0.0
        df.iloc[i, 0] = i + 1
        for j in range(cols):
            entry = Entry(root)
            if j > 1 and not math.isnan(df.iloc[i, j]):
                entry.insert(0, df.iloc[i, j])
            elif j <= 1:
                entry.insert(0, df.iloc[i, j])
            entry.grid(row = i + 1, column = j)
            entry.bind("<FocusOut>", update_df)
    
    def ranker():
        percentages = list(df["Percentage"])
        names = list(df["Name"])
        combined = []
        for i in range(rows):
            temp = [names[i], percentages[i]]
            combined.append(temp)
        l = len(combined)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (combined[j][1] > combined[j + 1][1]):
                    tempo = combined[j]
                    combined[j] = combined[j + 1]
                    combined[j + 1] = tempo
        print(combined)
        for i in range(3):
            name = combined[l - i - 1][0]
            label = Label(root, text = "Rank " + str(i + 1) + ": "+ str(name)).grid(row = rows + 1, column = i)

button = Button(root, text = "Generate Marksheet", command = lambda:generation(False, df))
button.grid(row = 1, column = 0, columnspan = 2)

fileName = Entry(root)
fileName.grid(row = 2, column = 0)

def open_csv():
    global df, dfchk
    file_name = str(fileName.get()) + ".csv"
    df = pd.read_csv(file_name)
    generation(True, df)

open_button = Button(root, text="Open from .csv", command = open_csv)
open_button.grid(row = 2, column = 2)

root.mainloop()