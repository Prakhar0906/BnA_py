import socket
import time 
import pickle 


HEADERSIZE = 10

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("[STARTING] server has started...")
print("[LISTENING] waiting for connection....")

while True:
    clientsocket, address= s.accept()
    print(f"Connection from {address} has been establishen!")
    d= {1: "Hey", 2: "There"}
    msg= pickle.dump(d)
    
    msg= bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8")+msg
    clientsocket.send(msg)

