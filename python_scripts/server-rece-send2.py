import threading
import time
import socket


s = socket.socket()
HOST = '127.0.0.1'  
PORT = 12345
s.bind((HOST, PORT))
s.listen(5)

data = "hello"
while True:
	conn, addr = s.accept()
	print 'Got connection from', addr	
	connection.send(data) 	
	c.close()  
print "Exiting Main Thread"


