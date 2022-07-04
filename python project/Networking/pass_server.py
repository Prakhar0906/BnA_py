import socket 
import threading

HEADER= 64
PORT= 5050
IP= socket.gethostbyname(socket.gethostname())
ADDR= (IP, PORT)
FORMAT= "utf-8"
PASSWORD= '3024'

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def pas():
    print(f"New client {addr} and {client}")
    connected= True
    client.send("Please enter the password".encode(FORMAT))
    while connected:
        msg_length= client.recv(HEADER).decode(FORMAT)
        if msg_length:
         msg_length= int(msg_length)
         msg= client.recv(msg_length).decode(FORMAT)
        if msg == PASSWORD:
            client.send("Welcom".encode(FORMAT))
            thread= threading.Thread(target=handle_client)
            thread.start()
            connected= False
        else:
            client.send("Incorrect password".encode(FORMAT))

def handle_client():
    client.send("you have control".encode(FORMAT))


print("[STARTING] server is starting ...")
print(f"[LISTENING] server is listening on {IP}")
while True:
    server.listen()
    client, addr= server.accept()
    pas()

