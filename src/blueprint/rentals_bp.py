from model_schema.game import Game, GameSchema
from model_schema.user import User
from model_schema.game_rent_detail import GameRentDetail, GameRentDetailSchema, CreateRentalSchema
from blueprint.auth_bp import is_admin, is_store
from flask import Blueprint, request
from sqlalchemy import desc
from datetime import date
from flask_jwt_extended import jwt_required
from init import db

rentals = Blueprint('rental', __name__, url_prefix='/rentals')

# route to view all game rentals (admin only)
@rentals.route('/')
@jwt_required()
def get_rentals():
    is_admin()
    
    game_rentals = GameRentDetail.query.order_by(desc('date')).all()
    
    return GameRentDetailSchema(many=True).dump(game_rentals), 200

# route to view all game rentals by a store (store only)
@rentals.route('/store')
@jwt_required()
def get_store_rentals():
    game_store_id = is_store()
    
    games = Game.query.filter_by(store_id = game_store_id).all()
    
    return GameSchema(many=True, only=['id', 'name', 'game_rent_details']).dump(games), 200

# route to add game rental (store only)
@rentals.route('/new', methods=['POST'])
@jwt_required()
def new_rental():
    game_store_id = is_store()
    
    rental_detail = CreateRentalSchema().load(request.json)
    
    game = Game.query.where(db.and_(Game.store_id == game_store_id, 
                                    Game.id == rental_detail['game_id'])).first()
    
    if not game:
        return {'error': 'Store does not own game (cannot use game_id)'}, 400
    
    rentee = User.query.filter_by(id = rental_detail['rentee_id']).first()
    
    if not rentee:
        return {'error': 'Rentee does not exist (cannot use rentee_id)'}, 400
    
    if game.owner_id == rentee.id:
        return {'error': 'Rentee cannot rent out a game they own'}, 400
    
    order_quantity = rental_detail['quantity']
    store_quantity = game.quantity
    
    if store_quantity < order_quantity:
        return {'error': f'Not enough quantity of game, only have {store_quantity} copies and order requires {order_quantity} copies'}, 400
    
    new_rental = GameRentDetail(
        date = date.today(),
        rentee_id = rentee.id,
        rentee_first_name = rentee.first_name,
        rentee_last_name = rentee.last_name,
        rentee_email = rentee.email,
        game_id = game.id,
        game_name = game.name,
        price_per_week = game.price_per_week,
        quantity = order_quantity,
        store_name = game.store.name,
        store_street_number = game.store.street_number,
        store_street_name = game.store.street_name,
        store_suburb = game.store.suburb,
        store_postcode = game.store.postcode
    )
    
    game.quantity = store_quantity - order_quantity
    
    db.session.add(new_rental)
    db.session.commit()
    
    return GameRentDetailSchema().dump(new_rental), 201

# route to delete a game rental (admin only)
@rentals.route('/<int:rental_id>', methods=['DELETE'])
@jwt_required()
def delete_rental(rental_id):
    is_admin()
    
    game_rental = GameRentDetail.query.filter_by(id = rental_id).first()
    
    if not game_rental:
        return {'error': 'Game rental does not exist (no game rental with rental_id)'}, 404
    
    db.session.delete(game_rental)
    db.session.commit()
    
    return {}, 200