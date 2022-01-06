from django.contrib.auth.models import AbstractUser
from django.db import models
import json

class User(AbstractUser):
    pass

class UserNotSignIn(models.Model):
    cookie = models.AutoField(primary_key=True)

class Url(models.Model):
    url = models.CharField(max_length=254, null=False, blank=False)
    shorten = models.CharField(max_length=254, unique=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    visits = models.IntegerField(default=0)
    userNotSignIn = models.ForeignKey(UserNotSignIn, on_delete=models.CASCADE, null=True, blank=True, default=None)
    