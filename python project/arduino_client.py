import socket 

PORT = 5050
SERVER= input("Enter the ip:")
ADDR= (SERVER, PORT)
HEADER= "utf-8"
FORMAT= 64

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len= len(message)
    send_length= str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADER- len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)

while True:
    text= input(":")
    text= bytes(text)
    send(text)

