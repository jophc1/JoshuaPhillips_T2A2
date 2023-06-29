# Boardgame Rental Service API

[Trello board](https://trello.com/b/azoCqVE1/boardgame-rental-service-api)   
[Link to Git repository](https://github.com/jophc1/JoshuaPhillips_T2A2)   

### <u>Installation and Setup</u>

### <u>Identification of problem that is solved by this app</u>

Boardgaming is a increasing popular gaming hobby that has been gaining traction over recent years, with many new board game titles released each year. There are many websites that sell games, search engines to point you towards good sales for board games and even rental services of boardgames offered by individual businesses. However the access of a network for rentals from businesses where the games are loaned by individuals is a largely unexplored area that may pose several advantages over current rental services.   

A large benefit is the prospect of a network of affordable rental games that can cover more than just the major cities. This can be a deal breaker for those looking into getting into the board gaming hobby as buying games can be expensive and shipping is becoming costly. Having insight into what type of games that are availiable locally can help those who are either on a budget, are new to the hobby or just want to try out new games without having to buy could have a cheaper alternative through renting boardgames through designated stores where stock is generally supplied by fellow gamers.   

Another benefit is that is can be a low risk method of revenue for a business as it won't be required to buy and ship stock. Apart from the space that will be required to store game, this rental service can be operated in tandem with their current services which may only require small training or practices with current personal.  

### <u>Why solve this problem?</u>

As of 2022, the board game industry pulled in \$3.13 billion in revenue with an projection of increase to \$3.63 billion in 2023. This shows that board gaming as an industry is increasing at a high level, where 57% of gamers in a survey indicating that they own between 1-25 board/card games with 22% of total people surveyed spending over \$1,000 each year on new games (Georgiev, 2023).   

Not only is board gaming booming as a business, it also brings with it potential medical benefits. A literature review supplied by BioPsychoSocial Medicine indicates that out of 83 relevent articles, there have been multiple randomized trials that show evidence where more traditional board games, like chess, have shown to reduce depression and improve cognitive impairment (Nakao, 2019). It also helps to promote teamwork between people, stimulate creativity, enhance problem-solving and critical thinking and is an excellent tool for social interaction.   

As explored, we have discussed that not only is boardgaming a viable business, it also brings with it positive health and social benefits. However as not everyone has the space or money to spend on board games, this is where a rental service for board games that could provide a larger network so that people are able to access the hobby at low cost.

### <u>The choice of PostgreSQL and the drawbacks compared to other database systems</u>

### <u>Functionalities and Benefits of an ORM</u>

### <u>Endpoints of this API</u>
[Authentication routes endpoints](./docs/end_points.md#authentication-routes)   
[Game routes endpoints](./docs/end_points.md#games-routes)   
[Rental routes endpoints](./docs/end_points.md#rentals-routes)   


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

Georgiev, D., 2023. 13 Board Game Statistics - All You Need to Know in 2023. [Online] 
Available at: https://techjury.net/blog/board-game-statistics/
[Accessed 22 June 2023].   

Nakao, M., 2019. Special series on “effects of board games on health education and promotion” board games as a promising tool for health promotion: a review of recent literature. [Online] 
Available at: https://bpsmedicine.biomedcentral.com/articles/10.1186/s13030-019-0146-3
[Accessed 22 June 2023].


