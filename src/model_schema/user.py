from init import db, ma


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
    

class UserSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'admin')
        load_only = ('password, admin')