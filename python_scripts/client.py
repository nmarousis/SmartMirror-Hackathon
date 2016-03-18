import socket

host = '52.169.181.92'
port = 4000

s = socket.socket()
s.bind((host, port))

s.listen(5)

while(1):
    c, addr = s.accept()
    msg = c.receive()
    c.send(msg)
    
