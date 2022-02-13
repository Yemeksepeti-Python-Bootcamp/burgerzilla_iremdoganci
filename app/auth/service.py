from datetime import datetime
from email import message
from flask import current_app
from flask_jwt_extended import create_access_token

from app import db
from app.utils import message,err_resp, internal_err_resp
from app.models.customer import Customer
from app.models.restaurant import Restaurant
from app.models.schemas import RestaurantSchema
from app.models.schemas import CustomerSchema

restaurant_schema = RestaurantSchema()
customer_schema = CustomerSchema()

class AuthService:
    @staticmethod
    def login(data):
        email = data.get('email')
        password = data.get('password')
        try:
            if not (customer := Customer.query.filter_by(email=email).first()):
                pass

            elif customer and customer.verify_password(password):
                customer_info = customer_schema.dump(customer)
                print('Customer:',customer_info)
                access_token = create_access_token(identity=customer.id)
                resp = message('True', 'Login successful')
                resp['access_token'] = access_token
                resp['customer'] = customer_info
                return resp, 200

            if not (restaurant := Restaurant.query.filter_by(email=email).first()):
                pass
                return err_resp('Email did not match any account',"email_404",404)

            elif restaurant and restaurant.verify_password(password):
                restaurant_info = restaurant_schema.dump(restaurant)
                print('Restaurant:',restaurant_info)
                access_token = create_access_token(identity=restaurant.id)
                resp = message('True', 'Login successful')
                resp['access_token'] = access_token
                resp['restaurant'] = restaurant_info
                return resp, 200
            return err_resp('Email or password is wrong', "email_password_404", 404)


        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
        

    @staticmethod
    def register(data):
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
        address = data.get('address')
        user_type = data.get('user_type')
    

        if Customer.query.filter_by(email=email).first():
            return err_resp('This email address is used',"email_409",409)
        elif Restaurant.query.filter_by(email=email).first():
            return err_resp('This email address is used',"email_409",409)
        try:
            if user_type == 'customer':
                customer = Customer(email=email, name=name, password=password,address=address)
                db.session.add(customer)
                db.session.commit()

                customer_info = customer_schema.dump(customer) # Convert user model to json format
                access_token = create_access_token(identity=customer.id) # Generating token
                resp = message('True', 'Registration Successful') # Composing message
                resp['access_token'] = access_token # Add tokens
                resp['user'] = customer_info # Adding user info
                return resp,200 


            elif user_type == 'restaurant':
                restaurant = Restaurant(email=email, name=name, password=password,address=address)
                db.session.add(restaurant)
                db.session.commit()
            
                restaurant_info = restaurant_schema.dump(restaurant) # Convert user model to json format
                access_token = create_access_token(identity=restaurant.id) # Generating token
                resp = message('True', 'Registration Successful') # Composing message
                resp['access_token'] = access_token # Add tokens
                resp['user'] = restaurant_info # Adding user info
                return resp,200 
                
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()