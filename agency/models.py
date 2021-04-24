from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse
from PIL import Image
# from .business_logic.car import Car
from users.models import User

class EMPLOYEE(models.Model):
    CNIC = models.CharField(max_length=15, primary_key=True, default="")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    available=models.BooleanField(default=True)
    #hourly_rate 
    def __str__(self):
        return self.first_name + ' ' + self.last_name