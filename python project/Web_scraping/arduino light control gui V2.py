import serial
import time
from tkinter import *

root= Tk()

LEDs=[]

serialcom= serial.Serial('COM5', 9600)
serialcom.timeout = 1

state1=0
state2=0
state3=0

def led1():
    Led1_button['bg']= 'lightblue'
    if state1 != 0:
        state1=0
        xi='oneoff'
        serialcom.write(xi.encode())
    else:
        state1=1
        i= 'one'
        serialcom.write(i.encode())
        time.sleep(0.5)
        
        

def led2():
    Led2_button['bg']= 'lightblue'
    if state2 != 0:
        state2=0
    else:
        state2=1
        b= 'two'
        serialcom.write(b.encode())
        time.sleep(0.5)
        

def led3():
    Led3_button['bg']= 'lightblue'
    if state3 != 0:
        state3=0
    else:
        state3=1
        c= 'three'
        serialcom.write(c.encode())
        time.sleep(0.5)

def display():
    dis= Label(root, text=LEDs)
    dis.grid(row=15, column=3)
    
    
intro= Label(root, text="Select The LEDs")
intro.grid(row=1, column=1)

Led1_button= Button(root, text= 1, padx=10, pady=10,bg="white", command= led1)
Led1_button.grid(row=5, column=0)

Led2_button= Button(root, text= 2, padx=10, pady=10,bg= "white", command= led2)
Led2_button.grid(row=5, column=1)

Led3_button= Button(root, text=3, padx= 10, pady=10,bg="white",command= led3)
Led3_button.grid(row=5, column=3)

Select= Button(root, text="select", padx=5, pady=20,command= display)
Select.grid(row=10, column=5)

