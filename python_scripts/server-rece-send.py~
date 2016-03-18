import threading
import time
import socket

class myThread (threading.Thread):
    def __init__(self, name, connection):
        threading.Thread.__init__(self)
        self.name = name
        self.connection = connection
    def run(self):
	if(self.name=='send'):
		while(1):
			message = raw_input('Enter: ')
			connection.sendall(data) 
	elif(self.name=='receive'):
		while(1):
			message = conn.recv(1024)
			print message 
	else:
		print "ERROR"

	       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''  
PORT = 50008
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "Start messanging \n"

# Create new threads
thread_send = myThread("send", conn )
thread_receive = myThread("receive", conn)

# Start new Threads
thread_send.start()
thread_receive.start()

print "Exiting Main Thread"


