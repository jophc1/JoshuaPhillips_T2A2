from init import db, ma

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
    [admin, boolean, default=False]
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
    admin = db.Column(db.Boolean, default=False)
    # foreign keys
    
    # field relationships
    

class StoreSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'name', 'street_number', 'street_name', 'suburb', 'postcode', 'phone', 'email', 'password', 'admin')
        load_only = ('password, admin')