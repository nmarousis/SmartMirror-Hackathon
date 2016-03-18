#!/usr/bin/python           # This is server.py file

import socket


s = socket.socket()
HOST = socket.gethostname()
PORT = 80
s.bind((HOST, PORT))
s.listen(5)

data = "hello"
while True:
        conn, addr = s.accept()
        print 'Got connection from', addr
        conn.send(data)
        c.close()
print "Exiting Main Thread"

