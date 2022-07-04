from tkinter import *

root= Tk()
root.title("Simple Calculator")

e= Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def num(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+ str(number))
    
    

def add():
    global ans
    global num
    global pre 
    num= e.get()
    ans= pre+num
    pre=ans 
    e.delete(0,END)

def clear():
    e.delete(0,END)

def equal():
    e.delete(0,END)
    e.insert(0,pre)

pre= e.get()

b1= Button(root, text="1", padx=40, pady=20, command=lambda: num(1))
b2= Button(root, text="2", padx=40, pady=20, command=lambda: num(2))
b3= Button(root, text="3", padx=40, pady=20, command=lambda: num(3))
b4= Button(root, text="4", padx=40, pady=20, command=lambda: num(4))
b5= Button(root, text="5", padx=40, pady=20, command=lambda: num(5))
b6= Button(root, text="6", padx=40, pady=20, command=lambda: num(6))
b7= Button(root, text="7", padx=40, pady=20, command=lambda: num(7))
b8= Button(root, text="8", padx=40, pady=20, command=lambda: num(8))
b9= Button(root, text="9", padx=40, pady=20, command=lambda: num(9))
b0= Button(root, text="0", padx=40, pady=20, command=lambda: num(0))
add= Button(root, text="+", padx=20, pady=20, command=add)
equal= Button(root, text="=", padx=20, pady=20, command=add)
clear= Button(root, text="Clear", padx=10, pady=20, command=clear)

b1.grid(row=3 ,column=0)
b2.grid(row=3 ,column=1)
b3.grid(row=3 ,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row=2 ,column=2)

b7.grid(row=1 ,column=0)
b8.grid(row=1 ,column=1)
b9.grid(row=1 ,column=2)

b0.grid(row=4 ,column=0)

add.grid(row=5, column=0)
equal.grid(row=5, column=2)
clear.grid(row=5, columnspan=2)




