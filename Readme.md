# Coda Bene Entry Test Backend
Author : Martin Chevereau

## Backend
The Django framework is imposed for the project\
It is composed of a single app called Inventory

### Views
- **Add product** Add or update an expiry date to an existing product
- **Display Expiries** Display products in a specific shelf with their expiry dates.
### DataBase
The choice of a relational database is imposed so I decided to add more information to justify this choice.

![DB](./images/DB.png)

Each product has its own GTIN and belongs to a specific shelf (yogurts, cheeses...)\
Each table is represented through a Django **Model**\
The **PostgreSQL** DB runs online through railway

### Forms
In order to listen to user's commands I used the **Form** class of Django. This is used in two cases:

- Filter shelf to display product
- Ask the user for expiry date of a product
## Frontend
### Templates
Each view matched to a specific template, an html file displaying data from queries and forms
## Areas of improvement
### Security 
Since I had to make the git repo public, anyone can access the database because of its infos present in the code...\
However these data are not crucial to protect\
I found out about tools like **Git secret** but this would have taken too much time to implement or I could have just give the DB info to the user but this is less practical
### Styling
Unfortunately I did not have time to implement css into the project
### Testsuite
Adding a testsuite via *Postman* or another tool would have been a good inclusion. However since we are not directly building an API this is harder to implement 
## Opinion about the test 
Event though I had to work on schools project at the same time, I enjoyed doing this project.
This was the opportunity to learn more about *Django* and do a first project.
However I was surprised that I had to work on the design and frontend for a backend test. Struggling with html took way too much time.