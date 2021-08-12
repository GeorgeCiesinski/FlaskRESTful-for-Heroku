from app import app
from db import db

db.init_app(app)


# Creates the data.db file before the first request is ran.
@app.before_first_request
def create_tables():
	db.create_all()  # Relies on the model being imported for it to see the model/table