from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print request.get_data()
    print 'debug'
    return 'hello world'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

