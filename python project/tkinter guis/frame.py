from tkinter import *
from tkinter import messagebox

root= Tk()
root.title('Frame')

def popup():
    messagebox.showinfo("??","I said you don't click the button")

frame= LabelFrame(root, text="This is my frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b= Button(frame, text="Dont click me!", command=popup)
b.pack()

root.mainloop()
