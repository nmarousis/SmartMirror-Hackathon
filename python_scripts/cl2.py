#!/usr/bin/python           # This is server.py file

import socket

s = socket.socket()
target = '52.169.181.92'
port = 80
s.connect((target,port))

while True:
	data = s.recv(1024)
	print 'Received', repr(data)
s.close()
