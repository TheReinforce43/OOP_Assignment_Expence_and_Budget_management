from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User extending AbstractUser
    """

    username = None  # remove username field
    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20,db_index=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email
