from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Flask!'


@app.route('/flask')
def renderHelloTemplate():
    return make_response(open('templates/index.html').read())

if __name__ == '__main__':
    app.run()
