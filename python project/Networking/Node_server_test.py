import socket
from tkinter import *

root= Tk()

HEADER= 10
PORT= 5050
IP= socket.gethostbyname(socket.gethostname())
ADDR= (IP, PORT)

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

ips= []
names_list= []
Addresses= []

class nodeCreate:
    def __init__(self, ip, name):
        self.ip= ip #get the ip in variable 
        self.name= name #get the ip in a variable 
        Addresses.append((name, ip)) # insert a tuplet of name and addresses in the list 
        print(Addresses)#debugging message 
        Name= Button(device_show, text= name, bg= "red", command= lambda:view(name)) #command to verify 
        Name.pack()
        names_list.append(Name)

    def delete_node(TarName):
        print(f"I will be forgetting {TarName}")
        for i in names_list: #go through each one 
            current = i['text'] #get the text of the button 
            if current == TarName: # if text is the selected target 
                i.destroy() #destroy iy 
                names_list.remove(i) #remove it from the list

        for i in names_list:
            remaining= i['text']
            print(remaining)

class nodeManage:
    def new():
        top= Toplevel()
        text= Label(top, text="Enter the data")
        text.grid(row=1, column=1)
        namedes= Label(top, text="Name")
        namedes.grid(row=2, column=1)
        name= Entry(top)
        name.grid(row=2, column=2)
        ipdes= Label(top, text="Enter the ip")
        ipdes.grid(row=3, column=1)
        ip= Entry(top)
        ip.grid(row=3, column=2)
        ok= Button(top, text="ok", command= lambda: nodeCreate(ip.get(), name.get()))
        ok.grid(row=4, column=3)

    def delete():
        global name
        top= Toplevel()
        text= Label(top, text="Enter the name")
        text.grid(row=1, column=1)
        name= Entry(top)
        name.grid(row=2, column=2)
        ok= Button(top, text="Ok", command= lambda: nodeCreate.delete_node( name.get()))
        ok.grid(row=3, column=3)

def view(name):
    print(name)


def start_server():
    server.listen()
    print(f"[LISTENING] on {IP}")
    while True:
        conn, addr= server.accept()
        msg= "Welcom"
        conn.send(msg.encode('utf-8'))

device_show= LabelFrame(root, text="Select", padx=50, pady=50)
device_show.pack()
device_label= Label(device_show, text="Your devices")
device_label.pack()

welcom= Label(root, text="Welcom")
welcom.pack()
add= Button(root, text="Add", command= nodeManage.new)
add.pack()
delete_device= Button(root, text="Delete Node", command= nodeManage.delete)
delete_device.pack()
