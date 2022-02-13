from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.product import Product
from app.utils import err_resp,internal_err_resp, message
from app.models.customer import Customer
from app.models.restaurant import Restaurant
from app.models.order import Order, Status
from app import db


class CustomerService:
    @staticmethod
    def get_customer_data(email: str) -> dict:
        """
        Get customer data
        :param email: customer email"""
        customer = Customer.query.filter_by(email=email).first()
        if not customer:
            return err_resp("Customer Not Found","customer_404",404)
        current_user = get_jwt_identity()
        if customer.id != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        from .utils import load_data
        try:
            customer_data = load_data(customer)
            resp = message(True,"Customer data sent")
            resp["customer"] = customer_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp(message="Internal server error")

    @staticmethod
    def create_order(customer_id:int,data:dict) -> dict:
        """
        Create a new order
        :param customer_id: customer id
        :param data: order data"""
        current_user = get_jwt_identity()
        if customer_id != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            from .utils import load_data
            if not (product_id := Product.query.filter_by(id=data["product_id"]).first()):
                return err_resp("Product Not Found","product_404",404)
            if not (rest_id := Restaurant.query.filter_by(id=data["rest_id"]).first()):
                return err_resp("Restaurant Not Found","restaurant_404",404)
            order = Order(customer_id=customer_id,rest_id=data['rest_id'],product_id=data['product_id'])

            db.session.add(order)
            db.session.commit()
            return message(True,"Order created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_order_details(order_id:int) -> dict:
        """
        get a order by id
        :param order_id: order id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        customer_info = order.customer_id
        current_user = get_jwt_identity()
        if customer_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        temp = order.product_id
        if not (products := Product.query.filter_by(id=temp).first()):
            return err_resp(msg="Products not found",code=400,reason="no_products")
        from .utils import load_data
        try:
            products_data = load_data(products)
            resp=message(True,"Order loaded successfully")
            resp["order"]=products_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def update_order(order_id:int,order_data:dict) -> dict:
        """
        update a order
        :param order_id: order id
        :param order_data: order data"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        customer_info = order.customer_id
        current_user = get_jwt_identity()
        if customer_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            Order.query.filter_by(id=order_id)
            temp = temp.orde
            db.session.commit()
            return message(True,"Order updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_orders(customer_id:int) -> dict:
        """
        Get all orders of a specific customer
        :param customer_id: customer id"""
        if not(orders := Order.query.filter_by(customer_id=customer_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        current_user = get_jwt_identity()
        if customer_id != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        from .utils import load_data
        try:
            orders_data = [load_data(order) for order in orders]
            resp=message(True,"Orders loaded successfully")
            resp["orders"]=orders_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    
        
    @staticmethod
    def cancel_order(order_id:int) -> dict:
        """
        update a order status to cancelled by customer
        :param order_id: order id"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        customer_info = order.customer_id
        current_user = get_jwt_identity()
        if customer_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            temp=Order.query.filter_by(id=order_id).first()
            temp.status=Status.MUSTERI_IPTAL
            db.session.commit()
            return message(True,"Order status updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def add_product_to_order(order_id:int,product_data:dict) -> dict:
        """
        Insert a new product to menu
        :param order_id: order id
        :param product_data: product data"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        customer_info = order.customer_id
        current_user = get_jwt_identity()
        if customer_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            from .utils import load_data
            current_user = get_jwt_identity()
            temp = Order.query.filter_by(id=order_id).first()
            temp.product_id=(product_data['product_id'])

            db.session.commit()
            return message(True,"Product created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
