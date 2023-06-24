from init import db, ma

class GameDesigner(db.Model):
    __tablename__ = 'game_designers'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    
    # foreign keys
    designer_id = db.Column(db.Integer, db.ForeignKey('designers.id', ondelete='SET NULL'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)
    # field relationships
    

class GameDesignerSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'designer_id', 'game_id')