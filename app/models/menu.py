from app import db
from datetime import datetime

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    name = db.Column(db.String(255), unique=False, nullable=False)
    product = db.relationship('Product', backref='product')
