from init import db, bcrypt
from flask import Blueprint
from model_schema.category import Category
from model_schema.designer import Designer
from model_schema.game import Game
from model_schema.game_category import GameCategory
from model_schema.game_designer import GameDesigner
from model_schema.game_rent_detail import GameRentDetail
from model_schema.rental import Rental
from model_schema.store import Store
from model_schema.user import User

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables dropped')
    
@db_commands.cli.command('seed')
def seed_db():
    
    users = [
        User(
        first_name = 'John',
        last_name = 'Smith',
        email = 'admin@bg.com',
        password = bcrypt.generate_password_hash('admin123').decode('UTF-8'),
        admin = True
    ),
        User(
        first_name = 'Sally',
        last_name = 'McDonald',
        email = 'sally@yahoo.com',
        password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    ),
        User(
        first_name = 'Greg',
        last_name = 'Layland',
        email = 'greggory@gmail.com',
        password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    ),
        User(
        first_name = 'Naomi',
        last_name = 'Fairfield',
        email = 'nfair@gmail.com',
        password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    )
    ]
    
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    
    stores = [
        Store(
            name = 'Play more games Inc',
            street_number = 25,
            street_name = 'Lake st',
            suburb = 'Cairns',
            postcode = 4870,
            email = 'services@playmore.com',
            password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    ),
        Store(
            name = 'Random Dice Ltd',
            street_number = 11,
            street_name = 'Griffin st',
            suburb = 'Cairns',
            postcode = 4870,
            email = 'bookings@randomdice.com',
            password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    ),
        Store(
            name = 'Blue Wizard Gaming Pty Ltd',
            street_number = 5,
            street_name = 'Shannon Dr',
            suburb = 'Cairns',
            postcode = 4870,
            email = 'administration@bluewizard.com',
            password = bcrypt.generate_password_hash('12345678').decode('UTF-8')
    )
    ]
    
    db.session.query(Store).delete()
    db.session.add_all(stores)
    db.session.commit()
    
    games = [
        Game(
            name = 'Blood Rage',
            year = 2015,
            min_age = 15,
            price_per_week = 17.50,
            quantity = 1,
            store_id = stores[0].id,
            owner_id = users[1].id
    ),
        Game(
            name = 'Dominion',
            year = 2008,
            min_age = 11,
            price_per_week = 13.49,
            quantity = 3,
            store_id = stores[1].id,
            owner_id = users[2].id
    ),
        Game(
            name = 'Ticket to ride',
            year = 2005,
            min_age = 5,
            price_per_week = 15,
            quantity = 2,
            store_id = stores[2].id,
            owner_id = users[3].id
    ),
        Game(
            name = 'Pandemic',
            year = 2007,
            min_age = 12,
            price_per_week = 10.99,
            quantity = 1,
            store_id = stores[0].id,
            owner_id = users[1].id
    ),
        Game(
            name = 'Carcassonne',
            year = 2000,
            min_age = 7,
            price_per_week = 8.50,
            quantity = 3,
            store_id = stores[1].id,
            owner_id = users[2].id
    )
    ]
    
    db.session.query(Game).delete()
    db.session.add_all(games)
    db.session.commit()
    
    rentals = [
        Rental(
        date = '2023/05/25',
        rentee_id = users[1].id,
        rentee_first_name = users[1].first_name,
        rentee_last_name = users[1].last_name,
        rentee_email = users[1].email
    ),
        Rental(
        date = '2023/06/18',
        rentee_id = users[2].id,
        rentee_first_name = users[2].first_name,
        rentee_last_name = users[2].last_name,
        rentee_email = users[2].email
    ),
        Rental(
        date = '2023/06/19',
        rentee_id = users[1].id,
        rentee_first_name = users[1].first_name,
        rentee_last_name = users[1].last_name,
        rentee_email = users[1].email
    ),
        Rental(
        date = '2023/06/25',
        rentee_id = users[3].id,
        rentee_first_name = users[3].first_name,
        rentee_last_name = users[3].last_name,
        rentee_email = users[3].email
    )
    ]
    
    db.session.query(Rental).delete()
    db.session.add_all(rentals)
    db.session.commit()
    
    print('Tables seeded')
    



