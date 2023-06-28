from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, Range

class Game(db.Model):
    """
    Model for Game, fields are (field name, field type, requirement?):
    [name, string, required]
    [year, int, required]
    [min_age, int, required]
    [price_per_week, float, required]
    [quantity, int, required]
    [store_id, int, required]
    [owner_id, int, required]
    """
    __tablename__ = 'games'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    price_per_week = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    
    # foreign keys
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id', ondelete='Cascade'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='Cascade'), nullable=False)
    
    # field relationships
    game_designers = db.relationship('GameDesigner', backref='game', cascade='all, delete')
    game_categories = db.relationship('GameCategory', backref='game', cascade='all, delete')
    game_rent_details = db.relationship('GameRentDetail', backref='game')

class GameSchema(ma.Schema):
    game_designers = fields.List(fields.Nested('GameDesignerSchema', only=['designer']))
    game_categories = fields.List(fields.Nested('GameCategorySchema', only=['category']))
    store = fields.Nested('StoreSchema', exclude=['games', 'password'])
    game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', exclude=['game_id', 'game_name', 'store_name', 
                                                                                    'store_street_number', 'store_street_name', 
                                                                                    'store_suburb', 'store_postcode'])) 
    owner = fields.Nested('UserSchema', exclude=['games', 'game_rent_details', 'password', 'admin'])
    
    categories = fields.List(fields.String(required=True), required=True, validate=Length(min=1))
    designers = fields.List(fields.String(
        required=True, 
        validate=Regexp("^[A-Za-z]+\s[A-Za-z]+$", 
        error='Name string must be in format [first_name last_name] e.g Alan Moon')
        ), 
        required=True, validate=Length(min=1))
    
    class Meta:
        ordered = True
        fields = ('id', 'name', 'year', 'min_age', 'price_per_week', 'quantity', 
                  'game_designers', 'game_categories', 'store', 'game_rent_details', 'owner', 'owner_id', 
                  'categories', 'designers') #game_rent_details may not be needed
        
class GameUpdateSchema(ma.Schema):
    game_designers = fields.List(fields.Nested('GameDesignerSchema', only=['designer']))
    game_categories = fields.List(fields.Nested('GameCategorySchema', only=['category']))
    store = fields.Nested('StoreSchema', exclude=['games', 'password'])
    
    categories = fields.List(fields.String(required=True), required=False, validate=Length(min=1))
    designers = fields.List(fields.String(
        required=True, 
        validate=Regexp("^[A-Za-z]+\s[A-Za-z]+$", 
        error='Name string must be in format [first_name last_name] e.g Alan Moon')
        ), 
        required=False, validate=Length(min=1))

    class Meta:
        ordered = True
        fields = ('id', 'name', 'year', 'min_age', 'price_per_week', 'quantity', 
                  'game_designers', 'game_categories', 'store', 
                  'categories', 'designers')

class MinMaxSchema(ma.Schema):
    
    min_price = fields.Float(required=True)
    max_price = fields.Float(required=True)
    
    class Meta:
        fields = ('min_price', 'max_price')
        