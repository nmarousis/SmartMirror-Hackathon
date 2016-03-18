import socket
import json

#Server address where this script binds
host = '52.169.181.92'
port = 4000

#Starting sockety
s = socket.socket()
s.bind((host, port))


#JSON Parsing
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)

print(parsed_json['first_name'])

s.listen(5)

while(1):
    c, addr = s.accept()
    msg = c.receive()
    msg = raw_input('Enter: ')
    c.send(msg)
