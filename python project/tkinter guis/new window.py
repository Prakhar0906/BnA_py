from tkinter import *

root= Tk()
root.title('Window')

def create():
    top= Toplevel()
    text= Label(top,text="Hello")
    text.pack()

b= Button(root, text="Click Me!", command= create)
b.pack()

mainloop()
