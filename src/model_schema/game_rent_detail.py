from init import db, ma

class GameRentDetail(db.Model):
    __tablename__ = 'game_rent_details'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
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
    rental_id = db.Column(db.Integer, db.ForeignKey('rentals.id', ondelete='Cascade'), nullable=False)
    # field relationships
    
class GameRentDetailSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'game_name', 'price_per_week', 'quantity', 'store_name', 
                  'store_street_number', 'store_street_name', 'store_suburb', 'store_postcode')