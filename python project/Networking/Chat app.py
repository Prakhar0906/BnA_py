from tkinter import *
import socket
#Prakhar Laptop Ip 192.168.1.9
#Prajjwal IP 192.168.1.8
#sharad ip 192.168.1.5
root= Tk()
root.title('Chat app')
root.geometry("250x250")

FORMAT= "utf-8"
IP= socket.gethostbyname(socket.gethostname())
PORT= 5056
ADDR= (IP,PORT)
HEADER= 64

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

clients=[]
contacts={}
ip=[]
name=[]

def send_command():
    msg="Cliet verified"
    conn.send(msg.encode(FORMAT))
    conn.close()
    pass 

def verify(address):
    for i in range(len(clients)):
        tar= clients[i]
        print(f"{address} is trying to connect!")
        for i in range(len(ip)):
            if tar == ip[i]:
                print('valid connection')
                send_command()
            else:
                print(f"{address} was not authorised")
                clients.pop(int(tar))

def start():
    global conn
    server.listen()
    print(f"Server is listening on {IP}")
    while True:
        conn, addr= server.accept()
        address= addr[0]
        print(address)
        clients.append(address)
        verify(address)      


def ok(stir):
    global con
    global pre_ip
    global pre_name
    if (stir == 'add'):
        IP= askip.get()
        Name= askname.get()
        ip.append(IP)
        name.append(Name)
        contacts[Name]=IP
        askip.delete(0, 'end')
        askname.delete(0,'end')
        r= len(name)
        con= Button(window, text=Name, bg="red", command= lambda: val(Name))
        con.grid(row=r, column=2)
    elif (stir == 'delete'):
        target= target_Entery.get()
        print(target)
        contacts.pop(target)
        print(f"{target} has been removed from contacts")
        con.destroy()
        print(contacts)
    elif (stir == 'editini'):
        tar= editname_entry.get()
        select=contacts[tar]
        change_window= Toplevel()
        ask= Label(change_window, text="Change the info")
        ask.grid(row=1, column=0)
        pre_name= Entry(change_window)
        pre_ip= Entry(change_window)
        pre_name.grid(row=2, column=1)
        pre_ip.grid(row=3, column=1)
        pre_name.insert(0, tar)
        pre_ip.insert(0, select)
        confirm= Button(change_window, text="Ok", command= lambda: ok('setedit'))
        confirm.grid(row=4, column=2)
    elif (stir == 'setedit'):
        update={}
        new_ip= pre_ip.get()
        new_name= pre_name.get()
        update[new_name]= new_ip
        print(update)
        contacts.update(update)
        print(contacts)


def clos():
     pass
     
     
        
def add():
    global name
    global IP
    global askip
    global askname
    global top
    top= Toplevel()
    ask= Label(top, text="Enter the Information")
    ask.grid(row=0, column=0)
    quename= Label(top, text="Enter the name")
    quename.grid(row=1, column=0)
    queip= Label(top, text="Enter the Ip")
    queip.grid(row=2, column=0)
    askname= Entry(top)
    askname.grid(row=1,column=1)
    askip= Entry(top)
    askip.grid(row=2, column=1)
    okey= Button(top, text="Ok", command= lambda: ok('add'))
    okey.grid(row=3, column=1)
    close= Button(top, text="Close", command=clos)
    close.grid(row=3 ,column=2)

def mode(mode):
    global target_Entery
    global editname_entry
    if mode == 'delete':
        deletewindow= Toplevel()
        ask= Label(deletewindow, text="Select the target:")
        ask.grid(row=2, column=1)
        target_Entery= Entry(deletewindow)
        target_Entery.grid(row=2, column=2)
        conform= Button(deletewindow, text= "ok", command= lambda: ok('delete'))
        conform.grid(row=2, column=3)
    if mode == 'edit':
        editwindow= Toplevel()
        ask= Label(editwindow, text="Enter the record to be eddited")
        ask.grid(row=1, column=1)
        editname_entry= Entry(editwindow)
        editname_entry.grid(row=3, column=1)
        confirm= Button(editwindow, text="ok", command= lambda: ok('editini'))
        confirm.grid(row=3, column=2)

def val(Name):
    print(contacts)
    print(Name)
    sel= contacts[Name]
    print(sel)

window= LabelFrame(root, text="Select", padx= 50, pady= 50)
window.grid(row=2,column=1,columnspan=5)
contactinfo= Label(window, text="Your divices:-")
contactinfo.grid(row=1, column=0)

add= Button(root, text="Add", command= add)
add.grid(row=5, column=3)
Delete= Button(root, text="Delet", command= lambda: mode('delete'))
Delete.grid(row=5, column=4)
Edit= Button(root, text="Edit", command= lambda: mode('edit'))
Edit.grid(row=5, column=5)
strt= Button(root, text="Connect", command= start)
strt.grid(row=5, column=6)
