python3 -m venv .venv
source .venv/bin/activate.fish

pip install djangorestframework autopep8 pylint isort

django-admin startproject django_api
cd django_api/
python3 manage.py startapp users

In settings.py
add 'rest_framework', 'users'

python3 manage.py migrate # Initialize database

python3 manage.py runserver # Run server

python3 manage.py makemigrations # after model creation
python3 manage.py migrate