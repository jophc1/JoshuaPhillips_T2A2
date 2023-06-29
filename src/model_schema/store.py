from init import db, ma
from marshmallow import fields
from marshmallow.validate import And, Regexp, Range, Length

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

    name = fields.String(required=True, validate=And(Regexp('^[A-Za-z !,]+$', error='store name must only contain letters, spaces and special characters [!,]'), 
                                                     Length(min=1, max=30)))
    street_number = fields.Integer(required=True, validate=Range(min=1))
    street_name = fields.String(required=True, validate=And(Regexp('^[A-Za-z ]+$', error='store name must only contain letters and spaces e.g Shield Street'), 
                                                     Length(min=4, max=20)))
    suburb = fields.String(required=True, validate=And(Regexp('^[A-Za-z ]+$', error='store name must only contain letters and spaces e.g Shield Street'), 
                                                     Length(min=4, max=20)))
    postcode = fields.Integer(required=True, validate=Range(min=800, max=9999))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=8, max=30))
    
    class Meta:
        ordered = True
        fields = ('id', 'name', 'street_number', 'street_name', 'suburb', 
                  'postcode', 'email', 'password', 'games')
        
class UpdateStoreSchema(ma.Schema): 
    name = fields.String(required=False, validate=And(Regexp('^[A-Za-z !,]+$', error='store name must only contain letters, spaces and special characters [!,]'), 
                                                     Length(min=1, max=30)))
    street_number = fields.Integer(required=False, validate=Range(min=1))
    street_name = fields.String(required=False, validate=And(Regexp('^[A-Za-z ]+$', error='store name must only contain letters and spaces e.g Shield Street'), 
                                                     Length(min=4, max=20)))
    suburb = fields.String(required=False, validate=And(Regexp('^[A-Za-z ]+$', error='store name must only contain letters and spaces e.g Shield Street'), 
                                                     Length(min=4, max=20)))
    postcode = fields.Integer(required=False, validate=Range(min=800, max=9999))
    email = fields.Email(required=False)
    
    
    class Meta:
        ordered = True
        fields = ()       