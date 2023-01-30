from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"Hello World"}
    
api.add_resource(HelloWorld, "/helloworld")

@app.route('/')
def home():
    return "Hello World"

@app.route('/')
def user(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run(debug=True)