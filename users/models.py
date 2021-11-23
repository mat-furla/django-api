import uuid
from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True, blank=False,
                              max_length=254)
    password = models.CharField(blank=False, max_length=254)
    first_name = models.CharField(blank=False, max_length=254)
    last_name = models.CharField(blank=False, max_length=254)
    birth_date = models.DateField(blank=False)
