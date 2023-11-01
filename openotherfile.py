from tkinter import *
from tkinter.ttk import *

from tkinter.filedialog import askopenfile, asksaveasfile

root = Tk()
root.geometry('200x100')

def open_file():
	file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
	if file is not None:
		content = file.read()   
		print(content)

btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

def save():
	files = [('All Files', '*.*'),
			('Python Files', '*.py'),
			('Text Document', '*.txt')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
btn2 = Button(root, text = 'Save', command = lambda : save())
btn2.pack(side = TOP, pady = 20)


mainloop()


mainloop()
