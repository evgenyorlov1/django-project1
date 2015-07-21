from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=50)
    nikname = models.CharField(max_length=50)
    email = models.EmailField(default='abc@abc.net')
