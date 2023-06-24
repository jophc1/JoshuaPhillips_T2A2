from init import db, ma

class Designer(db.Model):
    __tablename__ = 'designers'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    # foreign keys
   
    # field relationships
    

class DesignerSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'first_name', 'last_name')