from django.contrib import admin
from .models import BOOKING, EMPLOYEE,CAR, FARE,TICKET,TRIP,HOTEL, HOTEL_FARE

# Register your models here.
admin.site.register(EMPLOYEE)
admin.site.register(CAR)
admin.site.register(TRIP)
admin.site.register(TICKET)
admin.site.register(BOOKING)
admin.site.register(FARE)
admin.site.register(HOTEL)
admin.site.register(HOTEL_FARE)
