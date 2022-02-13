from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask import request


from .service import CustomerService
from .dto import CustomerDto

order_item = CustomerDto.order_item
order = CustomerDto.order
api  = CustomerDto.api
customer_resp = CustomerDto.customer_resp


@api.route("/<string:email>")
class CustomerGet(Resource):
    @api.doc("Get specified customer data",responses={
        200:("Success",customer_resp),
        404:"Customer Not Found",
    })
    @jwt_required()  
    def get(self,email):
        """get customer data"""
        return CustomerService.get_customer_data(email)

@api.route("/orders/<int:order_id>")
class CustomerOrderDetails(Resource):
    @api.doc("List order details",responses={200:"Success"})
    @jwt_required()
    def get(self,order_id):
        """list order details"""
        return CustomerService.get_order_details(order_id)

    @api.doc("Update a specific order",responses={200:"Success"})
    @api.expect(order)
    @jwt_required()
    def put(self,order_id):
        """ update a specific order"""
        data = request.get_json()
        return CustomerService.update_order(order_id,data)
    
    @api.doc("Cancel order",responses={200:"Success"})
    @jwt_required()
    def delete(self,order_id):
        """cancel order"""
        return CustomerService.cancel_order(order_id)

    @api.doc("Add product to order",responses={200:"Success"})
    @jwt_required()
    def post(self,order_id):
        """ add product to order"""
        data = request.get_json()
        return CustomerService.add_product_to_order(order_id,data)

@api.route("/orders2/<int:customer_id>")
class OrderList(Resource):
    @api.doc("Get all order of a specific customer",responses={200:"Success",500:"Internal Server Error"})
    @jwt_required()
    def get(self,customer_id):
        """
        Get all order of a specific user"""
        return CustomerService.get_orders(customer_id)

    @api.doc("Create a new order",responses={200:"Success",500:"Internal Server Error"})
    @api.expect(order)
    @jwt_required()
    def post(self,customer_id):
        """
        Create a new order"""
        data = request.get_json()
        return CustomerService.create_order(customer_id,data)