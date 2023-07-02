# Boardgame Rental Service API

[Trello board](https://trello.com/b/azoCqVE1/boardgame-rental-service-api)   
[Link to Git repository](https://github.com/jophc1/JoshuaPhillips_T2A2)   

### <u>Installation and Setup</u>
Requirements:
PostgreSQL [download guide here](https://www.postgresql.org/download/)
Python3 [download guide here](https://www.python.org/downloads/)

Git Clone the file to a desired location, locate file through terminal and change directory to the 'src' folder e.g. ```jophc@Joshs-MacBook-Pro src %```.   
   
Through terminal, connect to PostgresSQL database:   
```
psql
```   
Create a database that you will use for the API:   
```
CREATE DATABASE example_db;
```   
Connect to this database:   
```
\c example_db
```   
Create a User with a password:   
```
CREATE USER example_user WITH PASSWORD 'examplepassword';
```   
Grant this User access privileges:   
```
GRANT ALL PRIVILEGES ON DATABASE example_db to example_user;
```   
Can now quit out of PostgreSQL:   
```
\q
```   
   
While still in 'src' directory, create a python virtual environment:
```
python3 -m venv .venv
```   
Activate virtual environment:   
```
source .venv/bin/activate
```   
Terminal line should look something like this: 
```
(.venv) jophc@Joshs-MBP src %
```   
Install dependencies and packages through requirements.txt file:   
```
python3 -m pip install -r requirements.txt
```   
In 'src' directory, locate '.env.sample' file. Change this to '.env' and modify the variables within to include the database name, user and user password (more infomation in file):

```
DB_URI="postgresql+psycopg2://example_user:examplepassword@localhost:5432/example_db"
JWT_KEY="exampleSecretKey"
``` 

From terminal in 'src' directory, database tables can now be created and seeded with sample records (Optional: If tables already created, drop tables before recreating by ```flask db drop```):   

```
flask db create   
flask db seed
```   
From these seeds, an administrator user credentials is generated that will be required for some routes:   
```
"email": "admin@bg.com"
"password": "admin123"
```   
Now the flask application can be ran through PORT 5000 (can be changed in .flaskenv):
```
flask run
```


### <u>Identification of problem that is solved by this app</u>

Boardgaming is a increasing popular gaming hobby that has been gaining traction over recent years, with many new board game titles released each year. There are many websites that sell games, search engines to point you towards good sales for board games and even rental services of boardgames offered by individual businesses. However the access of a network for rentals from businesses where the games are loaned by individuals is a largely unexplored area that may pose several advantages over current rental services.   

A large benefit is the prospect of a network of affordable rental games that can cover more than just the major cities. This can be a deal breaker for those looking into getting into the board gaming hobby as buying games can be expensive and shipping is becoming costly. Having insight into what type of games that are availiable locally can help those who are either on a budget, are new to the hobby or just want to try out new games without having to buy could have a cheaper alternative through renting boardgames through designated stores where stock is generally supplied by fellow gamers.   

Another benefit is that is can be a low risk method of revenue for a business as it won't be required to buy and ship stock. Apart from the space that will be required to store game, this rental service can be operated in tandem with their current services which may only require small training or practices with current personal.  

### <u>Why solve this problem?</u>

As of 2022, the board game industry pulled in \$3.13 billion in revenue with an projection of increase to \$3.63 billion in 2023. This shows that board gaming as an industry is increasing at a high level, where 57% of gamers in a survey indicating that they own between 1-25 board/card games with 22% of total people surveyed spending over \$1,000 each year on new games (Georgiev, 2023).   

Not only is board gaming booming as a business, it also brings with it potential medical benefits. A literature review supplied by BioPsychoSocial Medicine indicates that out of 83 relevent articles, there have been multiple randomized trials that show evidence where more traditional board games, like chess, have shown to reduce depression and improve cognitive impairment (Nakao, 2019). It also helps to promote teamwork between people, stimulate creativity, enhance problem-solving and critical thinking and is an excellent tool for social interaction.   

As explored, we have discussed that not only is boardgaming a viable business, it also brings with it positive health and social benefits. However as not everyone has the space or money to spend on board games, this is where a rental service for board games that could provide a larger network so that people are able to access the hobby at low cost.

### <u>Why PostgreSQL was chosen for this API </u>
The chosen database management system is PostgreSQL, which has a long development history starting as far as 1986 when it was first developed and has been made open source with a large community contributing to adding extra features and functionality (Peterson, 2023).    
   
PostgreSQL is a robust database system as it has a good reputation for maintaining data integrity, with ACID (Atomicity, Consistency, Isolation, Durability) compliancy, which means that PostgreSQL will either fully complete or fail a transaction, rolls back all changes a database has made if a transaction fails, separates transactions and ensures that one transaction is complete before starting another and can recover a database to a prior state should a server fail occur. ACID is important for this API as the information stored is required to be as accurate and reliable as possible, with game rental details and store/user accounts being a priority, which can be provided by PostgreSQL (digital ocean, 2022).   
   
As the chosen API framework is Flask, a benefit to using PostgreSQL is also the third-party packages support to allow it to be integrated, which can be paired up with an ORM (Object Relation Mapper) can make it simpler to perform CRUD (Create, Read, Update, Delete) operations onto a database without needing to know complex SQL query syntax. This ultimately gives our API good functionality as it can contain useful end routes.    
   
As the searching, creation or updating of board games can contain many different properties where multiple database tables may be required to access all the relevant information (e.g., a game may need to retrieve designers from another table), PostgreSQL is useful for this as it has native support to allow table joining and ordering which makes querying information from multiple tables a simplified task. It can also allow us to create complex data types and to define relationships between tables  (Dhruv, 2019).   
   
A downside though to using PostgreSQL is that performance can be affected if large amounts of data are stored in the database. This is generally due to the way PostgreSQL reads data as it starts from the first row and continue until the relevant data is found. While this may be a factor if a huge number of games is stored in the database, it seems more relevant that good database design will have a greater affect than how much PostgreSQL can cause on overall performance (Nakao, 2019).   
   
Overall PostgreSQL is a great database management system as it is open source, has excellent data integrity functionality and is relatively easy to use, all which are desirable for this API.    

### <u>Object Relation Mapper (ORM) functionality and benefits</u>

An ORM is generally a software or application that usually connects an API to a database where it essentially acts as a translator for objects in object-oriented programming and the data that is stored in a database. This basically provides a level of abstraction where instead of having to understand and write long complex SQL code, a ORM can provide “mapping” functionality which is a way to relate objects, or “models” which is what is used in the ORM SQLAlchemy that is used with this API, to the tables in a database. This is beneficial as abstracting the process of SQL querying can also reduce the likelihood of an SQL injection attack from being performed as there is no direct connection from the API and the database (Liang, 2021) (Ellingwood, 2023). 

By providing this object to table relation, it makes it easier to do CRUD operations so that data in a database can be queried or manipulated without having to have a deep understanding of the underlying SQL queries that is performed in the database. An example of how a model class from SQLAlchemy can represent a table in PostgreSQL:

![model_example](./docs/model_exp.png)

![table_example](./docs/table_exp.png)

As seen, by using python syntax we can create a table with fields that contain constraints, primary keys, foreign keys and relationships to other tables by a relatively simpler syntax than what would need to be done in raw SQL code. This also simplifies the process of database data manipulation, for example when a new record in table is being inserted verses creating an instance of a model, adding it to a transaction and committing it:   

![model_instance_example](./docs/model_instance_exp.png)   

```
INSERT INTO games(name, year, min_age, price_per_week, quantity, store_id, owner_id)
VALUES (‘Blood Rage’, 2015, 15, 17.50, 4, 1, 2);
```
As seen with both table creation and data record insertion, an ORM abstracts and makes it easier to perform SQL operations without having to write long SQL code. This is the main reason many developers favour using an ORM as it can speed up development times and provide the ability to create relatively complex SQL operations in a programming language that they are more comfortable in.




### <u>Endpoints of this API</u>
[Authentication routes endpoints](./docs/end_points.md#authentication-routes)   
[Game routes endpoints](./docs/end_points.md#games-routes)   
[Rental routes endpoints](./docs/end_points.md#rentals-routes)   

Optional: If you have Postman installed ([installation guide here](https://learning.postman.com/docs/getting-started/installation-and-updates/)), there is a json file located in ```./docs/postman_t2a2_routes.json``` that contains all routes used in this API that can be imported into Postman for testing purposes (more info on importing [here](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman)).

### <u>Third party services used in the API</u>
##### Flask
Flask was chosen as the framework for the development for this API as it is python based, is open source and while it may lack the more advanced functionality that may be found in other API frameworks, it contains enough features to implement a RESTful (Representational State Transfer) API which this project requires (Bharadwaj, 2022).


##### SQLAlchemy
SQLAlchemy is a python based ORM that provides an interface between the API and database to provide CRUD functionality without the need to write complex SQL code (Makai, 2022).

##### Marshmallow
Marshmallow is an additional library that assists with our ORM SQLAlchemy to provide serialization or deserialization of python dictionaries and SQLAlchemy model objects. This will be mainly used with a ‘Schema’ class that can either dump (serialize) an SQLAlchemy model to a Python dictionary to where can be converted to JSON. Likewise, it can be loaded through a Schema class (deserialize) to take in JSON data and convert it to a Python dictionary (Nguyen, 2020). 

##### psycopg2-binary
As SQLAlchemy ORM can be used with different database management systems, an additional package called pyscopg2 is required to provide a database adaptor so that SQLAlchemy can be used with PostgreSQL. The package ‘psycopg2-binary’ is a simplified version of ‘psycopg2’ which lacks more advanced features but works without needing to do additional setup steps. For this reason and considering the scope of the API, we only need psycopg2-binary (pysql.tecladocode.com, 2023) (psycopg.org, 2023).

##### python-dotenv
Python-dotenv is a package that allows our key-value pairs that are in an .env file to be loaded in as environmental variables. As an .env file usually contains sensitive variables like our database connection string and our JWT secret key, python-dotenv enables these variables to be used in our API. It also imports our variables from .flaskenv, which contains flask application configuration values like server port number, default directory for running the flask app and toggling debugging mode (Sasidharan, 2021).

##### flask-sqlalchemy
Flask-sqlalchemy is a package that simplifies the use of SQLAlchemy by providing quality of life features, like sessions that act as a representation of a transaction (flask-sqlalchemy.palletsprojects.com, 2023).

##### flask-marshmallow
Flask-marshmallow is the main package that integrates Marshmallow into Flask, thereby allowing serialization/deserialization of python objects (Loria, 2023).

##### marshmallow-sqlalchemy
Provides an integration layer between Marshmallow and SQLAlchemy so that SQLAlchemy models can be serialized/deserialized (Loria, 2023).
 
##### flask-bcrypt
Flask-bcrypt is a package that provides functionality to convert a string with a hashing algorithm to create an encrypted representation. This is useful for sensitive data like passwords as the password data in a database is stored encrypted, so if there is a data breach the password is practically impossible to decrypt (Countryman, 2023).


##### flask-jwt-extended
This package is for implementing the use of JWT (JSON Web Token) for authorization purposes. A JWT can be generated for an authenticated user which can in turn be provided back to the API which will check if it is a valid JWT and optionally if the identity of the owner of the JWT still exists in the database. While this is a secure way of authorization as the token is only stored on the client's side, this makes it difficult to log out a user, but for the purposes of this API is appropriate as storing user login information is not required (flask-jwt-extended.readthedocs.io, 2023).

### <u>Entities Relationship Diagram (ERD)</u>
![ERD of boardgame rental service database](/docs/erd_t2a2.png)
All tables in the ERD have been normalised up to the third mode, however some duplicated fields were required to be inputted into the 'game_rent_details' table. The reason for the duplicated fields in 'game_rent_details', where it takes fields from 'users' and 'games', is to prevent a deletion anomalie, where if a user either updates their information or deletes their account entirely, a record of crucial information is still maintained for past rentals of boardgames, which can also happen if a game is deleted. As a game record also contains the store id, a record of the store name and address is also need in case that the store deletes their account.   

Keeping copies of these fields is important for record keeping as it allows us to maintain integrity of past rentals of board games, but also keeps accurate information which could be necessary for financial or taxation purposes. 

### <u>Database relations in the application</u>

#### List of Entities
* <u>Stores</u>: contains name, address and login details for a store that will be renting out board games
* <u>Users</u>: contains name and login details for a user. This user can both own and rent out board games with relation to a store.
* <u>Games</u>: has details of a board game, like name, year, rent price, age restriction and quantity that are out for loan.
* <u>Designers</u>: contains the first and last name of a board game designer.
* <u>Game_designers</u>: joining table between games and designers. Contains a game and designer id's to show that a game and designer have a many-to-many relationship.
* <u>Categories</u>: has a category name. Intended to help group board games into different groups.
* <u>Game_categories</u>: joining table for games and categories. Contains a game and category id's which highlights a many-to-many relationship between them.
* <u>Game_rent_details</u>: joining table between users and games, intended to show a many-to-many relationship. Contains game id, user id and a list of fields from games, users and stores which is intended to provide backup details in the case of a record of a user, store or game being deleted. 


#### Stores and Games - One to many relationship

![one-many-store-games](./docs/r9%20database%20relations/store_game_1M.png)

While a store can have many different games to rent out, a game can only belong to a single store. This was done as a game is an owned object by an individual, therefore you cannot have a game being rented out by multiple stores

#### Users and Games - One to many relationship

![one-many-users-games](./docs/r9%20database%20relations/users_games_1M.png)

A user can own many different board games, while a game only owned by one person. Even though it can be possible to own a board game (.e.g couples), for simplicity sakes it was decided that only one owner would be registered to a game.

#### Games and Designers - many to many relationship

![games and designers many-many](./docs/r9%20database%20relations/games_designers_MM.png)

It is possible for a game to have multiple designers that worked on a board game, and a designer can have created many games. To accomadate this relatioship, a joining table called 'game_designers' was created which lists the game id's and designer id's. 

#### Games and Categories - many to many relationship

![games and categories many many](./docs/r9%20database%20relations/games_categories_MM.png)

A game can be listed under multiple different categories, and a category can contain multiple games. To achive this relationship, a joining table 'game_categories' was created that lists the game id's and category id's

#### Users and Games - many to many relationship

![games to users many many](./docs/r9%20database%20relations/games_users_MM.png)

A user can rent out many different games, and a game can be rented out by multiple people at different times. To achieve this relationship, a joining table called 'game_rent_details' was created which lists the user id as the rentee id and the game id. It also lists a copy of some of the game details, the rentees information and the store that is renting the game out. 

### <u>Project model relationships</u>

From the ERD that was designed, a python object representation can now be developed with the use a SQLAlchemy class of a Model to represent a table in a database. First we have to create a Model of each table that is basically an extension of the Model class provided by SQLAlchemy:

```python
class Game(db.Model):
    __tablename__ = 'games'
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    # field names
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    price_per_week = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    
    # foreign keys
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id', ondelete='Cascade'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='Cascade'), nullable=False)
```
As seen in this Game model, the fields of a table are represented as columns with parameters to indicate the type, constraints, primary and foreign keys.   

To show the relationships that tables can have with each other (one-to-one, one-to-many), we can specify another field in the model that will form a relationship to another model:

```python
# field relationships
game_designers = db.relationship('GameDesigner', backref='game', cascade='all, delete')
game_categories = db.relationship('GameCategory', backref='game', cascade='all, delete')
game_rent_details = db.relationship('GameRentDetail', backref='game')
```
There fields, that use the relationship method of a SQLAlchemy instance in the form of 'db' shows that three fields relate to other models which will contain their own field that will refer back to these fields. In the relationship parameters, a model name is specificed, followed by the name of the field that this will relate to (e.g. game_designers forms a connection to game, that is located in the GameDesigner model) through the use of 'backref'. Next we'll discuss how models relate to each other in this API by using our Game model as an example.

#### Games
```python
# foreign keys
store_id = db.Column(db.Integer, db.ForeignKey('stores.id', ondelete='Cascade'), nullable=False)
owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='Cascade'), nullable=False)
    
# field relationships
game_designers = db.relationship('GameDesigner', backref='game', cascade='all, delete')
game_categories = db.relationship('GameCategory', backref='game', cascade='all, delete')
game_rent_details = db.relationship('GameRentDetail', backref='game')
```
Our Game model contains two foreign key, one that connects to the primary key in stores through the store id and another that connects to the primary key in users to the user id. These foreign keys have been set to delete on a cascade, meaning if either a user of store that relates to a record is deleted, the game record is also deleted.  

We also have a one-to-many relationship to GameDesigner, GameCategory and GameRentDetail models where two of these specify to delete the related records in the other models if a record in this model is deleted (aka it'll cascade delete).  

When we come to return a json data back to a client, we can also use a Schema that is part of Marshmallow which can allow us to seralize a model object into a python dictionary that can be jsonified. The advantage of this is that we can specify which fields are return and what to exclude, with our Game Schema returning by default the following fields:

```python   
fields = ('id', 'name', 'year', 'min_age', 'price_per_week', 'quantity', 
        'game_designers', 'game_categories', 'store', 'game_rent_details', 'owner', 'owner_id', 
        'categories', 'designers') 
```

All of these fields except for categories and designers, which are used to load for a specific route, and the fields native to the Game model can be related to another Model Schema which can have their own fields, therefore we can choose the fields that will be displayed in the json:

```python
game_designers = fields.List(fields.Nested('GameDesignerSchema', only=['designer']))
game_categories = fields.List(fields.Nested('GameCategorySchema', only=['category']))
game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', exclude=['game_id', 'game_name', 'store_name', 
                                                                                    'store_street_number', 'store_street_name', 
                                                                                    'store_suburb', 'store_postcode'])) 
owner = fields.Nested('UserSchema', exclude=['games', 'game_rent_details', 'password', 'admin'])
store = fields.Nested('StoreSchema', exclude=['games', 'password'])
```

Our field variables game_designers, game_categories, game_rent_details are Lists, meaning that they can contain more than one value so we have to put these Nested fields into a List method. Also while not specified in the Game Model, there are two more field relationships called owner and store, however because of the way backref works it creates it behind the scenes verses another parameter called back_populates. All these nested fields will indicate which Schema they relate to and if there are any excluded fields from those Schemas, which can be important as this can prevent a circlar imports from occuring.   

All of these ways that foreign keys are used, fields that have relationships pointing to other fields in other models and the use of Schemas that will be used to return json data is also used in other models are all used in similar ways in other models, only differing in what fields their Schemas will return and the establishment of relationships.   

#### Categories
Category Model relationships:
```python
game_categories = db.relationship('GameCategory', backref='category', cascade='all, delete')
```
Category Schema fields (including other Models Nested fields)   
```python
game_categories = fields.List(fields.Nested('GameCategorySchema', exclude=['category']))
    
fields = ('id', 'name', 'game_categories')
```
In our Category model, there is a single relationship called game_categories that connects a field category in the GameCategory Model and indicates a one-to-many relationship between Categories and Game_Categories. This field is a Nested list, which has excluded the category to prevent a circular import. It also indicates to continue a delete onto the model that contains game_categories (GameCategory). By default, the Category Schema will dump id, name and game_categories.

#### Designers
Designer Model relationships:
```python
game_designers = db.relationship('GameDesigner', backref='designer', cascade='all, delete')
```
Designer Schema fields (including other Models Nested fields):
```python
game_designers = fields.List(fields.Nested('GameDesignerSchema', exclude=['designer']))
      
fields = ('id', 'first_name', 'last_name', 'game_designers')
```
Our Designer model has one field relationship, where it refers to a field designer in GameDesigner model which will cascade delete if a designer record is removed and provides a representation of a one-to-many relationship between Designers and Game_Designers. This game_designers is a Nested list that excludes designer from its fields to prevent a circular import. The default fields return by the Schema are the first and last name of the designer and from the Nested fields contained in game_designers.

#### Game_Categories
GameCategory Model foreign keys:
```python
# foreign keys
category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='Cascade'), nullable=False)
game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)  
```
GameCategoy Schema fields (including other Models Nested fields):
```python
category = fields.Nested('CategorySchema', exclude=['game_categories'])
game = fields.Nested('GameSchema', exclude=['game_categories', 'game_rent_details', 'owner', 'owner_id'])
    
fields = ('id', 'category', 'game')
```
This model contains a foreign key that connects to the primary key in Categories and a foreign key that connects to the primary key in Games. In the Schema there are two nested list fields that link to the Category Schema and Game Schema. The Schema will dump by default the id, nested fields in category and nested fields in game.

#### Game_Designers
GameDesigner Model foreign keys:
```python
designer_id = db.Column(db.Integer, db.ForeignKey('designers.id', ondelete='Cascade'), nullable=False)
game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='Cascade'), nullable=False)
```
GameDeigner Schema fields (including other Models Nested fields):
```python
designer = fields.Nested('DesignerSchema', exclude=['game_designers'])
game = fields.Nested('GameSchema', exclude=['game_designers', 'game_rent_details', 'owner', 'owner_id'])
    
fields = ('id', 'designer','game')
```
In the GameDesigner model, two foreign keys are present that connect up to the primary keys in designers and games. The Schema contains two nested field lists that will return by default the id, nested fields in designer and nested fields in game.

#### Stores
Store Model relationships:
```python
games = db.relationship('Game', backref='store', cascade='all, delete')
```
Store Schema fields (including other Models Nested fields):
```python
games = fields.List(fields.Nested('GameSchema', exclude=['store']))

fields = ('id', 'name', 'street_number', 'street_name', 'suburb', 
        'postcode', 'email', 'password', 'games')
```
The Store Model contains a relationship that connects a games field to a store field in the Game model, indicating a one-to-many relationship, where if games is deleted it will cascade to all the related records in Games table and delete them as well. The Store Schema only contains one nested fields list where the Schema will by default return the store details and login details (though in all routes the password is ommited for security reasons) and the nested fields in games.   

#### Users
User Model relationships:
```python
games = db.relationship('Game', backref='owner', cascade='all, delete')
game_rent_details = db.relationship('GameRentDetail', backref='rentee')
```
User Schema fields (including other Models Nested fields):
```python
games = fields.List(fields.Nested('GameSchema', exclude=['game_rent_details','owner']))
game_rent_details = fields.List(fields.Nested('GameRentDetailSchema', exclude=['rentee', 'rentee_first_name', 'rentee_last_name', 'rentee_email', 'rentee_id']))

fields = ('id', 'first_name', 'last_name', 'email', 
        'password', 'admin', 'games', 'game_rent_details')
```
The User Model has one relationship that connects a games field to a game field in the Game Schema, indicating a one-to-many relationship. Another relationship for a field game_rent_details creates a relationship to a rentee field in GameRentDetail Model, indicating a one-to-many relationship. The User Schema contains two nested field lists and returns the fields of the user details (except the password in all routes for security purposes) and the nested fields in games and game_rent_details.

#### Game_Rent_Details
GameRentDetail Model foreign keys:
```python
game_id = db.Column(db.Integer, db.ForeignKey('games.id', ondelete='SET NULL'))
rentee_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
```
GameRentDetail Schema fields:
```python
fields = ('id', 'date', 'rentee_id', 'rentee_first_name', 'rentee_last_name', 'rentee_email', 
        'game_id', 'game_name', 'price_per_week', 'quantity', 'store_name', 
        'store_street_number', 'store_street_name', 'store_suburb', 
        'store_postcode')
```
The GameRentDetail model contains two foreign keys that link up to the primary key in games and users. Both of these foreign keys indicate that a deletion will set the value to NULL instead of deletion that has been the case with other Models. The GameRentDetail Schema contains no nested fields, however it does contain fields that are most copies from other table records in the case of deletion. Most of these fields will be returned/dumped though the Schema except for some ids that irrelevant to a game rental details.

### <u>Project management and task allocation methods</u>

In the early stages of the project before any coding or documentation was to progress, a task organisation system was needed to split up the project into smaller and more manageable task. For this, a Kanban style Trello board was selected as it provides the functionality needed for this project. To begin with, all major sections of the project and documentation were identified:   
![task list 1st part](./docs/r10%20trello/tasks1.png)
![task list 2nd part](./docs/r10%20trello/tasks2.png)
With each task, a checklist of items was created to break the task down into smaller sections:   
![task checklist](./docs/r10%20trello/task%20checklist.png)   
In these individual tasks cards, a complexity rating, a priority scale and a due date were assigned to further organise the order of the tasks:   
![task priority, complexity, date](./docs/r10%20trello/complex%20priority%20date.png)   
The task cards can now be assigned and ordered on the trello board:   
![task list construction](./docs/r10%20trello/task%20construction.png)   
To help identify key functionalities of the API, a set of user stories was collected:   
![user stories 1st part](./docs/r10%20trello/user%20stories%201.png)
![user stories 2nd part](./docs/r10%20trello/user%20stories%202.png)   
Within each user story, the tasks and routes were identified that would be needed to be implemented into the API:   
![user story construction](./docs/r10%20trello/user%20story%20construction.png)   
Now that all tasks and user stories have been identified and cataloged, the project could now progress into the documentation and coding development phase, where each task or user story was examined at different times of the project to make sure that the timeline was being meet. Generally at a single time only only task card would be worked on depending on priority and date due, which when complete would be moved to the 'Finished' column and a new task would be set to 'In Progress'.    
Overall the trello board is a useful tool as it breaks down complex tasks, helps brainstorm ideas and generally reduces development time of a project.   
![trello board overview](./docs/r10%20trello/trello%20overview.png)

#### <u>References</u>

Bharadwaj, A., 2022. Python | Build a REST API using Flask. [Online] 
Available at: https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/
[Accessed 1 July 2023].   

Countryman, M., 2023. Flask-Bcrypt. [Online] 
Available at: https://pypi.org/project/Flask-Bcrypt/
[Accessed 1 July 2023].   

Dhruv, S., 2019. PostgreSQL Advantages and Disadvantages. [Online] 
Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/
[Accessed 30 June 2023].   

digital ocean, 2022. ACID Compliance. [Online] 
Available at: https://docs.digitalocean.com/glossary/acid/
[Accessed 30 June 2023].   

Ellingwood, J., 2023. What is an ORM?. [Online] 
Available at: https://www.prisma.io/dataguide/types/relational/what-is-an-orm
[Accessed 1 July 2023].   

flask-jwt-extended.readthedocs.io, 2023. Basic Usage. [Online] 
Available at: https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage.html
[Accessed 1 July 2023].   

flask-sqlalchemy.palletsprojects.com, 2023. Flask SQLAlchemy. [Online] 
Available at: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/
[Accessed 1 July 2023].   

Georgiev, D., 2023. 13 Board Game Statistics - All You Need to Know in 2023. [Online] 
Available at: https://techjury.net/blog/board-game-statistics/
[Accessed 22 June 2023].   

Liang, M., 2021. Understanding Object-Relational Mapping: Pros, Cons, and Types. [Online] 
Available at: https://www.altexsoft.com/blog/object-relational-mapping/
[Accessed 1 July 2023].   

Loria, S., 2023. Flask + marshmallow for beautiful APIs. [Online] 
Available at: https://pypi.org/project/flask-marshmallow/
[Accessed 1 July 2023].   

Loria, S., 2023. marshmallow-sqlalchemy. [Online] 
Available at: https://marshmallow-sqlalchemy.readthedocs.io/en/latest/
[Accessed 1 July 2023].   

Makai, M., 2022. SQLAlchemy. [Online] 
Available at: https://www.fullstackpython.com/sqlalchemy.html
[Accessed 1 July 2023].   

Nakao, M., 2019. Special series on “effects of board games on health education and promotion” board games as a promising tool for health promotion: a review of recent literature. [Online] 
Available at: https://bpsmedicine.biomedcentral.com/articles/10.1186/s13030-019-0146-3
[Accessed 22 June 2023].   

Nguyen, M., 2020. Marshmallow: Easy Serialization in Python. [Online] 
Available at: https://blog.knoldus.com/marshmallow-easy-serialization-in-python/
[Accessed 1 July 2023].   

Peterson, R., 2023. What is PostgreSQL? Introduction, Advantages & Disadvantages. [Online] 
Available at: https://www.guru99.com/introduction-postgresql.html
[Accessed 30 June 2023].   

psycopg.org, 2023. Psycopg – PostgreSQL database adapter for Python. [Online] 
Available at: https://www.psycopg.org/docs/
[Accessed 1 July 2023].   

pysql.tecladocode.com, 2023. PostgreSQL Python Libraries: psycopg2 and psycopg2-binary. [Online] 
Available at: https://pysql.tecladocode.com/section05/lectures/04_psycopg2_vs_psycopg2-binary/
[Accessed 1 July 2023].   

Sasidharan, 2021. Flask and .env. [Online] 
Available at: https://dev.to/sasicodes/flask-and-env-22am
[Accessed 1 July 2023].   






