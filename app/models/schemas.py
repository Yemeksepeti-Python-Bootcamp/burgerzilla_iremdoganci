from app import ma

class CustomerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','email', 'name', 'password_hash','address','order')

class RestaurantSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','email', 'name','password_hash', 'address','order','menu')

class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','rest_id', 'name','product')

class ProductsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','rest_id','menu_id','product_name','product_price','product_description','product_img','date_added')	
 
class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','customer_id','rest_id','products','status','date_added','date_updated')

class OrderItemSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id','order_id','customer_id','rest_id','product_id','quantity','date_added','date_updated')
