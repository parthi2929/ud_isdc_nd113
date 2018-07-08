from tkinter import *
from tkinter.colorchooser import *
def getColor():
    color = askcolor() 
    print(color)
Button(text='Select Color', command=getColor).pack()
mainloop()