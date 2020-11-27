# pylint: disable=missing-docstring

BASE_URL = '/api/v1'

from flask import Flask, request
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  # NEW LINE (Order is important here!)
db = SQLAlchemy(app)
ma = Marshmallow(app)  # NEW LINE

from models import Product

from schemas import many_product_schema, one_product_schema

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    from tasks import very_slow_add
    very_slow_add.delay(1, 2) # This pushes a task to Celery and does not block.

    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/<int:id>', methods=['GET'])
def get_one_product(id):
    products = db.session.query(Product).get(id) # SQLAlchemy request => 'SELECT * FROM products'
    return one_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products', methods=['POST'])
def add_one_product():
    name = request.get_json().get('name')
    products = Product(id=3, name=name, description=name)
    print(products)
    products = db.session.add(products) # SQLAlchemy request => 'SELECT * FROM products'
    db.session.commit()
    return one_product_schema.jsonify(products), 200
