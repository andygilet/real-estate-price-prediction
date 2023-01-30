from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/')
def user(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run(port=5000)