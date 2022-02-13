from pkg_resources import ResolutionError
from app import db
from datetime import datetime
from app import db, bcrypt


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    password_hash = db.Column(db.String(255), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    order = db.relationship('Order', backref='order')
    menu = db.relationship('Menu', backref='menu')


    def __init__(self, **kwargs):
        super(Restaurant, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Restaurant {self.name}>"


    def insert_restaurant():
        """default restaurant data"""
        restaurant = Restaurant(email="omerk@restoran.nett",
                            name="Dumbili Burger",
                            password="12345678",
                            address="Ata Mahallesi No:1 Ümraniye/İstanbul")

        restaurant2 = Restaurant(email="tuncd@restoran.nett",
                            name="Dublemumble",
                            password="12345678",
                            address="Cennet Mahallesi No:1 Ankara")
        db.session.add(restaurant)
        db.session.add(restaurant2)
        db.session.commit()
