import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app.models.order import Order
from app.models.product import Product
from app.models.restaurant import Restaurant
from app.models.menu import Menu
from app.models.customer import Customer


import click
from flask_migrate import Migrate

# configte dev database ve prod database ve test database ayrı. flask congiften aldıüı dbyi değiştireceği için migrate burada
from app import create_app, db
app = create_app(os.getenv('FLASK_CONFIG') or 'default') #env nin içinden configle ilgili olanı al ya da default olarak kullan
migrate = Migrate(app, db)



@app.cli.command()
def defaultdata():
    """default data"""
    Customer.insert_customer()
    Restaurant.insert_restaurant()
    Menu.insert_menu()
    Product.insert_product()
    return 1

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit test """
    import unittest

    if test_names:
        """
        flask test tests.test_dataset_model
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests',pattern='test*.py')

    result =  unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
