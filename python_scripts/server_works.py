import socket
import sys

s = socket.socket()
s2 = socket.socket()

HOST = ''
PORT = 1425
PORT2 = 1325

s.bind((HOST, PORT))
s2.bind((HOST, PORT2))

s.listen(5)
s2.listen(5)

conn, addr = s.accept()
while True:
	print 'Got connection from', addr
	conn2, addr = s2.accept()
	print 'Got new data'
	data = conn2.recv()
	conn2.close()
    	conn.send(data)
conn.close()
