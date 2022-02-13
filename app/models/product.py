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

def insert_product():
    """default product data"""
    product = Product(menu_id="1",
                      rest_id="1",
                      product_name="bombili",
                      product_price="30",
                      product_description="Meshur dombili burger,ozel soslu, sarımsaklı ve soganli",
                      product_img="https://picjumbo.com/yummy-pulled-pork-burger/"

                      )

    product2 = Product(menu_id="1",
                       rest_id="1",
                       product_name="duble peynirli",
                       product_price="50",
                       product_description="Cift katli mozerella ve chedarla bezenmis dombili burger",
                       product_img="https://picjumbo.com/french-fries-and-fresh-bacon-burger/")

    product3 = Product(menu_id="1",
                       rest_id="1",
                       product_name="ac doyuran",
                       product_price="75",
                       product_description="Ozel ketcap ve tatli mayonezli burger ve patates",
                       product_img="https://picjumbo.com/black-bacon-burger/")

    product4 = Product(menu_id="2",
                       rest_id="2",
                       product_name="tekkatli",
                       product_price="25",
                       product_description="Bol domatesli, özel muble soslu ve soganli",
                       product_img="https://picjumbo.com/yummy-pulled-pork-burger/")

    product5 = Product(menu_id="2",
                       rest_id="2",
                       product_name="dublemuble",
                       product_price="45",
                       product_description="Çift katlı, beyaz peynir + kaşar peynir soslu, duble hamburger",
                       product_img="https://picjumbo.com/black-bacon-burger/")

    product6 = Product(menu_id="2",
                       rest_id="2",
                       product_name="delüks",
                       product_price="70",
                       product_description="Özel dublemuble burger, patates ve eritme peynirle birlikte",
                       product_img="https://picjumbo.com/black-bacon-burger/")

    db.session.add(product)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.commit()
