from flask_restx import Namespace, fields

class RestaurantDto:

    api = Namespace("restaurant", description="Restaurant related operations")

    restaurant = api.model('Restaurant Object', {
    "email": fields.String,
    "name": fields.String,
    "address": fields.String
    })

    restaurant_resp = api.model('Auth Success Response', 
    {"status": fields.Boolean,
     "message": fields.String,
     "restaurant": fields.Nested(restaurant)
    })

    order_item = api.model('Order Item Object', {
    "order_id": fields.Integer,
    "user_id": fields.Integer,
    "rest_id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer
    })

    order = api.model('Order Object', {
    "customer_id": fields.Integer,
    "rest_id": fields.Integer,
    "products": fields.List(fields.Nested(order_item))
    })

    menu = api.model('Menu Object', {
    "rest_id": fields.Integer,
    "products": fields.List(fields.Nested(order_item))
    })