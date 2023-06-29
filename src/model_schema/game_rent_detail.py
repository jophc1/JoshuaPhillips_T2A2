from init import db, ma
from marshmallow import fields
from marshmallow.validate import Range

class GameRentDetail(db.Model):
    """
    Model for GameRentDetail, fields are (field name, field type, requirement?):
    [date, string(yyyy/mm/dd), required]
    [rentee_id, int, required]
    [rentee_first_name, string, required]
    [rentee_last_name, string, required]
    [rentee_email, string, required]
    [game_id, int, required]
    [game_name, string, required]
    [price_per_week, float, required]
    [quantity, int, required]
    [store_name, string, required]
    [store_street_number, int, required]
    [store_street_name, string, required]
    [store_suburb, string, required]
    [store_postcode, int, required]
    """
    __tablename__ = 'game_rent_details'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    date = db.Column(db.Date, nullable=False)
    rentee_first_name = db.Column(db.String, nullable=False)
    rentee_last_name = db.Column(db.String, nullable=False)
    rentee_email = db.Column(db.String, nullable=False)
    game_name = db.Column(db.String, nullable=False)
    price_per_week = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    store_name = db.Column(db.String, nullable=False)
    store_street_number = db.Column(db.Integer, nullable=False)
    store_street_name = db.Column(db.String, nullable=False)
    store_suburb = db.Column(db.String, nullable=False)
    store_postcode = db.Column(db.Integer, nullable=False)
    
    # foreign keys
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='SET NULL'))
    rentee_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    # field relationships
    
class GameRentDetailSchema(ma.Schema):
    
    
    class Meta:
        ordered = True
        fields = ('id', 'date', 'rentee_id', 'rentee_first_name', 'rentee_last_name', 'rentee_email', 
                  'game_id', 'game_name', 'price_per_week', 'quantity', 'store_name', 
                  'store_street_number', 'store_street_name', 'store_suburb', 
                  'store_postcode') # 'game' may not be needed
        
class CreateRentalSchema(ma.Schema):
    rentee_id = fields.Integer(required=True, validate=Range(min=1))
    game_id = fields.Integer(required=True, validate=Range(min=1))
    quantity = fields.Integer(required=True, validate=Range(min=1))
    
    class Meta:
        ordered = True
        fields = ('rentee_id', 'game_id', 'quantity')
