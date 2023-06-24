from init import db, ma

VALID_CATEGORIES = ('deck building', 'worker placement', 'abstract', 'euro', 'wargame')

class Category(db.Model):
    __tablename__ = 'categories'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    # foreign keys
   
    # field relationships
    

class CategorySchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'name')