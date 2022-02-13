from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils import err_resp,internal_err_resp, message
from app.models.restaurant import Restaurant
from app.models.order import Order, Status
from app.models.menu import Menu
from app.models.product import  Product
from app import db

class RestaurantService:
    @staticmethod
    def get_restaurant_data(email:str) -> dict:
        """get restaurant data by email
        :param email: restaurant email"""
        restaurant = Restaurant.query.filter_by(email=email).first()
        if not restaurant:
            return err_resp("Restaurant Not Found","restaurant_404",404)
        restaurant_info = restaurant.id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        from .utils import load_data
        try:
            restaurant_data = load_data(restaurant)
            resp = message(True,"Restaurant Data Sent")
            resp["restaurant"] = restaurant_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp(message="Internal server error")

    @staticmethod
    def get_restaurant_orders(rest_id:int) -> dict:
        """get all orders of a specific customer
        :param rest_id: restaurant id"""
        if not(orders := Order.query.filter_by(rest_id=rest_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        current_user = get_jwt_identity()
        if rest_id != current_user:
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
    def get_restaurant_order_details(order_id:int) -> dict:
        """get a order by id
        :param order_id: order id"""
        if not (order := Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        restaurant_info = order.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        from .utils import load_data
        try:
            order_data = load_data(order)
            resp=message(True,"Order loaded successfully")
            resp["order"]=order_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

        
    @staticmethod
    def cancel_restaurant_order(order_id:int) -> dict:
        """cancel order by restaurant
        :param order_id: order id"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        restaurant_info = order.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            temp=Order.query.filter_by(id=order_id).first()
            temp.status=Status.REST_IPTAL 
            db.session.commit()
            return message(True,"Order status updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()


    @staticmethod
    def update_order_status(order_id:int,data:dict) -> dict:
        """update a order status
        :param order_id: order id"""
        if not (order:=Order.query.get(order_id)):
            return err_resp(msg="Order not found",code=400,reason="no_order")
        restaurant_info = order.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            temp = Order.query.filter_by(id=order_id).first()
            temp.status = data["status"]
            db.session.commit()
            return message(True,"Order status updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    
    @staticmethod
    def update_menu(menu_id:int,product_data:dict) -> dict:
        """insert a new product to menu
        :param menu_id: menu id
        :param product_data: product data"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(msg="Menu not found",code=400,reason="no_menu")
        restaurant_info = menu.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            from .utils import load_data
            current_user = get_jwt_identity()
            temp = Product.query.filter_by(id=product_data["product_id"]).first()
            temp.menu_id = menu_id
            temp.product_name = product_data["product_name"]
            temp.product_price = product_data["product_price"]
            temp.product_description = product_data["product_description"]
            temp.product_img = product_data["product_img"]
           
            db.session.commit()
            return message(True,"Product updated successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def get_menu_products_list(menu_id:int) -> dict:
        """get a menu products by id
        :param menu_id: menu id"""
        if not (menu := Menu.query.get(menu_id)):
            return err_resp(msg="Menu not found",code=400,reason="no_menu")
        restaurant_info = menu.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        if not (products := Product.query.filter_by(menu_id=menu_id)):
            return err_resp(msg="Products not found",code=400,reason="no_products")
        from .utils import load_data
        try:
            products_data = [load_data(product) for product in products]
            resp=message(True,"Menu loaded successfully")
            resp["products"]=products_data
            return resp,200
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def insert_product_to_menu(menu_id:int,product_data:dict) -> dict:
        """insert a new product to menu
        :param menu_id: menu id"""
        if not (menu:=Menu.query.get(menu_id)):
            return err_resp(msg="Menu not found",code=400,reason="no_menu")
        restaurant_info = menu.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            from .utils import load_data
            current_user = get_jwt_identity()
            product = Product(rest_id=product_data['rest_id'],menu_id=menu_id,
                                product_name=product_data['product_name'],product_price=product_data['product_price'],
                                product_description=product_data['product_description'],product_img=product_data['product_img'])
            db.session.add(product)
            db.session.commit()
            return message(True,"Product created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def delete_product(product_id:int) -> dict:
        """delete a product by id
        :param product_id: product id"""
        if not (product := Product.query.get(product_id)):
            return err_resp(msg="Product not found",code=400,reason="no_product")
        restaurant_info = product.rest_id
        current_user = get_jwt_identity()
        if restaurant_info != current_user:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            db.session.delete(product)
            db.session.commit()
            return message(True,"Product deleted successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()

    @staticmethod
    def create_menu(rest_id:int,data) -> dict:
        """create menu by rest id
        :param rest_id: restaurant id"""
        current_user = get_jwt_identity()
        if current_user != rest_id:
            return err_resp("Unauthorized","unauthorized",401)
        try:
            from .utils import load_data
            menu = Menu(rest_id=rest_id,name=data["name"])
            db.session.add(menu)
            db.session.commit()
            return message(True,"Menu created successfully")
        except Exception as e:
            current_app.logger.error(e)
            return internal_err_resp()
