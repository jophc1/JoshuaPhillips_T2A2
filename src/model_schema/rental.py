from init import db, ma
from marshmallow import fields

class Rental(db.Model):
    """
    Model for Rental, fields are (field name, field type, requirement?):
    [date, string(yyyy/mm/dd), required]
    [rentee_id, int, required]
    [rentee_first_name, string, required]
    [rentee_last_name, string, required]
    [rentee_email, string, required]
    """
    __tablename__ = 'rentals'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    date = db.Column(db.Date, nullable=False)
    rentee_first_name = db.Column(db.String, nullable=False)
    rentee_last_name = db.Column(db.String, nullable=False)
    rentee_email = db.Column(db.String, nullable=False)
    # foreign keys
    rentee_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    # field relationships
    game_rent_details = db.relationship('GameRentDetail', backref='rental', cascade='all, delete')

class RentalSchema(ma.Schema):
    game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', exclude=['rental']))

    class Meta:
        ordered = True
        fields = ('id', 'date', 'rentee_id','rentee_first_name', 
                  'rentee_last_name', 'rentee_email', 'game_rent_details')