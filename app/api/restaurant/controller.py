from http.client import responses
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from flask import request

from .service import RestaurantService
from .dto import RestaurantDto
from app.models.order import Order

order_item = RestaurantDto.order_item
order = RestaurantDto.order
api  = RestaurantDto.api
restaurant_resp = RestaurantDto.restaurant_resp
menu = RestaurantDto.menu

@api.route("/<string:email>")
class RestaurantGet(Resource):
    @api.doc("Get specified restaurant data",responses={
        200:("Success",restaurant_resp),
        404:"Customer Not Found",
    })
    @jwt_required()
    def get(self,email):
        """get restaurant data"""
        return RestaurantService.get_restaurant_data(email)

@api.route("/orders/<int:rest_id>")
class RestaurantOrders(Resource):
    @api.doc("Get restaurant orders",responses={
        200:("Success",order),
        404:"Order Not Found",
    })
    @jwt_required()
    def get(self,rest_id):
        """get restaurant orders"""
        return RestaurantService.get_restaurant_orders(rest_id)

@api.route("/orders_details/<int:order_id>")
class RestaurantOrdersDetails(Resource):
    @api.doc("Get restaurant order details",responses={
        200:("Success",order_item),
        404:"Order Not Found",
    })
    @jwt_required()
    def get(self,order_id):
        """get restaurant order details by order id"""
        return RestaurantService.get_restaurant_order_details(order_id)
    
    @api.doc("Set order status to cancel",responses={200:"Success"})
    @jwt_required()
    def delete(self,order_id):
        """update order status to cancel by restaurant""" 
        return RestaurantService.cancel_restaurant_order(order_id)

    
    @api.doc("Update a specific order status",responses={200:"Success"})
    @jwt_required()
    def put(self,order_id):
        """update order status by restaurant"""
        data = request.get_json()
        return RestaurantService.update_order_status(order_id,data)


@api.route("/menu/product/<int:menu_id>")
class MenuProducts(Resource):
    @api.doc("Product details",responses={200:"Success"})
    @jwt_required()
    def get(self,menu_id):
        """get product details by menu id"""
        return RestaurantService.get_menu_products_list(menu_id)

    @api.doc("Menu update",responses={200:"Success"})
    @jwt_required()
    def put(self,menu_id):
        """update menu by restaurant"""
        data = request.get_json()
        return RestaurantService.update_menu(menu_id,data)

    @api.doc("Insert product",responses={200:"Success"})
    @jwt_required()
    def post(self,menu_id):
        """insert product by restaurant"""
        data = request.get_json()
        return RestaurantService.insert_product_to_menu(menu_id,data)

@api.route("/menu/product/<int:product_id>")
class ProductDetails(Resource):
    @api.doc("Delete product",responses={200:"Success"})
    @jwt_required()
    def delete(self,product_id):
        """delete product by restaurant"""
        return RestaurantService.delete_product(product_id)

@api.route("/menu_create/<int:rest_id>")
class CreateMenu(Resource):
    @api.doc("Create Menu",responses={200:"Success"})
    @jwt_required()
    def post(self,rest_id):
        """create menu by restaurant"""
        data = request.get_json()
        return RestaurantService.create_menu(rest_id,data)


