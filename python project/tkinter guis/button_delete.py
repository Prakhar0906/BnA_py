from tkinter import *

root= Tk()

ips=[]
names=[]

class nodeCreate:
    def __init__(self, ip, name):
        global Name 
        self.ip= ip
        self.name=name 
        Name = Button(device_show, text= name, bg= "red", command= lambda: view(name))
        Name.pack()
        names.append(Name)
        ips.append(ip)
    def delete_node(Name):
        print(f"I will be deleating {Name}")
        for i in names:
            name= i['text']
            #print(i)
            #print(name)
            if name == Name:
                i.destroy()
                names.remove(i)
        #for i in names:   #debugging 
            #new_names= i['text']
            #print(new_names)
            

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
    def delete_node():
        top= Toplevel()
        info= Label(top, text="Enter the button name")
        info.grid(row=1, column=1)
        Target= Entry(top)
        Target.grid(row=1, column=2)
        ok= Button(top, text="ok", command= lambda: nodeCreate.delete_node(Target.get()))
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
delete_device= Button(root, text="delete", command= nodeManage.delete_node)
delete_device.pack()
