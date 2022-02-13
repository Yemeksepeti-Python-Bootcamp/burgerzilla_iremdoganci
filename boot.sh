source venv/bin/activate
flask db init
flask db migrate
flask db upgrade
flask defaultdata
flask run --host=0.0.0.0
