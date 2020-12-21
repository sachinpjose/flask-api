from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {"sachin": {"age": 25, "gender": "male"}, "test": {"age": 45, "gender": "male"}}

class HelloWorld(Resource):

    def get(self, name):
        return names[name]
        # return {"data": "The price of the product {} is  {}".format(name, price)}

api.add_resource(HelloWorld, "/hi/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)