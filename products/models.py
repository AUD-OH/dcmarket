from django.db import models
from django.contrib.auth.models import AbstractUser

# Create vour models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.PositiveIntegerField()
    author = models.ForeignKey('accounts.User', on_delete = models.CASCADE)

