from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    aadhar = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField(null=True, blank=True)
    mobile = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.email
