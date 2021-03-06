from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.email

    USERNAME_FIELD = 'username'


