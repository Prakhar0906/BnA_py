from tkinter import *

root = Tk()

e= Entry(root,width= 10, bg="yellow", fg= "blue")
e.pack()

def myClick():
    m=e.get()
    if (m == 'l'):
        myLabel= Label(root, text="Hi")
        myLabel.pack()
    else:
        bye= Label(root, text= "bye")
        bye.pack()
    
myButton= Button(root, text="Enter your Name", padx=50, pady=50, command= myClick)
myButton.pack()

myLable= Label(root, text="Hello World!")

myLable.pack()

root.mainloop()
