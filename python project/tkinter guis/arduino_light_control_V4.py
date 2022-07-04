from tkinter import * #GUI Libary 
import time
import serial # Serial communication libary

com= input("Enter the COM:")# com port 
baud= int(input("Enter the baudh:")) #baudh rate

serialcom= serial.Serial(com, baud)
serialcom.timeout = 1                  


root= Tk()

#to know number of LEDs we use a list

def add(): #function for adding object
    global LEDs #global list of LEDs
    LEDs=((select.get()).split(",")) #seperator for list 
    print(LEDs)
    on['state']= "active"
    off['state']= "active"
    clear['state']= "active"
    return LEDs

def clear():
    LEDs.clear() #remove content of LEDs
    print(LEDs)
    add['state']= "active"
    on['state']= "disabled"
    off['state']= "disabled"
    clear['state']= "disabled"
    select.delete(0,'end')

def on():
    zero['state']="active"
    print(LEDs)
    for i in range(len(LEDs)): #make a loop size of LEDs 
        if (LEDs[i] == '1'): #get the first object in list and get what it is
            print("1 is on")
            one= 'one'
            time.sleep(0.5)
            serialcom.write(one.encode()) #Thats how you should send data
            time.sleep(1)#delay so things work
        elif (LEDs[i] == '2'):
            print("2 is on")
            two= 'two'
            time.sleep(0.5)
            serialcom.write(two.encode())
            time.sleep(1)
        elif (LEDs[i] == '3'):
            print("3 is on")
            three= 'three'
            time.sleep(0.5)
            serialcom.write(three.encode())
            time.sleep(1)
        else:
            print("??")

def off():
    print(LEDs)
    for i in range(len(LEDs)):
        if (LEDs[i] == '1'): #same method
            print("1 is off")
            oneoff= 'oneoff'#variable name 
            time.sleep(0.5)
            serialcom.write(oneoff.encode()) #write the variable
            time.sleep(1)
        elif (LEDs[i] == '2'):
            print("2 is off")
            twooff= 'twooff'
            time.sleep(0.5)
            serialcom.write(twooff.encode())
            time.sleep(1)
        elif (LEDs[i] == '3'):
            print("3 is off")
            threeoff= 'threeoff'
            time.sleep(0.5)
            serialcom.write(threeoff.encode())
            time.sleep(1)
        else:
            print("??")

def zero():
    zero='zero'
    serialcom.write(zero.encode())
    

#Make and Place everything

welcom= Label(root, text="Select The Leds", bg= "white")
welcom.grid(row=0, column=0)


select= Entry(root)
select.grid(row=2, column=1)

add= Button(root, text="Add", bg="white", command=add)
add.grid(row=3, column=1)

on= Button(root, text="On", padx=5, pady=5, state=DISABLED, command= on)
on.grid(row=4, column=0)

off= Button(root, text="Off", padx=5, pady=5, state=DISABLED,command=off)
off.grid(row=4, column=1)

clear= Button(root, text="Clear", padx=5, pady=8, state=DISABLED,command= clear)
clear.grid(row=4, column=2)

zero= Button(root, text="Zero", padx=5, pady=5, state= DISABLED, command=zero)
zero.grid(row=4, column=3)
root.mainloop()
