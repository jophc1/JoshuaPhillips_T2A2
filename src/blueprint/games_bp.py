from model_schema.game import Game, GameSchema
from model_schema.user import User, UserSchema
from model_schema.store import Store, StoreSchema
from model_schema.game_category import GameCategory, GameCategorySchema
from model_schema.game_designer import GameDesigner, GameDesignerSchema
from model_schema.designer import Designer, DesignerSchema
from model_schema.category import Category, CategorySchema, VALID_CATEGORIES
from blueprint.auth_bp import is_admin, is_store
from flask import Blueprint, request, abort
# from sqlalchemy import and_
from flask_jwt_extended import get_jwt_identity, jwt_required
from init import db

boardgames = Blueprint('bg', __name__, url_prefix='/games')

# route to view all games
@boardgames.route('/')
def get_games():
    games = Game.query.all()
    return GameSchema(many=True, exclude=['game_rent_details','owner']).dump(games), 200

# route to view specific game by id
@boardgames.route('/<int:game_id>')
def retrieve_game(game_id):
    game = Game.query.filter_by(id=game_id).first()
    
    if not game:
        return {'error': 'game id does not exist'}, 404
    
    return GameSchema(exclude=['game_rent_details','owner']).dump(game), 200

# route to view games owned by the owner (through jwt identity for user email)
@boardgames.route('/owned')
@jwt_required()
def get_owned_games():
    jwt_identity = get_jwt_identity()
    user = User.query.filter_by(email=jwt_identity[1]).first()
    
    if not user:
        return {'error': 'User identified in jwt no longer exists'}, 401
    
    games = Game.query.filter_by(owner_id=user.id).all()
    
    return GameSchema(many=True).dump(games), 200

# route to filter games by a range of rental price

# route to filter games by a store id
@boardgames.route('/store/<int:bgstore_id>')
def filter_games_by_store(bgstore_id):
    
    store = Store.query.filter_by(id=bgstore_id).first()
    
    if not store:
        return {'error': 'no store exists'}, 404
    
    games = Game.query.filter_by(store_id=store.id).all()
    
    return GameSchema(many=True, exclude=['owner', 'game_rent_details']).dump(games), 200

# route to filter games by designer
@boardgames.route('/designer/<string:designer_first_name>/<string:designer_last_name>')
def filter_games_by_designer(designer_first_name, designer_last_name):
    designer = Designer.query.where(db.and_(Designer.first_name == designer_first_name.title(), 
                                            Designer.last_name == designer_last_name.title())).first()
    
    if not designer:
        return {'error': 'designer does not exist'}, 404
    
    return DesignerSchema().dump(designer), 200


# route to filter games by category
@boardgames.route('/category/<string:category_name>')
def filter_games_by_category(category_name):
    category = Category.query.filter_by(name=category_name.title()).first()
    
    if not category:
        return {'error': f'category name must be {all_categories()}'}, 400
    
    return CategorySchema().dump(category), 200

# route to filter games by minimum age
@boardgames.route('/minage/<int:minimum_age>')
def filter_games_by_minage(minimum_age):
    games = Game.query.where(Game.min_age<=minimum_age).all()
    
    if not games:
        return {'error': f'no game with a minimum age less than {minimum_age}'}, 404

    return GameSchema(many=True, exclude=['game_rent_details', 'owner']).dump(games), 200
    
# route to add new game (store only)
@boardgames.route('/', methods=['POST'])
@jwt_required()
def add_game():
    store_id_number = is_store()
    
    game_info = GameSchema().load(request.json)
    
    # Check all categories are valid in list supplied
    categories_id = []
    for category_name in game_info['categories']:
        category = Category.query.filter_by(name=category_name.title()).first()
        if not category:
            if len(category_name) == 1:
                return {'error': 'categories must be in a list e.g. ["Deck Builder", "Euro"]'}, 400
            return {'error': f'[{category_name}] is an invalid category'}, 401
        categories_id.append(category.id)
    
    # Check all designers names are valid in list supplied
    designers_id = []
    for designer_name in game_info['designers']:
        designer_name_list = designer_name.split()
        if len(designer_name_list) != 2:
            return {'error': f'[{designer_name}] is wrong word count, must be in format "first_name last_name" and in a list e.g. ["Alan Moon"]'}, 400
        
        designer_first_name = designer_name_list[0]
        designer_last_name = designer_name_list[1] 
        designer = Designer.query.where(db.and_(Designer.first_name == designer_first_name.title(),
                                                Designer.last_name == designer_last_name.title())).first()
        if not designer:
            return {'error': f'{designer_name} is an invalid designer'}, 401

        designers_id.append(designer.id)
    
    test_game = Game.query.where(db.and_(Game.owner_id == game_info['owner_id'], 
                                         Game.name == game_info['name'].title(),
                                         Game.store_id == store_id_number)).first()
    if test_game:
        return {'error': 'game already loaned to store by same owner'}, 400
    
    owner = User.query.filter_by(id=game_info['owner_id']).first()
    
    if not owner:
        return {'error': 'owner id does not exist'}, 404
    
    game = Game(
        name = game_info['name'],
        year = game_info['year'],
        min_age = game_info['min_age'],
        price_per_week = game_info['price_per_week'],
        quantity = game_info['quantity'],
        store_id = store_id_number,
        owner_id = owner.id
    )
    
    db.session.add(game)
    db.session.commit()
    
    # check that inputted categories are valid
    
    
    for id_category in categories_id:
        
        # check if category already associated with game
        test_game_category = GameCategory.query.where(db.and_(GameCategory.category_id == id_category,
                                                              GameCategory.game_id == game.id)).first()
        if not test_game_category:
            new_game_category = GameCategory(
                category_id = id_category,
                game_id = game.id
            )
            db.session.add(new_game_category)
     
    for id_designer in designers_id:
        
        # check if designer already associated with game
        test_game_designer = GameDesigner.query.where(db.and_(GameDesigner.designer_id == id_designer,
                                                              GameDesigner.game_id == game.id)).first()
        if not test_game_designer:
            new_game_designer = GameDesigner(
                designer_id = id_designer,
                game_id = game.id
            )
            db.session.add(new_game_designer)
            
    db.session.commit()    
            
    
    # check that inputted designers are valid
    return GameSchema(exclude=['owner_id']).dump(game), 200

# route to update game (store only)

# route to delete game (store or admin)



def is_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    
    if not category:
        abort(401, description='category name does not exist')

def all_categories():
    stmt = db.select(Category)
    all_category = db.session.scalars(stmt).all()
    return [category.name for category in all_category]