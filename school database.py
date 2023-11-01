from tkinter import *
import pandas as pd

root = Tk()
root.title("Spreadsheet App")

rows = 10
cols = 6

col_names = ["Name", "Physics", "Chemistry", "Maths", "English", "Computer", "Percentage"]
colson = ["Physics", "Chemistry", "Maths", "English", "Computer"]

df = pd.DataFrame(index=range(rows), columns=col_names)

def update_df(event):
    row = event.widget.grid_info()["row"]
    col = event.widget.grid_info()["column"]
    value = event.widget.get()
    df.iloc[row, col] = int(value)
    df['Percentage'] = df[colson].sum(axis = 1)
    c = df.iat[row, 6] / 5
    for i in range(rows):
        label = Label(root, text = c)
        label.grid(row = row, column = 7)

entries = []
for i in range(rows):
    row_entries = []
    for j in range(cols):
        entry = Entry(root)
        entry.grid(row=i, column=j)
        entry.bind("<Tab>", update_df)
        row_entries.append(entry)
    entries.append(row_entries)

def save_csv():
    file_name = input("Enter a file name: ")
    if not file_name.endswith(".xls"):
        file_name += ".xls"
    df.to_csv(file_name, index=False)

save_button = Button(root, text="Save as xls", command=save_csv)
save_button.grid(row=rows, column=0, columnspan=cols, sticky="ew")

root.mainloop()
