# Flask Restful App

This is a Flask Restful API which allows new users to register, authorize which provides a JWT token, and interact 
with Store and Item tables. Available commands are GET, POST, PUT, and DELETE. 

This API has been deployed on Heroku.

# Implementation

1. Clone repository
2. Create a virtual environment, and use pip to install the requirements
```
pip install -r requirements.txt
```
3. cd into app folder, and run app.py
```
cd app
python app.py
```
4. Use Postman to interact with API. 

# Interacting with API

The API URL changes depending on whether it is being run locally, or is deployed on Heroku. For the below

# Technology

- Flask
- FlaskRESTful
- Flask-JWT
- Flask-SQLAlchemy
- SQLite3 (development)
- PostgreSQL (production)
- Deployed on Heroku
