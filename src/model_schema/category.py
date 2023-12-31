from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

VALID_CATEGORIES = ('deck building', 'worker placement', 'abstract', 'euro', 'wargame')

class Category(db.Model):
    """
    Model for Category, fields are (field name, field type, requirement?):
    [name, string, required]
    """
    __tablename__ = 'categories'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False, unique=True)
    # foreign keys
   
    # field relationships
    game_categories = db.relationship('GameCategory', backref='category', cascade='all, delete')
    

class CategorySchema(ma.Schema):
    game_categories = fields.List(fields.Nested('GameCategorySchema', exclude=['category']))
    name = fields.String(required=True, validate=And(Regexp('^[A-Za-z ]+$', error='category name must be only letters and spaces'), 
                                                     Length(min=1, max=20)))

    class Meta:
        ordered = True
        fields = ('id', 'name', 'game_categories')