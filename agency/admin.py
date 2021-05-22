from django.contrib import admin
from .models import EMPLOYEE,HOTEL, HOTEL_FARE

# Register your models here.
admin.site.register(EMPLOYEE)
admin.site.register(HOTEL)
admin.site.register(HOTEL_FARE)