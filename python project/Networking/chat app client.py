import socket 

HEADER = 64
PORT = 5056
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= '!DISCONECT'
SERVER= input("Enter server IP:")
ADDR=  (SERVER, PORT)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recv():
    connected= True
    while connected:
        print(client.recv(2048).decode(FORMAT))
        connected= False
    
recv()
