# Project presentation

## How to run the app locally
1. create a virtual environment : `python3 -m venv venv`
2. activate it : `source venv/bin/activate`
3. install dependencies: `pip install -r requirements.txt`
4. run the app : `python CodaBeneProject/manage.py runserver`
5. now connect to `localhost:8000` to use the app

## Features
### Display products expiry
On the main page you can see all products currently in the store sorted by expiry date in ascending order

It is also possible to select products from a specific shelf

### Add a new expiry date
If you click on the according link you will be taken to a new page

You can select a specific product/GTIN and update its expiry date