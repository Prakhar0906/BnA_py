import socket 
import select 
import errno
import sys

HEADER_LENGTH = 10

IP=  "192.168.1.7"
PORT= 1234

my_username= input("Username:")
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username= my_username.encode("utf-8")
username_header= f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message= input(f"{my_username}>")
    if message:
        message= message.encode("utf-8")
        message_header= f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
    try:   
        while True:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection Closed by the server")
                sys.exit()
            username_length= 
    except:
        pass