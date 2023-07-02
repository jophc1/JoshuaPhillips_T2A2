## Boardgame Rental API Endpoints documentation
[Return to main page](../README.md)

[Authentication routes](#authentication-routes)     
[Games routes](#games-routes)   
[Rentals routes](#rentals-routes)   
   
### Authentication routes   
#### POST Register User
Route: /register/user    
Method/s: POST   
Description: Allows a new user account to be created with a JWT returned  
Authentication required: No    
Additional account permission: No
<u>Query Parameters</u>   
* Mandatory (key name, type):  
(first_name, string)   
(last_name, string)   
(email, string)   
(password, string)
* Optional (key name, type):   
n/a

example route URI:   
```
127.0.0.1:5000/register/user
```
example request body:   
```
{
    "first_name": "Franny",
    "last_name": "Rego",
    "email": "franny@gmail.com",
    "password": "12345678"
}
```
example request response:
```
{
    "user": {
        "email": "franny@gmail.com",
        "first_name": "Franny",
        "last_name": "Rego"
    },
    "token": "eyJhbGCiOiJIUzI1NiIsInR4cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAyNZY3MSwianRpIjoiMjI1MTYwZWYtMThjNC00Y2YyLWI0OTAtYzcyZThjMTU0MmI3IiwidHlwZSI6IrFjY2VzcyIsInN1YiI6WzUsImZyYW5ueUBnbWFpbC5jb20iXSwibmJmIjoxNjg4MDI3NjcxLCJleHAiOjE2ODgwMzg0NzF9.bAGLmO8B5G7I3yVB6XsdHrkIUWvtAlGa3bQbAXjwQyI"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Register Store
Route: /register/store  
Method/s: POST  
Description: Creates a new store account with a JWT returned  
Authentication required: Yes  
Additional account permission: Have a JWT associated with a User account with administrator privileges   
<u>Query Parameters</u>   
* Mandatory (key name, type):  
(name, string)   
(street_number, int)   
(street_name, string)   
(suburb, string)   
(postcode, int)   
(email, string)   
(password, string)

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/register/store
```
example request body:   
```
{
    "name": "Have fun gaming",
    "street_number": 70,
    "street_name": "Ronald Dr",
    "suburb": "Cairns",
    "postcode": 4870,
    "email": "have@fungaming.com",
    "password": "12345678"
}
```
example request response:
```
{
    "store": {
        "name": "Have fun gaming",
        "email": "have@fungaming.com"
    },
    "token": "eyJhcGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAyODEwNywianRpIjoiZDlmYTg4NGQtMzAzMC00YzYzLTgyMmMtZjJiNTMxODa5ZjkxIiwidHlwZSI6ImFJY2VzcyIsInN1YiI6WzQsImhhdmVAZnVuZ2FtaW5nLmNvbSJdLCJuYmYiOjE2ODgwMjgxMDcsImv4cCI6MTY4ODAzODkwN30.kdutfMBYAP4nJCm10cTAA_8wBQZ7PUNhqRQnsTwvfdU"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Login User
Route: /login/user     
Method/s: POST    
Description: Generates and returns a JWT if a valid User account is found  
Authentication required: No  
Additional account permission: No  
<u>Query Parameters</u>   
* Mandatory (key name, type):  
(email, string)   
(password, string)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/login/user
```
example request body:   
```
{
    "email": "admin@bg.com",
    "password": "admin123"
}
```
example request response:   
```
{
    "user": {
        "email": "admin@bg.com"
    },
    "token": "eyJhbGciOiJIuzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAyODA4MywianRpIjoiODg1NmMwNGUtY2E4Ni00YTY4LTg2NGQtYWQ4ZDkzNzQyNWM3IiwidHlWZSI6ImFjY2VzcyISInN1YiI6WzEsImFkbWluQGJnLmNvbSJdLCJuYmYiOjE2ODgwMjgwODMsImV4cCI6MTY4ODAzODg4M30.vkA4AMR7VdqwYb3dX-wIzsmpw3O3TY0RrJjVURjgmeo"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Login Store
Route: /login/store  
Method/s: POST  
Description: Generates a JWT if a valid Store account is found  
Authentication required: No  
Additional account permission: No  
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(email, string)   
(password, string)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/login/store
```
example request body:   
```
{
    "email": "services@playmore.com",
    "password": "12345678"
}
```
example request response:   
```
{
    "store": {
        "email": "services@playmore.com"
    },
    "token": "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAyOtUzMiwianRpIjoiZjA0MzFmMmItYjc3OS00ZGEyLTk1NDYtNmU2NWZiZDA1Njg3IiwidHlwZSI6ImFjY2VicyIsInN1YiI6WzEsInNlcnZpY2VzQHBsYXltb3JlLmNvbSJdLCJuYmYiOjE2ODgwMjk1MzIsImV4cCI6MTY4ODA0MDMzMn0.LVnMdq_QGypEohT4ZKDZZUldgtsjotY30Xe3De8Z_IM"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### PUT/PATCH Update User 
Route: /user    
Method/s: PUT, PATCH    
Description: Change the name details of a user   
Authentication required: Yes 
Additional account permission: Have a JWT associated with a User      
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
(first_name, string)   
(last_name, string)   

example route URI:   
```
127.0.0.1:5000/user
```
example request body:   
```
{
    "first_name": "John",
    "last_name": "Daniels"
}
```
example request response:   
```
{
    "first_name": "John",
    "last_name": "Daniels"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### PUT/PATCH Update Store
Route: /store  
Method/s: PUT, PATCH   
Description: Change details of a store account, returns a JWT if email is changed  
Authentication required: Yes   
Additional account permission: Have a JWT associated with a Store    
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
(name, string)   
(street_number, int)   
(street_name, string)   
(suburb, int)   
(postcode, int)   
(email, string)   

example route URI:   
```
127.0.0.1:5000/store
```
example request body:   
```
{
    "name": "Valley of Shadow gaming",
    "street_number": 35,
    "street_name": "Shield St",
    "suburb": "Cairns",
    "postcode": 4870,
    "email": "valley@shadowgaming.com"
}
```
example request response:   
```
{
    "store": {
        "id": 1,
        "name": "Valley of Shadow gaming",
        "street_number": 35,
        "street_name": "Shield St",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "valley@shadowgaming.com"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAzMDYwNiwianRpIjoiNDRlZjdiNzgtNTY3NS00MWUyLTkxZjQtMTM3M2JmYWIxMWJiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6WzEsInNlcnZpY2VzQHBsYXltb3JlLmNvbSJdLCJuYmYiOjE2ODgwMzA2MDYsImV4cCI6MTY4ODA0MTQwNn0.eiTjDg44IQ1qzaAy7u9h1ocdnwjuXlbMxD6wWgvLzcw"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete User
Route: /user  
Method/s: DELETE   
Description: Allows a person to delete their own User account, returns empty json if successful  
Authentication required: Yes     
Additional account permission: Have a JWT associated with a User. A User with administrator privileges cannot delete their own account.    
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a

* Optional (key name, type):   
n/a

example route URI:   
```
127.0.0.1:5000/user
```
example request body:   
```
n/a
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete specific user 
Route: /users/\<int:user_id\>  
Method/s: DELETE   
Description: Delete a specific user based on their id number, returns empty json is successful  
Authentication required: Yes  
Additional account permission: Have a JWT associated with a User with administrator privileges. Administrator cannot delete other Administrators.      
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/users/2
```
example request body:   
```
n/a   
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete Store 
Route: /store  
Method/s: DELETE   
Description: Allows a business to delete their own Store account, returns empty json if successful   
Authentication required: Yes  
Additional account permission: Have a JWT associated with a Store   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/store
```
example request body:   
```
n/a
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete specific Store 
Route: /stores/\<int:store_id\>  
Method/s: DELETE   
Description: Delete a specific Store based on their id number, returns empty json is successful   
Authentication required: Yes     
Additional account permission: Have a JWT associated with a User with administrator privileges.    
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/stores/3
```
example request body:   
```
n/a
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Get Users 
Route: /users  
Method/s: GET   
Description: Search and return all Users accounts  
Authentication required: Yes 
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/users
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 2,
        "first_name": "Sally",
        "last_name": "McDonald",
        "email": "sally@yahoo.com"
    },
    {
        "id": 3,
        "first_name": "Greg",
        "last_name": "Layland",
        "email": "greggory@gmail.com"
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Get Stores 
Route: /stores  
Method/s: GET   
Description: Search and return all Store accounts  
Authentication required: Yes     
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/stores
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 2,
        "name": "Random Dice Ltd",
        "street_number": 11,
        "street_name": "Griffin st",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "bookings@randomdice.com"
    },
    {
        "id": 4,
        "name": "Have fun gaming",
        "street_number": 70,
        "street_name": "Ronald Dr",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "have@fungaming.com"
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
### Games routes   
   
#### GET Get Games 
Route: /games  
Method/s: GET   
Description: Search and return all games  
Authentication required: No  
Additional account permission: No  
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 2,
        "name": "Dominion",
        "year": 2008,
        "min_age": 11,
        "price_per_week": 13.49,
        "quantity": 3,
        "game_designers": [],
        "game_categories": [
            {
                "category": {
                    "id": 1,
                    "name": "Deck Building"
                }
            }
        ],
        "store": {
            "id": 2,
            "name": "Random Dice Ltd",
            "street_number": 11,
            "street_name": "Griffin st",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "bookings@randomdice.com"
        }
    },
    {
        "id": 4,
        "name": "Pandemic",
        "year": 2007,
        "min_age": 12,
        "price_per_week": 10.99,
        "quantity": 1,
        "game_designers": [
            {
                "designer": {
                    "id": 4,
                    "first_name": "Matt",
                    "last_name": "Leecock"
                }
            }
        ],
        "game_categories": [
            {
                "category": {
                    "id": 3,
                    "name": "Abstract"
                }
            }
        ],
        "store": {
            "id": 1,
            "name": "Valley of Shadow gaming",
            "street_number": 35,
            "street_name": "Shield St",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "services@playmore.com"
        }
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Get specific Game 
Route: /games/\<int:game_id\>  
Method/s: GET  
Description: Search and return a specific game by id  
Authentication required: No  
Additional account permission: No     
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/5
```
example request body:   
```
n/a   
```
example request response:   
```
{
    "id": 5,
    "name": "Carcassonne",
    "year": 2000,
    "min_age": 7,
    "price_per_week": 8.5,
    "quantity": 3,
    "game_designers": [
        {
            "designer": {
                "id": 5,
                "first_name": "Klaus-Jurgen",
                "last_name": "Wrede"
            }
        }
    ],
    "game_categories": [
        {
            "category": {
                "id": 4,
                "name": "Euro"
            }
        }
    ],
    "store": {
        "id": 2,
        "name": "Random Dice Ltd",
        "street_number": 11,
        "street_name": "Griffin st",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "bookings@randomdice.com"
    }
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Get owned Games 
Route: /games/owned  
Method/s: GET   
Description: Retrieve all games owned by a User  
Authentication required: Yes  
Additional account permission: Have a JWT associated with a User   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/owned
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 7,
        "name": "Blood Rage",
        "year": 2015,
        "min_age": 15,
        "price_per_week": 17.5,
        "quantity": 1,
        "game_designers": [
            {
                "designer": {
                    "id": 3,
                    "first_name": "Alan",
                    "last_name": "Moon"
                }
            },
            {
                "designer": {
                    "id": 1,
                    "first_name": "Bob",
                    "last_name": "Ross"
                }
            }
        ],
        "game_categories": [
            {
                "category": {
                    "id": 1,
                    "name": "Deck Building"
                }
            },
            {
                "category": {
                    "id": 4,
                    "name": "Euro"
                }
            }
        ],
        "store": {
            "id": 1,
            "name": "Valley of Shadow gaming",
            "street_number": 35,
            "street_name": "Shield St",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "services@playmore.com"
        },
        "owner": {
            "id": 1,
            "first_name": "John",
            "last_name": "Daniels",
            "email": "admin@bg.com"
        }
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Filter Games by range price 
Route: /games/minmaxprice  
Method/s: POST      
Description: Search and return Games based on minimum and maximum prices sent in request body  
Authentication required: No  
Additional account permission: No     
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(min_price, float)
(max_price, float)

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/minmaxprice
```
example request body:   
```
{
    "min_price": 12.50,
    "max_price": 15.0
}
```
example request response:   
```
[
    {
        "id": 2,
        "name": "Dominion",
        "year": 2008,
        "min_age": 11,
        "price_per_week": 13.49,
        "quantity": 3,
        "game_designers": [],
        "game_categories": [
            {
                "category": {
                    "id": 1,
                    "name": "Deck Building"
                }
            }
        ],
        "store": {
            "id": 2,
            "name": "Random Dice Ltd",
            "street_number": 11,
            "street_name": "Griffin st",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "bookings@randomdice.com"
        }
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Filter games by store id 
Route: /games/store/\<int:bgstore_id\>  
Method/s: GET      
Description: Search and return games based on store id  
Authentication required: No  
Additional account permission: No 
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/store/1
```
example request body:   
```
n/a
```
example request response:   
```
[
    {
        "id": 4,
        "name": "Pandemic",
        "year": 2007,
        "min_age": 12,
        "price_per_week": 10.99,
        "quantity": 1,
        "game_designers": [
            {
                "designer": {
                    "id": 4,
                    "first_name": "Matt",
                    "last_name": "Leecock"
                }
            }
        ],
        "game_categories": [
            {
                "category": {
                    "id": 3,
                    "name": "Abstract"
                }
            }
        ],
        "store": {
            "id": 1,
            "name": "Valley of Shadow gaming",
            "street_number": 35,
            "street_name": "Shield St",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "services@playmore.com"
        }
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Filter Games by designer
Route: /games/designer/\<string:designer_first_name\>/\<string:designer_last_name\>  
Method/s: GET   
Description: Search and return all games with the designer's name that was provided  
Authentication required: No  
Additional account permission: No     
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/designer/klaus-jurgen/wrede
```
example request body:   
```
n/a
```
example request response:   
```
{
    "id": 5,
    "first_name": "Klaus-Jurgen",
    "last_name": "Wrede",
    "game_designers": [
        {
            "id": 5,
            "game": {
                "id": 5,
                "name": "Carcassonne",
                "year": 2000,
                "min_age": 7,
                "price_per_week": 8.5,
                "quantity": 3,
                "game_categories": [
                    {
                        "category": {
                            "id": 4,
                            "name": "Euro"
                        }
                    }
                ],
                "store": {
                    "id": 2,
                    "name": "Random Dice Ltd",
                    "street_number": 11,
                    "street_name": "Griffin st",
                    "suburb": "Cairns",
                    "postcode": 4870,
                    "email": "bookings@randomdice.com"
                }
            }
        }
    ]
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Filter Games by Category 
Route: /games/category/\<string:category_name\>  
Method/s: GET      
Description: Search and return games based on the category name provided  
Authentication required: No  
Additional account permission: No  
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/category/euro
```
example request body:   
```
n/a
```
example request response:   
```
{
    "id": 4,
    "name": "Euro",
    "game_categories": [
        {
            "id": 7,
            "game": {
                "id": 5,
                "name": "Carcassonne",
                "year": 2000,
                "min_age": 7,
                "price_per_week": 8.5,
                "quantity": 3,
                "game_designers": [
                    {
                        "designer": {
                            "id": 5,
                            "first_name": "Klaus-Jurgen",
                            "last_name": "Wrede"
                        }
                    }
                ],
                "store": {
                    "id": 2,
                    "name": "Random Dice Ltd",
                    "street_number": 11,
                    "street_name": "Griffin st",
                    "suburb": "Cairns",
                    "postcode": 4870,
                    "email": "bookings@randomdice.com"
                }
            }
        }
    ]
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Filter Games by minimum age 
Route: /games/minage/\<int:minimum_age\>  
Method/s: GET  
Description: Search and return games base on minimum age provided  
Authentication required: No  
Additional account permission: No   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/minage/15
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 2,
        "name": "Dominion",
        "year": 2008,
        "min_age": 11,
        "price_per_week": 13.49,
        "quantity": 3,
        "game_designers": [],
        "game_categories": [
            {
                "category": {
                    "id": 1,
                    "name": "Deck Building"
                }
            }
        ],
        "store": {
            "id": 2,
            "name": "Random Dice Ltd",
            "street_number": 11,
            "street_name": "Griffin st",
            "suburb": "Cairns",
            "postcode": 4870,
            "email": "bookings@randomdice.com"
        }
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Create new Game for store 
Route: /games  
Method/s: POST  
Description: Add a new Game, can only be created by a Store account. Must specify which User owns game by id  
Authentication required: Yes  
Additional account permission: Have a JWT associated with a Store  
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(name, string)   
(year, int)   
(min_age, int)   
(price_per_week, float)   
(quantity, int)   
(owner_id, int)   
(categories, [string])   
(designers, [string], format of string = "first_name last_name")   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games
```
example request body:   
```
{
    "name": "Blue Rage",
    "year": 2015,
    "min_age": 15,
    "price_per_week": 17.50,
    "quantity": 1,
    "owner_id": 1,
    "categories": ["Deck Building", "Euro"],
    "designers": ["Alan Moon", "Matt Leecock"]
}
```
example request response:   
```
{
    "id": 9,
    "name": "Blue Rage",
    "year": 2015,
    "min_age": 15,
    "price_per_week": 17.5,
    "quantity": 1,
    "game_designers": [
        {
            "designer": {
                "id": 3,
                "first_name": "Alan",
                "last_name": "Moon"
            }
        },
        {
            "designer": {
                "id": 4,
                "first_name": "Matt",
                "last_name": "Leecock"
            }
        }
    ],
    "game_categories": [
        {
            "category": {
                "id": 1,
                "name": "Deck Building"
            }
        },
        {
            "category": {
                "id": 4,
                "name": "Euro"
            }
        }
    ],
    "store": {
        "id": 1,
        "name": "Valley of Shadow gaming",
        "street_number": 35,
        "street_name": "Shield St",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "services@playmore.com"
    },
    "owner": {
        "id": 1,
        "first_name": "John",
        "last_name": "Daniels",
        "email": "admin@bg.com"
    }
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### PUT/PATCH Update a game 
Route: /games/\<int:game_id\>    
Method/s: PUT, PATCH      
Description: Update a Game details that is owned by the accessing Store account   
Authentication required: Yes   
Additional account permission: Have a JWT associated with a Store     
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
(name, string)   
(year, int)   
(min_age, int)   
(price_per_week, float)   
(quantity, int)   
(owner_id, int)   
(categories, [string])   
(designers, [string], format of string = "first_name last_name")   

example route URI:   
```
127.0.0.1:5000/games/1
```
example request body:   
```
{
    "name": "Blood Moon",
    "year": 2015,
    "min_age": 15,
    "price_per_week": 17.50,
    "quantity": 1,
    "categories": ["Euro", "Abstract"],
    "designers": ["Alan Moon", "Matt Leecock"]
} 
```
example request response:   
```
{
    "id": 1,
    "name": "Blood Moon",
    "year": 2015,
    "min_age": 15,
    "price_per_week": 17.5,
    "quantity": 1,
    "game_designers": [
        {
            "designer": {
                "id": 3,
                "first_name": "Alan",
                "last_name": "Moon"
            }
        },
        {
            "designer": {
                "id": 4,
                "first_name": "Matt",
                "last_name": "Leecock"
            }
        }
    ],
    "game_categories": [
        {
            "category": {
                "id": 4,
                "name": "Euro"
            }
        },
        {
            "category": {
                "id": 3,
                "name": "Abstract"
            }
        }
    ],
    "store": {
        "id": 1,
        "name": "Valley of Shadow gaming",
        "street_number": 35,
        "street_name": "Shield St",
        "suburb": "Cairns",
        "postcode": 4870,
        "email": "services@playmore.com"
    },
    "owner": {
        "id": 2,
        "first_name": "Sally",
        "last_name": "McDonald",
        "email": "sally@yahoo.com"
    }
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete game  
Route: /games/\<int:game_id\>  
Method/s: DELETE   
Description: Delete a game. If a Store is accessing then they can delete their own games, if Administrator is accessing they can delete any game. If successful, it returns an empty json  
Authentication required: Yes 
Additional account permission: Have a JWT associated with a Store or a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/1
```
example request body:   
```
n/a   
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Create Category 
Route: /games/category  
Method/s: POST   
Description: Add a board game Category  
Authentication required: Yes    
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(name, string)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/category
```
example request body:   
```
{
    "name": "traditional"
}
```
example request response:   
```
{
    "id": 7,
    "name": "Traditional"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Create Designer 
Route: /games/designer  
Method/s: POST   
Description: Add a board game Designer  
Authentication required: Yes  
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(first_name, string)   
(last_name, string)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/designer
```
example request body:   
```
{
    "first_name": "Gordan",
    "last_name": "Freeman"
}
```
example request response:   
```
{
    "id": 7,
    "first_name": "Gordan",
    "last_name": "Freeman"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### PUT/PATCH Update Category
Route: /games/category/\<int:category_id\>   
Method/s: PUT, PATCH     
Description: Change Category details based on the Category id 
Authentication required: Yes  
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(name, string)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/category/1
```
example request body:   
```
{
    "name": "adventure"
}
```
example request response:   
```
{
    "id": 1,
    "name": "Adventure"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### PUT/PATCH Update Designer
Route: /games/designer/\<int:designer_id\>  
Method/s: PUT, PATCH   
Description: Change a Designer details based on the designer id  
Authentication required: Yes    
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
(first_name, string)   
(last_name, string)    

example route URI:   
```
n/a   
```
example request body:   
```
{
    "first_name": "bob",
    "last_name": "ross"
}
```
example request response:   
```
{
    "id": 1,
    "first_name": "Bob",
    "last_name": "Ross"
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete Category 
Route: /games/category/\<int:category_id\>  
Method/s: DELETE   
Description: Remove a Category based on supplied category id, returns empty json if successful  
Authentication required: Yes   
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/category/2
```
example request body:   
```
n/a   
```
example request response:   
```
{}   
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### DELETE Delete Designer
Route: /games/designer/\<int:designer_id\>  
Method/s: DELETE   
Description: Remove a Designer based on supplied designer id, returns empty json if successful  
Authentication required: Yes 
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/games/designer/1
```
example request body:   
```
n/a   
```
example request response:   
```
{}   
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
### Rentals routes

#### GET Get Game Rentals 
Route: /rentals  
Method/s: GET  
Description: Search and return all Game Rentals  
Authentication required: Yes   
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/rentals
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 4,
        "date": "2023-06-25",
        "rentee_id": 2,
        "rentee_first_name": "Sally",
        "rentee_last_name": "McDonald",
        "rentee_email": "sally@yahoo.com",
        "game_id": 2,
        "game_name": "Dominion",
        "price_per_week": 13.49,
        "quantity": 2,
        "store_name": "Random Dice Ltd",
        "store_street_number": 11,
        "store_street_name": "Griffin st",
        "store_suburb": "Cairns",
        "store_postcode": 4870
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### GET Get Game Rentals from Store account 
Route: /rentals/store  
Method/s: GET   
Description: Search and return Game Rentals for Store that performed request  
Authentication required: Yes 
Additional account permission: Have a JWT associated with a Store 
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/rentals/store
```
example request body:   
```
n/a   
```
example request response:   
```
[
    {
        "id": 10,
        "name": "Blood Rage",
        "game_rent_details": [
            {
                "id": 6,
                "date": "2023-05-25",
                "rentee_id": 9,
                "rentee_first_name": "Greg",
                "rentee_last_name": "Layland",
                "rentee_email": "greggory@gmail.com",
                "price_per_week": 17.5,
                "quantity": 1
            }
        ]
    },
    {
        "id": 13,
        "name": "Pandemic",
        "game_rent_details": []
    }
]
```
[return to top](#boardgame-rental-api-endpoints-documentation)   
#### POST Create Rental
Route: /rentals/new   
Method/s: POST   
Description: Create a Game Rental based on which Store performed the request   
Authentication required: Yes    
Additional account permission: Have a JWT associated with a Store      
<u>Query Parameters</u>    
* Mandatory (key name, type):    
(game_id, int)   
(rentee_id, int)   
(quantity, int)   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/rentals/new
```
example request body:   
```
{
    "game_id": 1,
    "rentee_id": 1,
    "quantity": 1
}
```
example request response:   
```
{
    "id": 5,
    "date": "2023-06-29",
    "rentee_id": 1,
    "rentee_first_name": "John",
    "rentee_last_name": "Smith",
    "rentee_email": "admin@bg.com",
    "game_id": 1,
    "game_name": "Blood Rage",
    "price_per_week": 17.5,
    "quantity": 1,
    "store_name": "Play more games Inc",
    "store_street_number": 25,
    "store_street_name": "Lake st",
    "store_suburb": "Cairns",
    "store_postcode": 4870
}
```
[return to top](#boardgame-rental-api-endpoints-documentation)
#### DELETE Delete Game Rental

Route: /rentals/\<int:rental_id\>  
Method/s: DELETE   
Description: Remove a Game Rental record, return an empty json is successful  
Authentication required: Yes    
Additional account permission: Have a JWT associated with a User with administrator privileges   
<u>Query Parameters</u>    
* Mandatory (key name, type):    
n/a   

* Optional (key name, type):   
n/a   

example route URI:   
```
127.0.0.1:5000/rentals/1
```
example request body:   
```
n/a   
```
example request response:   
```
{}
```
[return to top](#boardgame-rental-api-endpoints-documentation)   