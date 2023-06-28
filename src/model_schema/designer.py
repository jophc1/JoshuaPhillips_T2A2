from init import db, ma
from marshmallow import fields
from sqlalchemy.ext import hybrid
from marshmallow.validate import Regexp, And, Length

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
    game_designers = db.relationship('GameDesigner', backref='designer', cascade='all, delete')
    
    @hybrid.hybrid_property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

class DesignerSchema(ma.Schema):
    game_designers = fields.List(fields.Nested('GameDesignerSchema', exclude=['designer']))
    first_name = fields.String(required=True, validate=And(Regexp('^[A-Za-z-]+$', error='first name must only contain letters and hyphen, no spaces e.g Sally-May'), 
                                                           Length(min=1, max=20)))
    last_name = fields.String(required=True, validate=And(Regexp('^[A-Za-z-]+$', error='last name must only contain letters and hyphen, no spaces e.g Reed-Smith'), 
                                                           Length(min=1, max=20)))

    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name', 'game_designers')