from init import db, ma
from marshmallow import fields


class User(db.Model):
    """
    Model for User, fields are (field name, field type, requirement?):
    [first_name, string, required]
    [last_name, string, required]
    [email, string, required]
    [password, string, required]
    [admin, boolean, default=False]
    """
    __tablename__ = 'users'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    # foreign keys
    
    # field relationships
    games = db.relationship('Game', backref='owner', cascade='all, delete')
    game_rent_details = db.relationship('GameRentDetail', backref='rentee')

class UserSchema(ma.Schema):
    games = fields.List(fields.Nested('GameSchema', exclude=['game_rent_details','owner']))
    game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', exclude=['rentee', 'rentee_first_name', 
                                                                                   'rentee_last_name', 
                                                                                   'rentee_email', 'rentee_id']))

    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name', 'email', 
                  'password', 'admin', 'games', 'game_rent_details')
        