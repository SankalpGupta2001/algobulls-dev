steps to run the code : 

1) python -m venv core   (to setup the virtual env file core)
2) pip install django
3) cd ToDo
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver

Now project will be run in 8000, and we can test through postman

For Unit testing and integration testing, we will do only one operation

python manage.py test home

it will test the cases
