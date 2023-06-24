from init import db, ma

class Game(db.Model):
    __tablename__ = 'games'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    min_age = db.Column(db.Integer, nullable=False)
    price_per_week = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    # foreign keys
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id', ondelete='Cascade'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='Cascade'), nullable=False)
    
    # field relationships
    

class GameSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'name', 'year', 'min_age', 'price_per_week', 'quantity')
        load_only = ('password, admin')