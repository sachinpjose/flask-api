from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import uuid

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('price', help= "Price of the product is required", required=True)
parser.add_argument('title',help= "Name of the product is required", required=True)


dummy_products = {}

class Products(Resource):

    def get(self):
        return dummy_products

    def post(self):
        pdt_id = uuid.uuid1()
        product = parser.parse_args()
        dummy_products[str(pdt_id)] = {'title': product['title'], 'price': product['price']}
        print(dummy_products)
        return dummy_products[str(pdt_id)], 201


api.add_resource(Products, "/products")

if __name__ == '__main__':
    app.run(debug=True)