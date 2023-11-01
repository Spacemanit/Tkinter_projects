# Import tkinter and pandas
from tkinter import *
import pandas as pd

# Create a root window
root = Tk()
root.title("Spreadsheet App")

# Define the number of rows and columns
rows = 10
cols = 6

# Create a list of column names
col_names = ["Name", "Physics", "Chemistry", "Maths", "English", "Computer", "Percentage"]
colson = ["Physics", "Chemistry", "Maths", "English", "Computer"]
# Create a dataframe to store the cell values
df = pd.DataFrame(index=range(rows), columns=col_names)
# Define a function to update the dataframe when a cell is edited
def update_df(event):
    # Get the row and column of the edited cell
    row = event.widget.grid_info()["row"]
    col = event.widget.grid_info()["column"]
    # Get the new value of the cell
    value = event.widget.get()
    # Update the dataframe with the new value
    df.iloc[row, col] = int(value)
    df['Percentage'] = df[colson].sum(axis = 1)
    c = df.iat[row, 6] / 5
    for i in range(rows):
        label = Label(root, text = c)
        label.grid(row = row, column = 7)

# Create a grid of entry widgets
entries = []
for i in range(rows):
    row_entries = []
    for j in range(cols):
        # Create an entry widget
        entry = Entry(root)
        # Place it on the grid
        entry.grid(row=i, column=j)
        # Bind the return key to update the dataframe
        entry.bind("<Tab>", update_df)
        # Append it to the row list
        row_entries.append(entry)
    # Append the row list to the entries list
    entries.append(row_entries)

# Define a function to save the dataframe as a csv file
def save_csv():
    # Ask the user for a file name
    file_name = input("Enter a file name: ")
    # Add the .csv extension if not present
    if not file_name.endswith(".xls"):
        file_name += ".xls"
    # Save the dataframe as a csv file
    df.to_csv(file_name, index=False)

# Create a button to save the dataframe as a csv file
save_button = Button(root, text="Save as xls", command=save_csv)
save_button.grid(row=rows, column=0, columnspan=cols, sticky="ew")

# Start the main loop
root.mainloop()
