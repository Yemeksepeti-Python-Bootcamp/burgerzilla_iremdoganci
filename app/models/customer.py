from pkg_resources import ResolutionError
from app import db
from datetime import datetime
from app import bcrypt

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), unique=False, nullable=False)
    password_hash = db.Column(db.String(255))
    address = db.Column(db.String(255), unique=False, nullable=False)
    order = db.relationship('Order', backref='order2')

    def __init__(self, **kwargs):
        super(Customer, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Customer {self.name}>"