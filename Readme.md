# Coda Bene Entry Test Backend
Author : Martin Chevereau

## Backend
The Django framework is imposed for the project\
It is composed of a single app called Inventory

### Views
- **Add product** Add an existing product to a shelf and specify its expiry date
- **Set expiry date** Update the expiry date for a product already in shelf
- **Display Expiries** Display product in shelves with their expiry dates
- **Add new Product** *optional* Create a new product with its GTIN
### DataBase
The choice of a relational database is imposed so I decided to add more information to justify this choice.

![DB](./images/DB.png)

Each product has its own GTIN and belongs to a specific shelf (yogurts, cheeses...)\
Each table is represented through a Django **Model**\
The **PostgreSQL** DB runs online through railway


## Expected Features

### New Expiry for a GTIN
Endpoint to add/update in Expiries

### Display
Endpoint list all expiries 
Display with css

### User Interface
use React + CSS for interaction


## Endpoints
