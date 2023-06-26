from flask import Flask
from init import db, ma, jwt, bcrypt
from os import environ

from blueprint.cli_bp import db_commands
from blueprint.auth_bp import accounts

from flask.json.provider import JSONProvider
import orjson

# required classes to implement Schema ordering, more info here (https://github.com/pallets/flask/pull/4692)
class OrJSONProvider(JSONProvider):
    def dumps(self, obj, *, option=None, **kwargs):
        if option is None:
            option = orjson.OPT_APPEND_NEWLINE | orjson.OPT_NAIVE_UTC
        
        return orjson.dumps(obj, option=option).decode()

    def loads(self, s, **kwargs):
        return orjson.loads(s)

class MyFlask(Flask):
    json_provider_class = OrJSONProvider

# list of register blueprints
registerable_blueprints = [
    db_commands,
    accounts
]

def setup_app():
    
    app = MyFlask(__name__)
    
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')  #configure app with a secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')   #database connection string
    
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    for bp in registerable_blueprints:
        app.register_blueprint(bp)
    
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    
    
    return app