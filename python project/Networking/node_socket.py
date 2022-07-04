import socket

HEADERSIZE= 10

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 5050))

while True:
    full_msg= ''
    new_msg= True 
    while True:
        msg= client.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen= int(msg[:HEADERSIZE])
            new_msg= False
             
        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full message recived")
            print(full_msg[HEADERSIZE:])
            new_msg= True
            full_msg= ''
        print(full_msg)

