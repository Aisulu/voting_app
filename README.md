## ABOUT

This is a web interface for manual annotation of tweets for the emotion detection task writen during my master thesis.

## Emotions folder:

[Static](emotions/static) folder contains style.css file with all the necessary style information.

[Templates](emotions/templates) folder contains two subfolders:
- [emotions](emotions/templates/emotions) (consisting of dashboard and voting page interfaces)
- [registration](emotions/templates/registration) (interface for user authentication)

[Models.py](emotions/models.py) describes two classes used: Tweet and Vote. Third class User is default django class.
<img src="data%20model.png" width="500" />

[Urls.py](emotions/urls.py) is responsible for routing through the app.

[Views.py](emotions/views.py) contains all the logic behind and a communication with the database.

## db.sqlite3

Database file containing all the initial Tweets + results of labelling.

## Access for labeling

- user: test
- pass: Test1234

## Access to database**

- user: rahaisulu
- pass: admin_path
