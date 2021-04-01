# ebay_like_app

## Video:-[Watch it, working](https://youtu.be/ueoYW6tCAE0)

## Installation
In order to run this project, you must have python3 installed on your system
```bash


# clone this repo with git
$ git clone https://github.com/princ3raj/ebay_like_app.git
$ cd ebay_like_app
$ activate virtual environment:- source env/bin/activate
$ pip install -r requirements.txt

# create database tables:-
$ python manage.py migrate

# finally run the application
$ python manage.py runserver
```

## USAGE
- Create account or login
- Create Listing and set a starting bid
- Users can bid on listed products
- When the owner of the listed products closes the auction , one who has bid highest price will receive a winning message
- users can comment on listed product
- add product to wishlist and remove it as well

