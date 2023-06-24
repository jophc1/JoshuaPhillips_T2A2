from init import db, ma

class Rental(db.Model):
    __tablename__ = 'rentals'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    date = db.Column(db.Date, nullable=False)
    rentee_first_name = db.Column(db.String, nullable=False)
    rentee_last_name = db.Column(db.String, nullable=False)
    rentee_email = db.Column(db.String, nullable=False, unique=True)
    # foreign keys
    rentee_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    # field relationships
    

class RentalSchema(ma.Schema):


    class Meta:
        ordered = True
        fields = ('id', 'date', 'rentee_first_name', 'rentee_last_name', 'rentee_email', 'rentee_id')