# key - id (primary automatic)
# first_name (string), last_name (string), phone (string)
# email (email), created_date(data), description (text),
# category (foreing key), show(boolean), owner (foreing key)
# picture.
from django.db import models
from django.utils import timezone

class Contact(models.model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # phone = models.CharField(max_length=50)
    # email = models.EmailField(max_length=254)
    # created_date = models.DateTimeField(defaut=timezone)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
