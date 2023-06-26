from init import db, bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required
from model_schema.user import User, UserSchema
from model_schema.store import Store, StoreSchema
from datetime import timedelta

accounts = Blueprint('account', __name__)

@accounts.route('/register/user', methods=['POST'])
def user_register():
    user_info = UserSchema().load(request.json)
    email_user_test = User.query.filter_by(email=user_info['email']).first()
    email_store_test = Store.query.filter_by(email=user_info['email']).first()
    
    if email_store_test or email_user_test:
        return {'error': 'Email already exists'}, 409
    
    user = User(
        first_name = user_info['first_name'],
        last_name = user_info['last_name'],
        email = user_info['email'],
        password = bcrypt.generate_password_hash(user_info['password']).decode('UTF-8')
    )
    
    db.session.add(user)
    db.session.commit()
    
    token = create_access_token(identity=[user.id, user.email], expires_delta=timedelta(minutes=180))
    
    return {'user': UserSchema(only=['email', 'first_name', 'last_name']).dump(user), 'token': token}


@accounts.route('/register/store', methods=['POST'])
# @jwt_required()
def store_register():
    # only an admin can create a store
    # is_admin()
    
    store_info = StoreSchema().load(request.json)
    email_user_test = User.query.filter_by(email=store_info['email']).first()
    email_store_test = Store.query.filter_by(email=store_info['email']).first()
    
    if email_store_test or email_user_test:
        return {'error': 'Email already exists'}, 409
    
    store = Store(
        name = store_info['name'],
        street_number = store_info['street_number'],
        street_name = store_info['street_name'],
        suburb = store_info['suburb'],
        postcode = store_info['postcode'],
        email = store_info['email'],
        password = bcrypt.generate_password_hash(store_info['password']).decode('UTF-8')
    )
    
    db.session.add(store)
    db.session.commit()
    
    token = create_access_token(identity=[store.id, store.email], expires_delta=timedelta(minutes=180))
    
    return {'store': StoreSchema(only=['name', 'email']).dump(store), 'token': token}

@accounts.route('/login/user', methods=['POST'])
def login_user():
    
    user_info = UserSchema().load(request.json)
    
    user = User.query.filter_by(email=user_info['email']).first()
    
    if not(user and bcrypt.check_password_hash(user.password, user_info['password'])):
        return {'error': 'email or password incorrect'}, 401
    
    token = create_access_token(identity=[user.id, user.email], expires_delta=timedelta(minutes=180))
    
    return {'user': UserSchema(only=['email']).dump(user), 'token': token}

# login store next
        
