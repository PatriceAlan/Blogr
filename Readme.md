# Blogr

## Setup virtual environment

python3 -m venv blenv

## Activate virtual environment

On linux: source blenv/bin/activate

## Django installation

pip install django

## Create Django project

django-admin startproject blog

## Change directory and create the blog app website

cd blog

python manage.py startapp website

## Install the python-dotenv app to use .env in the project

pip install python-dotenv

## Create a .env file to store your credentials

SECRET_KEY = 

## Modify settings.py to use credentials from .env

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

## Add app website in installed apps of settings.py

INSTALLED_APPS = [

    'website',
]

## Do the migrations in the app while in the blog folder

python manage.py migrate

## Run the application while in the blog folder

python manage.py runserver

## Create a superuser, give name, password(useful to connect to the admin control panel page)

python manage.py createsuperuser

## Modify urls.py in blog folder to include urls.py of website folder

path('', include('website.urls')),

## Create a urls.py in website folder and add urls of views

 urlpatterns = [
     path('', views.name_of_the_view, name='name_of_the_view'),
 ]

## Create the templates folder in the website folder

## Create html pages in the templates folder

create home.html

## Create new views in views.py of the website folder 

def home