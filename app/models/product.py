from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_name = db.Column(db.String(255), unique=False, nullable=False)
    product_price = db.Column(db.Float, unique=False, nullable=False)
    product_description = db.Column(db.String(255), unique=False, nullable=False)
    product_img = db.Column(db.String(255), unique=False, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)