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

class HOTEL_FARE(models.Model):
    type_choice = (
        ('Two Star','TWO STAR'),
        ('Three Star','THREE STAR'),
        ('Four Star','FOUR STAR'),
        ('Five Star','FIVE STAR'),
        ('Six Star','SIX STAR'),
        ('Seven Star','SEVEN STAR'),
    )
    hotel_type = models.CharField(max_length=100, choices=type_choice)
    hotel_fare = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.hotel_type + ': Rs' + str(self.hotel_fare)
    class Meta:
        verbose_name="HOTEL_FARE"


class HOTEL(models.Model):
    city_choice = (
        ('ISLAMABAD', 'ISLAMABAD'),
        ('MURREE', 'MURREE'),
        ('NATHIA GALI', 'NATHIA GALI'),
        ('NARAN KAGHAN', 'NARAN KAGHAN'),
        ('KASHMIR', 'KASHMIR'),
        ('SAWAT', 'SAWAT'),
    )
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=city_choice)
    address = models.CharField(max_length=100)
    image = models.ImageField(default='default_hotel.jpeg', upload_to='hotel_pics')
    charges = models.ForeignKey(HOTEL_FARE,null=True,on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={'pk': self.id})


