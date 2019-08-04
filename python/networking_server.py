import socket

host='127.0.0.1' #local address of own computer
port=5000

s=socket.socket() #socket name with variable s
s.bind((host,port)) 

s.listen(1) #set for socket and listen only one connection at a time
c,addr=s.accept() #if successful listen then store the information in addr
print("connectio from: "+str(addr))

while True:
    data=c.recv(1024)
    if not data:
        break
    print("from connected user: "+str(data))
    data=str(data).upper()
    print("sending: "+str(data))
    c.send(data.encode())
    print("sent")

c.close()
