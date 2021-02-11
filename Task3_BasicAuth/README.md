# Authentication Flows

This is the example project to run the authentication flows 
using Python Django.

Its the example demonstration of 
- Views
- Class based views.
- Forms
- Model Forms


### Technologies
Python, Django

### Run project

Clone the whole repository and go to following directory
../python-tasks/Task3_BasicAuth

Run following command to make virtual enviroment

`virtualenv -p python3 venv`

**Note:** This project has been tested over python3.6.5, make sure python3 is referring to same version

Now activate the environment and install the requirements using following command
`pip install -r requirements.txt`

Go to src directory and run following command

`./manage.py runserver` 

Home of project

http://127.0.0.1:8000/

**Admin portal**
You need a user and password to access admin portal http://localhost:8000/admin/

You can create a user using the following command:

./manage.py createsuperuser

or you can use already created one

email: admin@g.com
password: arbisoft
