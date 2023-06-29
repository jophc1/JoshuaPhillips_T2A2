from init import db, ma
from marshmallow import fields

class GameCategory(db.Model):
    """
    Model for GameCategory, fields are (field name, field type, requirement?):
    [category_id, int, required]
    [game_id, int, required]
    """
    __tablename__ = 'game_categories'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    
    # foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='Cascade'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)
    # field relationships
    

class GameCategorySchema(ma.Schema):
    category = fields.Nested('CategorySchema', exclude=['game_categories'])
    game = fields.Nested('GameSchema', exclude=['game_categories', 'game_rent_details', 'owner', 'owner_id'])
    
    class Meta:
        ordered = True
        fields = ('id', 'category', 'game')