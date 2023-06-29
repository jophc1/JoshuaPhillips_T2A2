from flask import Flask
from init import db, ma, jwt, bcrypt
from os import environ
from marshmallow.exceptions import ValidationError

from blueprint.cli_bp import db_commands
from blueprint.auth_bp import accounts
from blueprint.games_bp import boardgames
from blueprint.rentals_bp import rentals

# list of register blueprints
registerable_blueprints = [
    db_commands,
    accounts,
    boardgames,
    rentals
]

def setup_app():
    
    app = Flask(__name__)
    # Configuration setting for database
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')  #configure app with a secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')   #database connection string
    app.json.sort_keys = False
    # Initialize instances of SQLAlchemy, Marshmallow, BCrypt and JWT
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # Register all blueprints
    for bp in registerable_blueprints:
        app.register_blueprint(bp)
    
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    @app.errorhandler(ValidationError)
    def validate_error(err):
        return {'error': str(err)}, 400
    
    
    return app