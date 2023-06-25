from init import db, ma
from marshmallow import fields

class Designer(db.Model):
    """
    Model for Designer, fields are (field name, field type, requirement?):
    [first_name, string, required]
    [last_name, string, required]
    """
    __tablename__ = 'designers'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    # foreign keys
   
    # field relationships
    game_designers = db.relationship('GameDesigner', backref='designer')

class DesignerSchema(ma.Schema):
    game_designers = fields.List(fields.Nested('GameDesignerSchema', exclude=['designer']))

    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name', 'game_designers')