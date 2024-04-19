from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    followers = models.ManyToManyField('accounts.User', related_name='followings')
    jjim_products = models.ManyToManyField( 'products.Product', related_name='jjim_users')