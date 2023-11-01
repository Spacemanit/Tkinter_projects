# Paint App

from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("MB Paint")
root.minsize(100, 100)
root.geometry("1500x800+0+0")
colours = Frame(root)
colours.pack(side = TOP)
colour = [(0, 0, 0), "#000000"]
size = StringVar()

def choose_color():
	global colour
	colour = list(colorchooser.askcolor(title = "Colour"))

def col(c):
	global colour
	if c == "Green":
		colour = [(0,128,0), '#008000']
	if c == "Black":
		colour = [(0,0,0), '#000000']
	if c == "Yellow":
		colour = [(255,255,0), "#ffff00"]
	if c == "Orange":
		colour = [(255,165,0), "#ffa500"]
	if c == "Pink":
		colour = [(255,192,203), "#ffc0cb"]
	if c == "Blue":
		colour = [(0,0,255), "#0000ff"]
	if c == "White":
		colour = [(255,255,255), "#ffffff"]
	if c == "Red":
		colour = [(255,0,0), "#ff0000"]
	if c == "Custom":
		choose_color()

def paint(event):
	sizeint = size.get()
	x1, y1, x2, y2 = ( event.x - int(sizeint) ),( event.y - int(sizeint) ), ( event.x + int(sizeint) ),( event.y + int(sizeint) )
	global colour
	w.create_oval( x1, y1, x2, y2, fill = colour[1], outline=colour[1])

w = Canvas(root,background="White", bd = 7, relief="groove")
b1 = Button(colours, text = "   ", command = lambda:col("Green"), background="Green",).pack(side = LEFT)
b2 = Button(colours, text = "   ", command = lambda:col("Black"), background="Black",).pack(side = LEFT)
b3 = Button(colours, text = "   ", command = lambda:col("Yellow"), background="Yellow",).pack(side = LEFT)
b4 = Button(colours, text = "   ", command = lambda:col("Orange"), background="Orange",).pack(side = LEFT)
b5 = Button(colours, text = "   ", command = lambda:col("Pink"), background="Pink",).pack(side = LEFT)
b6 = Button(colours, text = "   ", command = lambda:col("Blue"), background="Blue",).pack(side = LEFT)
b7 = Button(colours, text = "   ", command = lambda:col("White"), background="White",).pack(side = LEFT)
b8 = Button(colours, text = "   ", command = lambda:col("Red"), background="Red",).pack(side = LEFT)
bcustom = Button(colours, text = " C ", command = lambda:col("Custom"), background="White").pack(side = LEFT)
sp = Spinbox(colours, textvariable=size, from_= 1, to = 50).pack(side=LEFT)
w.bind("<B1-Motion>", paint)
w.pack(side = BOTTOM, fill=BOTH, expand=True)

mainloop()