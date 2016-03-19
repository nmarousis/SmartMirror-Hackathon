from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = request.get_data()

    #Here we need to put a client socket
    s = socket.socket()
    target = ''
    port = 1325
    s.connect((target,port))
    s.send(data)
    s.close()

    return 'It works!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
