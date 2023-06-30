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
python3 -m pip install -r requirement.txt
```   
In 'src' directory, locate '.env.sample' file. Change this to '.env' and add the required fields (more infomation in file):

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
email = admin@bg.com
password = admin123
```   
Now the flask application can be ran through PORT 5000 (can be changed in .flaskenv):
```flask run```


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

### <u>Functionalities and Benefits of an ORM</u>





### <u>Endpoints of this API</u>
[Authentication routes endpoints](./docs/end_points.md#authentication-routes)   
[Game routes endpoints](./docs/end_points.md#games-routes)   
[Rental routes endpoints](./docs/end_points.md#rentals-routes)   

Optional: If you have Postman installed (https://learning.postman.com/docs/getting-started/installation-and-updates/), there is a json file located in ```./docs/postman_t2a2_routes.json``` that contains all routes used in this API that can be imported into Postman for testing purposes (more info on importing here: https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman).

### <u>Entities Relationship Diagram (ERD)</u>
NEEDS REWORDING 
![ERD of boardgame rental service database](/docs/erd_t2a2.png)
All tables in the ERD have been normalised up to the third mode, however some duplicated fields were required to be inputted into the 'rental' and 'game_rent_detail' tables. The reason for the duplicated fields in 'rental' where it fields from 'user' is to prevent a deletion anomalie, where if a user either updates there information or deletes there account entirely, a record of crucial information is still maintained for past rentals of boardgames.    

The same scenario happens with 'game_rent_detail', where it duplicates some fields from 'game' and 'store'. If either a games weekly rental price is changed or a game is removed, a copy of the rental weekly price and boardgame name is kept. Likewise a copy of the store name and address is also stored in the case that the store is removed or the store no longer hosts that particular game.

Keeping copies of these fields in both of these tables is important for record keeping, as it allows us to maintain integrity of past rentals of board games, but also keeps accurate information which could be necessary for financial or taxation purposes.

### <u>Third party services used in the API</u>

Flask

SQLAlchemy

Marshmallow

Psycopg2-binary

Python-Dotenv

Flask-SQLAlchemy

Flask-Marshmallow

Flask-Bcrypt

Flask-JWT-Extended

### <u>Relationships of the project models</u>

### <u>Implementation of Database relations in the application</u>

### <u>Project management and task allocation methods</u>

Trello board

User stories


#### <u>References</u>

Dhruv, S., 2019. PostgreSQL Advantages and Disadvantages. [Online] 
Available at: https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/
[Accessed 30 June 2023].

digital ocean, 2022. ACID Compliance. [Online] 
Available at: https://docs.digitalocean.com/glossary/acid/
[Accessed 30 June 2023].

Georgiev, D., 2023. 13 Board Game Statistics - All You Need to Know in 2023. [Online] 
Available at: https://techjury.net/blog/board-game-statistics/
[Accessed 22 June 2023].

Nakao, M., 2019. Special series on “effects of board games on health education and promotion” board games as a promising tool for health promotion: a review of recent literature. [Online] 
Available at: https://bpsmedicine.biomedcentral.com/articles/10.1186/s13030-019-0146-3
[Accessed 22 June 2023].

Peterson, R., 2023. What is PostgreSQL? Introduction, Advantages & Disadvantages. [Online] 
Available at: https://www.guru99.com/introduction-postgresql.html
[Accessed 30 June 2023].




