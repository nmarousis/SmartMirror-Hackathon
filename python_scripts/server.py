import socket

s = socket.socket()
HOST = ''
PORT = 80
s.bind((HOST, PORT))
s.listen(5)

data = "hello"
while True:
        conn, addr = s.accept()
        print 'Got connection from', addr
        conn.send(data)
        conn.close()
print "Exiting Main Thread"
