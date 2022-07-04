import serial
import time
from tkinter import *

root= Tk()
serialcom= serial.Serial('COM5', 9600)
serialcom.timeout = 1

def send_1() :
    i= 'one'
    serialcom.write(i.encode())
    time.sleep(0.5)
    onelable= Label(root, text= serialcom.readline().decode('ascii'))
    onelable.pack()

def send_2() :
    b= 'two'
    serialcom.write(b.encode())
    time.sleep(0.5)
    twolable= Label(root, text= serialcom.readline().decode('ascii'))
    twolable.pack()

def send_3() :
    c= 'three'
    serialcom.write(c.encode())
    time.sleep(0.5)
    threelable= Label(root, text= serialcom.readline().decode('ascii'))
    threelable.pack()

def done() :
    d= 'zero'
    done= Label(root, text="Done The Program")
    done.pack()
    serialcom.write(d.encode())
    serialcom.close()

def off_1():
    offone= 'oneoff'
    serialcom.write(offone.encode())
    time.sleep(0.5)
    oneofflab= Label(root, text="Led 1 is Off")
    oneofflab.pack()

def off_2():
    offtwo= 'twooff'
    serialcom.write(offtwo.encode())
    time.sleep(0.5)
    twoofflab= Label(root, text="Led 2 is Off")
    twoofflab.pack()

def off_3():
    offthree= 'threeoff'
    serialcom.write(offthree.encode())
    time.sleep(0.5)
    threeofflab= Label(root, text="Led 1 is Off")
    threeofflab.pack()
    

button_1= Button(root, text="1", padx= 10, pady= 10, command= send_1)
button_1.pack()

button_2= Button(root, text="2", padx= 10, pady= 10, command= send_2)
button_2.pack()

button_2= Button(root, text="3", padx= 10, pady= 10, command= send_3)
button_2.pack()

button_3= Button(root, text="Complete", padx= 20, pady=5, command= done)
button_3.pack()

led_1_off= Button(root, text="turn off one",padx= 20, pady= 20, command= off_1)
led_1_off.pack()

led_2_off= Button(root, text="turn off teo",padx= 20, pady= 20, command= off_2)
led_2_off.pack()

led_3_off= Button(root, text="turn off three",padx= 20, pady= 20, command= off_3)
led_3_off.pack()
