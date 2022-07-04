from tkinter import *
import time
import serial


root= Tk()
serialcom= serial.Serial('COM5', 9600)
serialcom.timeout = 1


LEDs=[]

def add():
    LEDs.append(select.get())
    select.delete(0,'end')
    dis1= Label(root, text= LEDs)
    dis1.grid(row=7, column=9)
    on['state']="active"
    off['state']="active"
    clear['state']="active"
    zero['state']="active"
    

def clear():
    LEDs.clear()
    add['state']="active"
    

def on():
    t=len(LEDs)
    if t > 3:
        err= Label(root,text="You Do Not have More than 3 LEDS")
        err.grid(row=10,column=10)
    else:
        for i in range(len(LEDs)):
            o= LEDs[i]
            if o == '1':
                print(" 1 is on")
                one= 'one'
                time.sleep(0.5)
                serialcom.write(one.encode())
                time.sleep(1)
                
            elif o == '2':
                print(" 2 is on")
                time.sleep(0.5)
                two= 'two'
                serialcom.write(two.encode())
                time.sleep(1)
                
            elif o == '3':
                print(" 3 is on")
                time.sleep(0.5)
                three='three'
                serialcom.write(three.encode())
                time.sleep(1)
                
            else:
                print("The Number you entered is Not avaliable")

def off():
    t=len(LEDs)
    if t > 3:
        err= Label(root,text="You Do Not have More than 3 LEDS")
        err.grid(row=10,column=10)
    else:
        for i in range(len(LEDs)):
            o= LEDs[i]
            if o=='1':
                oneoff='oneoff'
                print("1 is off")
                time.sleep(0.5)
                serialcom.write(oneoff.encode())
                time.sleep(1)
            elif o=='2':
                print("2 is off")
                twooff='twooff'
                time.sleep(0.5)
                serialcom.write(twooff.encode())
                time.sleep(1)
            elif o=='3':
                print("3 is off")
                time.sleep(0.5)
                threeoff='threeoff'
                serialcom.write(threeoff.encode())
                time.sleep(1)
            else:
                print("not avaliable")

def zero():
    zero='zero'
    time.sleep(0.5)
    serialcom.write(zero.encode())
    time.sleep(0.5)
     

led1= Label(root, text="LED1", bg= "white")
led1.grid(row=0, column=0)
led2= Label(root, text="LED2", bg= "white")
led2.grid(row=0, column=1)
led3= Label(root, text="LED3", bg="white")
led3.grid(row=0, column=2)


select= Entry(root)
select.grid(row=3, column=5)

add= Button(root, text="Select", padx=10, pady=5, command= add)
add.grid(row=4, column=5)

on= Button(root, text="on",padx=5, pady=5,state= DISABLED, command=on)
on.grid(row=9, column=1)
off= Button(root, text="off", padx=5, pady=5,state= DISABLED, command=off)
off.grid(row=9, column=2)
zero= Button(root, text="Zero", padx=5, pady=5,state= DISABLED, command= zero)
zero.grid(row=9, column=3)

clear= Button(root, text="Clear", padx=5, pady=5, state=DISABLED, command= clear)
clear.grid(row=11, column=4)

root.mainloop()
