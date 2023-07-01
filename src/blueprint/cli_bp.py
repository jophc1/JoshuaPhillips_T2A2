from init import db, bcrypt
from flask import Blueprint
from model_schema.category import Category
from model_schema.designer import Designer
from model_schema.game import Game
from model_schema.game_category import GameCategory
from model_schema.game_designer import GameDesigner
from model_schema.game_rent_detail import GameRentDetail
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
    # Seeding users table in database   
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
    
    # Seeding stores table in database
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
    
    # Seeding games table in database
    games = [
        Game(
            name = 'Blood Rage'.title(),
            year = 2015,
            min_age = 15,
            price_per_week = 17.50,
            quantity = 4,
            store_id = stores[0].id,
            owner_id = users[1].id
    ),
        Game(
            name = 'Dominion'.title(),
            year = 2008,
            min_age = 11,
            price_per_week = 13.49,
            quantity = 3,
            store_id = stores[1].id,
            owner_id = users[2].id
    ),
        Game(
            name = 'Ticket To Ride'.title(),
            year = 2005,
            min_age = 5,
            price_per_week = 15,
            quantity = 2,
            store_id = stores[2].id,
            owner_id = users[3].id
    ),
        Game(
            name = 'Pandemic'.title(),
            year = 2007,
            min_age = 12,
            price_per_week = 10.99,
            quantity = 1,
            store_id = stores[0].id,
            owner_id = users[1].id
    ),
        Game(
            name = 'Carcassonne'.title(),
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
    
    
    # Seeding game_rent_details table in database
    dates = ['2023/05/25', '2023/06/18', '2023/06/19', '2023/06/25']
    rentees = [users[2], users[3], users[1], users[1]]
    rent_games = [games[0], games[4], games[2], games[1]]
    rental_stores = [get_store(rent_games[x].store_id) for x in range(len(rent_games))]
    quantities = [1, 2, 1, 2]

    db.session.query(GameRentDetail).delete()
    
    for index in range(len(rent_games)):
        rental_detail = GameRentDetail(
                date = dates[index], 
                rentee_id = rentees[index].id,
                rentee_first_name = rentees[index].first_name,
                rentee_last_name = rentees[index].last_name,
                rentee_email = rentees[index].email,
                game_id = rent_games[index].id,
                game_name = rent_games[index].name,
                price_per_week = rent_games[index].price_per_week,
                quantity = quantities[index],
                store_name = rental_stores[index].name,
                store_street_number = rental_stores[index].street_number,
                store_street_name = rental_stores[index].street_name,
                store_suburb = rental_stores[index].suburb,
                store_postcode = rental_stores[index].postcode
        )
        db.session.add(rental_detail)
    
    db.session.commit()
    
    # Seeding designers table in database (first and last name must have capitals on each word ie 'eric' must be 'Eric')
    designers = [
        Designer(
            first_name = 'Eric'.title(),
            last_name = 'Lang'.title()
    ),
        Designer(
            first_name = 'Donald'.title(),
            last_name = 'Vaccarino'.title()
    ),
        Designer(
            first_name = 'Alan'.title(),
            last_name = 'Moon'.title()
    ),
        Designer(
            first_name = 'Matt'.title(),
            last_name = 'Leecock'.title()
    ),
        Designer(
            first_name = 'Klaus-Jurgen'.title(),
            last_name = 'Wrede'.title()
    )
    ]
    
    db.session.query(Designer).delete()
    db.session.add_all(designers)
    db.session.commit()
    
    # Seeding game_designers table in database
    game_designers = [
        GameDesigner(
            designer_id = designers[0].id,
            game_id = games[0].id
    ),
        GameDesigner(
            designer_id = designers[1].id,
            game_id = games[1].id
    ),
        GameDesigner(
            designer_id = designers[2].id,
            game_id = games[2].id
    ),
        GameDesigner(
            designer_id = designers[3].id,
            game_id = games[3].id
    ),
        GameDesigner(
            designer_id = designers[4].id,
            game_id = games[4].id
    )
    ]
    
    db.session.query(GameDesigner).delete()
    db.session.add_all(game_designers)
    db.session.commit()
    
    # Seeding categories table in database (category names must be capital on each word ie 'deck building' must be 'Deck Building')
    categories = [
        Category(
            name = 'Deck Building'.title()
    ),
        Category(
            name = 'Worker Placement'.title()
    ),
        Category(
            name = 'Abstract'.title()
    ),
        Category(
            name = 'Euro'.title()
    ),
        Category(
            name = 'Wargame'.title()
    )
    ]
    
    db.session.query(Category).delete()
    db.session.add_all(categories)
    db.session.commit()
    
    # Seeding game_categories table in database
    game_categories = [
        GameCategory(
            category_id = categories[1].id,
            game_id = games[0].id
    ),
        GameCategory(
            category_id = categories[4].id,
            game_id = games[0].id
    ),
        GameCategory(
            category_id = categories[0].id,
            game_id = games[1].id
    ),
        GameCategory(
            category_id = categories[1].id,
            game_id = games[2].id
    ),
        GameCategory(
            category_id = categories[3].id,
            game_id = games[2].id
    ),
        GameCategory(
            category_id = categories[2].id,
            game_id = games[3].id
    ),
        GameCategory(
            category_id = categories[3].id,
            game_id = games[4].id
    )
    ]
    
    db.session.query(GameCategory).delete()
    db.session.add_all(game_categories)
    db.session.commit()
    
    print('Tables seeded')
    

def get_store(store_id):
    stmt = db.select(Store).filter_by(id=store_id)
    return db.session.scalar(stmt)


