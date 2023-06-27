from init import db, ma
from marshmallow import fields

class Store(db.Model):
    """
    Model for Store, fields are (field name, field type, requirement?):
    [name, string, required]
    [street_number, int, required]
    [street_name, string, required]
    [suburb, string, required]
    [postcode, int, required]
    [email, string, required]
    [password, string, required]
    """
    __tablename__ = 'stores'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # foreign keys
    
    # field relationships
    games = db.relationship('Game', backref='store', cascade='all, delete')

class StoreSchema(ma.Schema):
    games = fields.List(fields.Nested('GameSchema', exclude=['store']))

    class Meta:
        ordered = True
        fields = ('id', 'name', 'street_number', 'street_name', 'suburb', 
                  'postcode', 'email', 'password', 'games')
        