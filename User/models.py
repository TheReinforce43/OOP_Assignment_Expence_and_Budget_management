from django.contrib.auth.models import AbstractUser
from django.db import models

from User.custom_manager import UserManager


class User(AbstractUser):
    """
    Custom User extending AbstractUser
    """

    username = None  
    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=20,db_index=True,blank=True,null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] 
    objects = UserManager()  

    def __str__(self):
        return self.email
