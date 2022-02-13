from telnetlib import STATUS
from app import db
from datetime import datetime

class Status:
    YENI = 1
    HAZIRLANIYOR = 2
    YOLDA = 3
    TESLIM = 4
    MUSTERI_IPTAL = 5
    REST_IPTAL = 6

class Order(db.Model):
    _tablename_ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    product_id = db.Column(db.String(255))
    status = db.Column(db.Integer, default=Status.YENI)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def create(self, customer_id, rest_id):
        self.customer_id = customer_id
        self.rest_id = rest_id
        self.status = True
        return self


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer, default=1)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
