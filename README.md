# Django

## Dependencies

```bash
>> python3 -m venv .venv
>> source .venv/bin/activate
>> pip install -r requirements.txt
```

## Project creation
```bash
>> django-admin startproject django_api
```

## App creation
```bash
>> python manage.py startapp users
>> python manage.py startapp export
```

## Migrations
```bash
>> python manage.py makemigrations
>> python manage.py migrate
```

## Start server
```bash
>> python manage.py runserver
```

## Routes
### Admin
```bash
http://localhost:8000/admin
```

### Users - GET, POST
```bash
#GET - Return all users
http://localhost:8000/users/

#POST - Create new user
http://localhost:8000/users/
---
{
  "email": "test@teste.com",
  "password": "",
  "first_name": "first_name",
  "last_name": "last_name",
  "birth_date": "2021-11-25"
}
---

#GET - Return user by id
http://localhost:8000/users/<user_id>
```

### Export - GET
```bash
#GET - Export user database to xlsl
http://localhost:8000/export/
```