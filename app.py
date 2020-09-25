import socket
from flask import Flask

app = Flask(__name__)

hostname = socket.gethostname()

@app.route('/')
def hello():
    return "Container hostname: {}".format(hostname)

if __name__ == '__main__':
    app.run()
