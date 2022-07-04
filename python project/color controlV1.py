from tkinter import *
import serial
import time

root= Tk()
serialcom= serial.Serial('COM5', 9600)
serialcom.timeout = 1

root.title("colorControl")
root.geometry("400x400")

def send():
    print(v1.get())
    print(v2.get())
    print(v3.get())
    redval= str(v1.get())
    greenval= str(v2.get())
    blueval= str(v3.get())
    serialcom.write(redval.encode())
    time.sleep(2)
    serialcom.write(greenval.encode())
    time.sleep(2)
    serialcom.write(blueval.encode())

def off():
    off='off'
    serialcom.write(off.encode())
    time.sleep(0.5)

welcom= Label(root, text="Adjust the Sliders to control The color")
welcom.grid(row=0,column=3)

v1 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v1.grid(row=3, column=3)
v2 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v2.grid(row=4, column=3)
v3 = Scale(root, from_=0,to=255,orient= HORIZONTAL)
v3.grid(row=5, column=3)

send= Button(root, text="Send", padx=10, pady=10, command=send)
send.grid(row=6, column=3)
off= Button(root, text="Off", padx=10, pady=10, command=off)
off.grid(row=7, column=3)

root.mainloop()



