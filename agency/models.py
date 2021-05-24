from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import PositiveBigIntegerField
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

class TRIP(models.Model):
    DEST_CITIES = (
        ('MURREE', 'MURREE'),
        ('NATHIA GALI', 'NATHIA GALI'),
        ('NARAN KAGHAN', 'NARAN KAGHAN'),
        ('KASHMIR', 'KASHMIR'),
        ('SAWAT', 'SAWAT'),
    )
    SOURCE_CITIES = (
        ('ISLAMABAD', 'ISLAMABAD'),
        ('RAWALPINDI', 'RAWALPINDI'),
    )
    source = models.CharField(max_length=100, choices=SOURCE_CITIES)
    destination = models.CharField(max_length=100, choices=DEST_CITIES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return 'Trip ' + str(self.id) + ' :' + self.source + ' - ' + self.destination


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
        return self.hotel_type + ': Rs ' + str(self.hotel_fare)
    class Meta:
        verbose_name="Hotel Fare"


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

    def __str__(self):
        return f'{self.name} [{self.city}]'

class FIXED_TRIP(models.Model):
    DEST_CITIES = (
        ('MURREE', 'MURREE'),
        ('NATHIA GALI', 'NATHIA GALI'),
        ('NARAN KAGHAN', 'NARAN KAGHAN'),
        ('KASHMIR', 'KASHMIR'),
        ('SAWAT', 'SAWAT'),
    )
    SOURCE_CITIES = (
        ('ISLAMABAD', 'ISLAMABAD'),
        ('RAWALPINDI', 'RAWALPINDI'),
    )
    SEAT_CHOICES = (
        (25, 25),
        (50, 50),
        (75, 75),
        (100, 100)
    )
    source = models.CharField(max_length=100, choices=SOURCE_CITIES)
    destination = models.CharField(max_length=100, choices=DEST_CITIES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    allocated_hotel = models.ForeignKey(HOTEL,null=True,on_delete=models.PROTECT)
    available_seats = models.PositiveIntegerField(choices=SEAT_CHOICES)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return 'Trip ' + str(self.id) + ' :' + self.source + ' - ' + self.destination
    
    class Meta:
        verbose_name="Fixed Trip"

class FARE(models.Model):
    TYPE_CHOICES = (
        ('Economy','ECONOMY'),
        ('Business','BUSINESS'),
        ('Luxury','LUXURY'),
    )
    car_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    car_fare = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.car_type + ': Rs' + str(self.car_fare) 

class CAR(models.Model):
    reg_no = models.CharField(max_length=25,primary_key=True, default="")
    make = models.CharField(max_length=100)
    model = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    image = models.ImageField(default='default_car.png', upload_to='car_pics')
    fare = models.ForeignKey(FARE,null=True,on_delete=models.PROTECT)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.reg_no) + ': ' + self.make + ' ' + str(self.model)

class BOOKING(models.Model):
    trip = models.OneToOneField(TRIP,on_delete=models.PROTECT)
    allocated_car = models.ForeignKey(CAR,null=True,on_delete=models.PROTECT)
    allocated_hotel = models.ForeignKey(HOTEL,null=True,on_delete=models.PROTECT)
    customer = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ': ' + self.trip.source + '-' + self.trip.destination

class FIXED_BOOKING(models.Model):
    trip = models.OneToOneField(TRIP,on_delete=models.PROTECT)
    customer = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ': ' + self.trip.source + '-' + self.trip.destination

class TICKET(models.Model):
    booking = models.ForeignKey(BOOKING,null=True,on_delete=models.PROTECT)
    seat_no = models.PositiveIntegerField(default=0)
