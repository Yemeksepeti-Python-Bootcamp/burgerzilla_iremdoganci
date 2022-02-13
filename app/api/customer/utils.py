def load_data(customer_db_obj):

    from app.models.schemas import CustomerSchema

    customer_schema = CustomerSchema()
    data = customer_schema.dump(customer_db_obj)
    return data
    