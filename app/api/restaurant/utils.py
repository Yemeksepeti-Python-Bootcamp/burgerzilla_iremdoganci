def load_data(restaurant_db_obj):

    from app.models.schemas import RestaurantSchema

    restaurant_schema = RestaurantSchema()
    data = restaurant_schema.dump(restaurant_db_obj)
    return data
    