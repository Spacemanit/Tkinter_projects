from tkinter import *
import pandas as pd

root = Tk()
root.title("Spreadsheet App")
rows = 11
cols = 6

col_names = ["", "Name", "Physics", "Chemistry", "Maths", "English", "Computer", "Percentage"]
coulson = ["Physics", "Chemistry", "Maths", "English", "Computer"]
columnsss = ["Marksheet", "Name", "Physics", "Chemistry", "Maths", "English", "Computer", "Percentage"]
df = pd.DataFrame(index=range(rows), columns=col_names)
for i in range(8):
    label = Label(root, text = columnsss[i])
    label.grid(row = 0, column = i)
for i in range(1, 11):
    label = Label(root, text = i)
    label.grid(row = i, column = 0)

def update_df(event):
    row = event.widget.grid_info()["row"]
    col = event.widget.grid_info()["column"]
    value = event.widget.get()
    print(row, col)
    if col > 1:
        df.iloc[row, col] = float(value)
    else:
        df.iloc[row, col] = value
    df['Percentage'] = df[coulson].sum(axis = 1) / 5
    c = str(df.iat[row, 7]) + "%"
    for i in range(rows):
        label = Label(root)
        label.configure(text = c)
        label.grid(row = row, column = 7)


entries = []
for i in range(rows):
    row_entries = []
    for j in range(cols):
        entry = Entry(root)
        entry.grid(row = i + 1, column = j + 1)
        entry.bind("<Tab>", update_df)
        row_entries.append(entry)
    entries.append(row_entries)

def save_csv():
    file_name = input("Enter a file name: ")
    if not file_name.endswith(".csv"):
        file_name += ".csv"
    df.to_csv(file_name, index=False)

save_button = Button(root, text="Save as xls", command=save_csv)
save_button.grid(row=rows, column=0, columnspan=8, sticky="ew")

root.mainloop()
