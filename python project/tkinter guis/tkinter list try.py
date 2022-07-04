import time
from tkinter import *

root= Tk()

LEDs=[]

def add():
    Led_dat= led_num.get()
    LEDs.append(Led_dat)
    dis= Label(root, text= LEDs)
    dis.pack()

ent= Label(root, text="Enter the numbers")
ent.pack()

led_num= Entry(root)
led_num.pack()


add= Button(root, text="ADD", padx=5, pady=10, command=add)
add.pack()
