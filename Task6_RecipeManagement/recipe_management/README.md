# Recipe Management App
This is an assignment based project whose details are given below

# Assignment Project
Create a REST based backend for a recipe management app using Django 2 and Python 3. User stories for the app are as follows:
* New members should be able to register to the app.
* Members should be able to login to the app.
* Members should be able to change their passwords.
* Members should be able to add a new recipe. (Recipe should contain title, brief description, stepwise directions, and ingredients)
* Members should be able to view all the recipes they have created.
* Members should be able to follow other members.
* Members should be able to view recipes of other members they are following.
* Members should be able to edit their profile.
* Members should be able to update or remove their recipes.


### Technologies
Python, Django, DRF, (Vagrant setup)

### Run project

Clone the whole repository and go to following directory

`../python-tasks/Task6_RecipeManagement/recipe_management`

Run following command to make virtual enviroment

`virtualenv -p python3 venv`

**Note:** This project has been tested over python3.6.5, make sure python3 is referring to same version

Now activate the environment and install the requirements using following command

`pip install -r requirements.txt`

Go to src directory and run following command

`./manage.py runserver` 

Home of project

http://127.0.0.1:8000/

#### Super user:
farhan/f@g.com/edx12345
#### Other profiles:
adnan/adnan, usman/usman
#### Followers
Usman is following Adnan and Farhan
Adnan is following Farhan

#### Following way is Archived
```
# How to run the Project
Checkout the project.
Open the terminal and set path of project root.
Run the following commands in sequence

vagrant up
// once the virtual box is all set, set the following command
vagrant ssh

cd /vagrant
mkvirtualenv recipe_management
workon recipe_management

pip install django==1.11
pip install djangorestframework==3.6.2

mkdir src
cd src

django-admin.py startproject recipe_management_project

cd recipe_management_project/
python manage.py startapp recipe_management_api

python manage.py migrate
python manage.py makemigrations

python manage.py runserver 0.0.0.0:8080
http://0.0.0.0:1234/  (Hit this url in browser)
```
