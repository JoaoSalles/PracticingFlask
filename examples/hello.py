from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_work():
    return "Hello World!"


if __name__ == '__main__':
    host = os.getenv('IP','127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.run(host = host, port = port)