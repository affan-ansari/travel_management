from django.db import models
from ..models import BOOKING
from django.utils import timezone
class Booking:
    def __new__(cls,trip,allocated_car,allocated_hotel,customer):
        now = timezone.localtime(timezone.now())
        now = now.replace(hour=0,minute=0,second=0,microsecond=0)
        new_booking = BOOKING(
            trip = trip,
            allocated_car = allocated_car,
            allocated_hotel = allocated_hotel,
            customer = customer,
            booking_date = now
        )
        return new_booking
