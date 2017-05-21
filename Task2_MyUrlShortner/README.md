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

Before running the application we need to create the needed DB tables:

    ./manage.py migrate

Now you can run the development web server:

    ./manage.py runserver

To access the applications go to the URL <http://localhost:8000/>


## Admin portal

http://localhost:8000/admin/
You need a user and password to access it.
you can create a user using the following command:

    ./manage.py createsuperuser

or you can use already created
user: admin
password: arbisoft