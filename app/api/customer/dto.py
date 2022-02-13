from flask_restx import Namespace, fields

class CustomerDto:

    api = Namespace("customer", description="Customer related operations")

    customer = api.model('Customer Object', {
    "email": fields.String,
    "name": fields.String,
    "address": fields.String

    })

    customer_resp = api.model('Auth Success Response', 
    {"status": fields.Boolean,
     "message": fields.String,
     "customer": fields.Nested(customer)
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