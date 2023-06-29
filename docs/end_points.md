## Boardgame Rental API Endpoints documentation
[Return to main page](../README.md)

[Authentication routes](#authentication-routes)     
[Games routes](#Games-routes)   
[Rentals routes](#Rentals-routes)   
   
#### Authentication routes   
##### POST Register User
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

example request body:   
```
{
    "first_name": "Franny",
    "last_name": "Rego",
    "email": "franny@gmail.com",
    "password": "12345678"
}
```
example response response:
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
example response response:
```
{
    "store": {
        "name": "Have fun gaming",
        "email": "have@fungaming.com"
    },
    "token": "eyJhcGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4ODAyODEwNywianRpIjoiZDlmYTg4NGQtMzAzMC00YzYzLTgyMmMtZjJiNTMxODa5ZjkxIiwidHlwZSI6ImFJY2VzcyIsInN1YiI6WzQsImhhdmVAZnVuZ2FtaW5nLmNvbSJdLCJuYmYiOjE2ODgwMjgxMDcsImv4cCI6MTY4ODAzODkwN30.kdutfMBYAP4nJCm10cTAA_8wBQZ7PUNhqRQnsTwvfdU"
}
```
