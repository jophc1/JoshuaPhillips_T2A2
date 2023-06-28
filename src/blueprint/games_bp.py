from model_schema.game import Game, GameSchema, GameUpdateSchema, MinMaxSchema
from model_schema.user import User, UserSchema
from model_schema.store import Store, StoreSchema
from model_schema.game_category import GameCategory, GameCategorySchema
from model_schema.game_designer import GameDesigner, GameDesignerSchema
from model_schema.designer import Designer, DesignerSchema
from model_schema.category import Category, CategorySchema, VALID_CATEGORIES
from blueprint.auth_bp import is_admin, is_store
from flask import Blueprint, request, abort
from sqlalchemy import func
from marshmallow.exceptions import ValidationError
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
@boardgames.route('/minmaxprice', methods=['POST'])
def filter_games_by_rangeprice():
    
    price_range = MinMaxSchema().load(request.json)
    
    min_price = price_range['min_price']
    max_price = price_range['max_price']
    
    if min_price > max_price:
        return {'error': 'Minimum price must be lower than or equal to Maximum price range'}
    
    games = Game.query.where(db.and_(Game.price_per_week >= min_price,
                                    Game.price_per_week <= max_price)).all()
    
    return GameSchema(many=True, exclude=['owner', 'game_rent_details', 'owner_id']).dump(games)

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
            return {'error': f'[{category_name}] is an invalid category'}, 401
        categories_id.append(category.id)
    
    # Check all designers names are valid in list supplied
    designers_id = []
    for designer_name in game_info['designers']:
        
        designer = Designer.query.filter_by(full_name=designer_name.title()).first()
        if not designer:
            return {'error': f'{designer_name} is an invalid designer'}, 401

        designers_id.append(designer.id)

    
    # Check if owner has already loaned this requested game to the store
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
            
    return GameSchema(exclude=['owner_id']).dump(game), 200

# route to update game (store only)
@boardgames.route('/<int:game_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_game(game_id):
    store_id_number = is_store()
    
    game = Game.query.where(db.and_(Game.id==game_id,
                                    Game.store_id==store_id_number)).first()
    
    game_info = GameUpdateSchema().load(request.json)
    
    if not game:
        return {'error': 'Store does not contain game'}
    
    # Update game fields
    game.name = game_info.get('name', game.name)
    game.year = game_info.get('year', game.year)
    game.min_age = game_info.get('min_age', game.min_age)
    game.price_per_week = game_info.get('price_per_week', game.price_per_week)
    game.quantity = game_info.get('quantity', game.quantity)
    
    # Update categories if new categories supplied with request
    if game_info.get('categories'):
        categories_id = []
        for category_name in game_info['categories']:
            category = Category.query.filter_by(name=category_name.title()).first()
            if not category:
                return {'error': f'[{category_name}] is an invalid category'}, 401
            categories_id.append(category.id)
    
        existing_game_categories = game.game_categories
        current_category_ids = []
        for current_category in existing_game_categories:
            current_category_ids.append(current_category.category.id)
        
        for category_id in current_category_ids:
            game_category = GameCategory.query.where(db.and_(GameCategory.game_id == game.id,
                                                            GameCategory.category_id == category_id)).first()
            if game_category:
                db.session.delete(game_category)
                db.session.commit()
    
        for id_category in categories_id:
            
            new_game_category = GameCategory(
                category_id = id_category,
                game_id = game.id
            )
            db.session.add(new_game_category)
        
    # Update designers if new designers supplied with request
    if game_info.get('designers'):
        designers_id = []
        for designer_name in game_info['designers']:
            
            designer = Designer.query.filter_by(full_name=designer_name.title()).first()
            
            if not designer:
                return {'error': f'{designer_name} is an invalid designer'}, 401

            designers_id.append(designer.id)
    
        existing_game_designers = game.game_designers
        current_designer_ids = []
        for current_designer in existing_game_designers:
            current_designer_ids.append(current_designer.designer.id)
        
        for designer_id in current_designer_ids:
            game_designer = GameDesigner.query.where(db.and_(GameDesigner.game_id == game.id,
                                                            GameDesigner.designer_id == designer_id)).first()
            if game_designer:
                db.session.delete(game_designer)
                db.session.commit()
    
        for id_designer in designers_id:
            
            new_game_designer = GameDesigner(
                designer_id = id_designer,
                game_id = game.id
            )
            db.session.add(new_game_designer)
            
    db.session.commit()
    
    return GameSchema(exclude=['game_rent_details', 'owner_id']).dump(game), 201
    
# route to delete game (store or admin)
@boardgames.route('/<int:game_id>', methods=['DELETE'])
@jwt_required()
def delete_game(game_id):
    jwt_identity = get_jwt_identity()
    
    game = Game.query.filter_by(id=game_id).first()
    if not game:
        return {'error': 'No game exists by that id'}, 404
    
    user = User.query.filter_by(email=jwt_identity[1]).first()
    store = Store.query.filter_by(email=jwt_identity[1]).first()
    
    if not (user or store):
        return {'error': 'Account does not exist, must be admin or store'}, 401
    
    if (user and user.admin) or (store and (store.id == game.store_id)):
        db.session.delete(game)
        db.session.commit()
        return {}, 200
    elif store and (store.id != game.store_id):
        error = {'error': 'Cannot delete, store does not own game'}
    else:
        error = {'error': 'Must be an admin to delete game'}
        
    return error, 401

# route to add category (admin only)
@boardgames.route('/category', methods=['POST'])
@jwt_required()
def create_category():
    is_admin()
    
    category = CategorySchema().load(request.json)
    
    check_category = Category.query.filter_by(name=category['name'].title()).first()
    
    if check_category:
        return {'error': 'Category already exists'}
    
    new_category = Category(
        name = category['name'].title()
    )
    
    db.session.add(new_category)
    db.session.commit()
    
    return CategorySchema(only=['id', 'name']).dump(new_category)

# route to add designer (admin only)
@boardgames.route('/designer', methods=['POST'])
@jwt_required()
def create_designer():
    is_admin()
    
    designer = DesignerSchema().load(request.json)
    
    check_designer = Designer.query.where(db.and_(Designer.first_name==designer['first_name'].title(),
                                                  Designer.last_name==designer['last_name'].title())).first()
    
    if check_designer:
        return {'error': 'Designer already exists'}
    
    new_designer = Designer(
        first_name = designer['first_name'].title(),
        last_name = designer['last_name'].title()
    )
    
    db.session.add(new_designer)
    db.session.commit()
    
    return DesignerSchema(exclude=['game_designers']).dump(new_designer)

# route to update category (admin only)
@boardgames.route('/category/<int:category_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_category(category_id):
    is_admin()
    
    category_info = CategorySchema().load(request.json)
    
    category = Category.query.filter_by(id=category_id).first()
    
    if not category:
        return {'error': 'Cannot update, Category id does not exist'}, 404
    
    check_category_name = Category.query.filter_by(name=category_info['name'].title()).first()
    
    if check_category_name:
        return {'error': 'Cannot update, Category name already exists (cannot have duplicates)'}
    
    category.name = category_info['name'].title()
    
    db.session.commit()
    
    return CategorySchema(only=['id', 'name']).dump(category)

# route to update designer (admin only)


# route to delete category (admin only)


# route to delete designer (admin only)



def is_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    
    if not category:
        abort(401, description='category name does not exist')

def all_categories():
    stmt = db.select(Category)
    all_category = db.session.scalars(stmt).all()
    return [category.name for category in all_category]


        