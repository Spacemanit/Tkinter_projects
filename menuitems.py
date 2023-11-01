# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.title('Menu Demonstration')
root.geometry("100x100")

# Creating Menubar
menubar = Menu(root)

menubutton = Menubutton(root, text = "Menu")   
    
menubutton.menu = Menu(menubutton)  
menubutton["menu"]= menubutton.menu  
  
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
  
menubutton.menu.add_checkbutton(label = "Courses",
                                variable = var1)  
menubutton.menu.add_checkbutton(label = "Students",
                                variable = var2)
menubutton.menu.add_checkbutton(label = "Careers",
                                variable = var3)
    
menubutton.pack()  

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
root.config(menu = menubar)
mainloop()
