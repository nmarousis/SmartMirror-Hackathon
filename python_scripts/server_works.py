import socket
import sys

s = socket.socket()
HOST = ''  
PORT = 80
s.bind((HOST, PORT))
s.listen(5)

conn, addr = s.accept()
while True:
	print 'Got connection from', addr	
	data= raw_input("Enter: ")
        conn.send(data) 	
conn.close()  


