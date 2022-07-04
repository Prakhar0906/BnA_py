import socket

HEADER = 64
PORT = 5050
FORMAT= 'utf-8'
DISCONNECT_MESSAGE= '!DISCONECT'
SERVER= input("Enter server Ip:")
ADDR=  (SERVER, PORT)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message= msg.encode(FORMAT)
    msg_length= len(message)
    send_length= str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER- len(send_length))
    client.send(send_length)
    client.send(message)
    while True:
        print(client.recv(2048).decode(FORMAT))
    

while True:
    send(input("message:"))