# importing tkinter module
from tkinter import * 
from tkinter.ttk import *
  
# creating tkinter window
root = Tk()
  
# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
              length = 100, mode = 'determinate')

def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
  
    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    if progress['value'] == 100:
        b.configure(text = "Done", command = root.destroy)
  
progress.pack(pady = 100, padx = 100)

b = Button(root, text = 'Start', command = bar)
b.pack(pady = 10, padx = 100)

mainloop()