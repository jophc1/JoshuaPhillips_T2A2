from init import db, ma

class Store(db.Model):
    __tablename__ = 'stores'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    # foreign keys
    
    # field relationships
    

class StoreSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'name', 'street_number', 'street_name', 'suburb', 'postcode', 'phone', 'email', 'password', 'admin')
        load_only = ('password, admin')