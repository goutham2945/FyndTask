# IMBD task

Create a RESTful API for movies (something similar to IMDB).
For this we would like you to use:
- MySql or SQLlite or MongoDB to store data
- Any of the following Python Framework for implementing the APIs.
    - Flask
    - Sanic (preferred)
    - FastAPI
- There need to be 2 levels of access:
  - admin = who can add, remove or edit movies.
  - users = who can just view the movies.
- There should also be a decent implementation to search for movies.
- Make sure to add test cases
- Document your code well so that we can test the API with ease.
- For your convenience we have attached some data that you can use to populate
your database
- Try and deploy this on Heroku or AWS or any cloud.

### Steps to check the functionality:
- Method1 - UI
- Method2 - Postman

Method1: 
   - Step1: Try to login in browser with the url:
https://fyndassignment.herokuapp.com/admin/login/?next=/admin/ and use below credentials for testing the app as admin
```
Username: fynd_user
password: Fynd1234
```
- step2: https://fyndassignment.herokuapp.com/search_movie
![](https://i.imgur.com/h3lyLKJ.png)

Method2:
    - Import the postman collection [here](https://www.getpostman.com/collections/8160f6db31488f59c74c) and pass required credentials in basic auth
    - ![](https://i.imgur.com/IPAQpJJ.png)
    - ![](https://i.imgur.com/Pl1ordp.png)
    
    
## Stack details
```bash
Framework : python-Django
version : Django-3.2

Database:
Db : sqlite (default)

Backend:
Language : python
verison : python3

Hostname:
host : localhost (default)
```

## Installation steps
```bash
mkdir new_project
cd new_project
python3 -m venv env
source env/bin/activate
git clone https://github.com/goutham2945/FyndTask.git
cd FyndTask

pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate_json_to_db # command line to sync sample json to db
python3 manage.py runserver

Note: when you want to run this application on server, please add domain name/ip address in ALLOWEDHOSTS in settings.py
and add DEBUG=True in settings.py when you run in local
```

To do sanity check when tried from local machine click [here](http://localhost:8000/search_movie) which will return all the available movies in db
![](https://i.imgur.com/T9mptuT.png)
