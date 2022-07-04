from tkinter import *

root= Tk()

root.title("Hmm Scales")

v1 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v1.pack()
v2 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v2.pack()
v3 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v3.pack()

root.mainloop()
