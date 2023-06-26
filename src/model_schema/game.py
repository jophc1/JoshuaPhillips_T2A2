from init import db, ma
from marshmallow import fields

class Game(db.Model):
    """
    Model for Game, fields are (field name, field type, requirement?):
    [name, string, required]
    [year, int, optional]
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
    year = db.Column(db.Integer)
    min_age = db.Column(db.Integer, nullable=False)
    price_per_week = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
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
    store = fields.Nested('StoreSchema', exclude=['games'])
    game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', only=['id'])) #might not need this schema field
    owner = fields.Nested('UserSchema', exclude=['games', 'game_rent_details'])
    
    class Meta:
        ordered = True
        fields = ('id', 'name', 'year', 'min_age', 'price_per_week', 'quantity', 
                  'game_designers', 'game_categories', 'store', 'game_rent_details', 'owner') #game_rent_details may not be needed
        