from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


dummy_products = []

class HelloWorld(Resource):

    def get(self):
        return {"product": dummy_products}

    def post(self, product):
        dummy_products.append(product)
        return {"message": "Created new product.", "product": product}
    


api.add_resource(HelloWorld, "/product")

if __name__ == '__main__':
    app.run(debug=True)