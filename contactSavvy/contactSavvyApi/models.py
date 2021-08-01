from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Contact(models.Model):
    name = models.CharField(max_length=60, default='John')
    surname = models.CharField(max_length=60, default='Doe')
    image = models.ImageField(default='default.png', blank=True)
    mobile_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=60)
    res_address = models.CharField(max_length=100)


