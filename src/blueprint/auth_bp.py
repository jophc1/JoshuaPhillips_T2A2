from init import db, bcrypt
from flask import Blueprint, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
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
@jwt_required()
def store_register():
    # only an admin can create a store
    is_admin()
    
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

@accounts.route('/login/store', methods=['POST'])
def login_store():
    
    store_info = StoreSchema().load(request.json)
    
    store = Store.query.filter_by(email=store_info['email']).first()
    
    if not(store and bcrypt.check_password_hash(store.password, store_info['password'])):
        return {'error': 'email or password incorrect'}, 401
    
    token = create_access_token(identity=[store.id, store.email], expires_delta=timedelta(minutes=180))
    
    return {'store': StoreSchema(only=['email']).dump(store), 'token': token}

@accounts.route('/user', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user():
    jwt_identity = get_jwt_identity()
    
    user = User.query.filter_by(email=jwt_identity[1]).first()
    
    if not user:
        return {'error': 'User not found'}, 404
    
    user_info = UserSchema().load(request.json)
    
    user.first_name = user_info.get('first_name', user.first_name)
    user.last_name = user_info.get('last_name', user.last_name)
    
    db.session.commit()
    
    return UserSchema(only=['first_name','last_name']).dump(user)

# route to update store details

# route to delete user

# route to delete store

# route to view all games owned by a store (using jwt identity)

# get all users (admin only)

# get all stores (admin only)    

def is_admin():
    jwt_admin = get_jwt_identity()
    
    user = User.query.filter_by(id=jwt_admin[0]).first()    
    
    if not (user and user.admin):
           abort(401, description='must be admin')

# def is_user_or_admin(user_input_id):
    
#     jwt_user = get_jwt_identity()
    
#     user = User.query.filter_by(id=jwt_user[0]).first()
    
#     if not (user and (user.admin or user.id == user_input_id)):
#          abort(401, description='must be admin or user')
         
def is_store_or_admin(store_id):
    
    jwt_identity = get_jwt_identity()
    
    store = Store.query.filter_by(id=jwt_identity[0]).first()
    user = User.query.filter_by(id=jwt_identity[0]).first()
    
    if not ((store and store.id == store_id) or (user and user.admin)):
         abort(401, description='must be admin or store')