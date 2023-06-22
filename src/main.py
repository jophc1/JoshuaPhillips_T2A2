from flask import Flask
from init import db, ma, jwt, bcrypt
from os import environ

def setup_app():
    
    app = Flask(__name__)
    
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')  #configure app with a secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')   #database connection string
    
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    return app