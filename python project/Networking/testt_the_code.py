
import socket
from tkinter import *

root= Tk()
root.title('Control server')
#root.geometry("250x250")

HEADER= 10
PORT= 5050
IP= socket.gethostbyname(socket.gethostname())
ADDR= (IP, PORT)

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

ips=[]
names=[]
Addresses=[]

class nodeCreate:
    def __init__(self, ip, name):
        global Name 
        self.ip= ip
        self.name=name 
        #name= name
        Addresses.append(name)
        print(Addresses)
        Name = Button(device_show, text= name, bg= "red", command= lambda: view(name))
        Name.pack()
        names.append(Name)
        
    def delete_node(Name):
        print(f"I will be forgetting {Name}")
        #node_name.__class__  = Button
        #node_name.pack_forget()
        for i in names:
            name= i['text']
            if name == Name:
                i.destroy()
                names.remove(i)
    def node_verify(self):
        pass

        
class nodeManage:
    def new():
        top= Toplevel()
        text= Label(top, text="Enter the Data")
        text.grid(row=1, column=1)# starting row 1 column 1 
        namedes= Label(top, text="Enter the name")
        namedes.grid(row=2, column=1)
        name= Entry(top)
        name.grid(row=2, column=2)
        ipdes= Label(top, text="Enter the ip")
        ipdes.grid(row=3, column=1)# same row column 1
        ip= Entry(top)
        ip.grid(row=3, column=2 ) #same row column  2 
        ok= Button(top, text="ok", command= lambda: nodeCreate(ip.get(), name.get()))
        ok.grid(row=4, column=3)

def delete():
    global name 
    top= Toplevel()
    text= Label(top, text="Enter the name")
    text.grid(row=1, column=1)
    name= Entry(top)
    name.grid(row=2, column= 1)
    ok= Button(top, text="Ok", command= lambda: nodeCreate.delete_node( name.get()))
    ok.grid(row=3, column=2)
        
def view(name):
    print(name)

        
device_show= LabelFrame(root, text="select", padx= 50, pady= 50)
device_show.pack()
devices_label= Label(device_show, text="Your nodes")
devices_label.pack()

welcom= Label(root, text="Welcom")
welcom.pack()
add= Button(root, text="Add client", command= nodeManage.new)
add.pack()
delete_device= Button(root, text="delete", command= delete)
delete_device.pack()

#connect= Button(root, text="Connect")
#connect.pack()
