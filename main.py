from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)


@app.route('/api/v1/hello-world-6')
def hello():
    return 'Hello World 6'


server = make_server('', 8000, app)
print('http://127.0.0.1:8000/api/v1/hello-world-6')
server.serve_forever()