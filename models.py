# models.py
# pylint: disable=missing-docstring

from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.Text())

    def __repr__(self):
        return '<id {}>'.format(self.id)
