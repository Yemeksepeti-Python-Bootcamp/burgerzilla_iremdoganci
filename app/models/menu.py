from app import db
from datetime import datetime

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    name = db.Column(db.String(255), unique=False, nullable=False)
    product = db.relationship('Product', backref='product')

    def insert_menu():
        """default menu data"""
        menu = Menu(rest_id="1",
                    name="Dombili Menu")

        menu2 = Menu(rest_id="2",
                    name="DubleMumle Menu")
        db.session.add(menu)
        db.session.add(menu2)
        db.session.commit()
