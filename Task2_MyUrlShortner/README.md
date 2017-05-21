# My Url Shortner App

This is a Django assignment in which i have created a URL shortener similar
to http://bit.ly but with a different URL encoding scheme.

Complete assignment details are here:
https://github.com/farhan/python-tasks/wiki/Django-URL-Shortening-Project

## Install Required Packages

All required packages to run this project are mentioned in 'requirements.txt' file.
To install them use the following command:

pip install -r requirements.txt


## Running the Application

Database (db.sqlite3) is already available in project, you don't need to create
a new one.

Just run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>


## Admin portal

You need a user and password to access admin portal.
http://localhost:8000/admin/

you can create a user using the following command:

    ./manage.py createsuperuser

or you can use already created
user: admin
password: arbisoft
