# key - id (primary automatic)
# first_name (string), last_name (string), phone (string)
# email (email), created_date(data), description (text),
# category (foreing key), show(boolean), owner (foreing key)
# picture.
from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to= 'pictures/%Y/%M')
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True,)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
