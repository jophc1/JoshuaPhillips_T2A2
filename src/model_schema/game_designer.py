from init import db, ma
from marshmallow import fields

class GameDesigner(db.Model):
    """
    Model for GameDesigner, fields are (field name, field type, requirement?):
    [designer_id, int, required]
    [game_id, int, required]
    """
    __tablename__ = 'game_designers'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    
    # foreign keys
    designer_id = db.Column(db.Integer, db.ForeignKey('designers.id', ondelete='Cascade'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)
    # field relationships
    

class GameDesignerSchema(ma.Schema):
    designer = fields.Nested('DesignerSchema', exclude=['game_designers'])
    game = fields.Nested('GameSchema', exclude=['game_designers'])
    
    class Meta:
        ordered = True
        fields = ('id', 'designer','game')