from django.db import models

# Create your models here.


class Person(models.Model):
    username =models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=200)

    