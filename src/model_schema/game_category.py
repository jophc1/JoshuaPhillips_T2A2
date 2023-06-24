from init import db, ma

class GameCategory(db.Model):
    __tablename__ = 'game_categories'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    
    # foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey('designers.id', ondelete='SET NULL'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)
    # field relationships
    

class GameCategorySchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'category_id', 'game_id')