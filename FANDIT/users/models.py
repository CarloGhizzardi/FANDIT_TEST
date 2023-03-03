from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email= models.EmailField(unique= True)
    username= models.CharField(max_length=50, unique= True)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= []

    


