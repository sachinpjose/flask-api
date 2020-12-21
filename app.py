from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {"sachin": {"age": 25, "gender": "male"}, "test": {"age": 45, "gender": "male"}}

class HelloWorld(Resource):

    def get(self, product, price):
        # return names[name]
        return {"message": "Product added successfully" , "data": "The price of the product {} is  {}".format(product, price)}

api.add_resource(HelloWorld, "/hi/<string:product>/<int:price>")

if __name__ == '__main__':
    app.run(debug=True)