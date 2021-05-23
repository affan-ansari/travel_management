from django.db import models
from ..models import BOOKING
class Booking:
    def __new__(cls,trip,allocated_car,allocated_hotel,customer):
        new_booking = BOOKING(
            trip = trip,
            allocated_car = allocated_car,
            allocated_hotel = allocated_hotel,
            customer = customer
        )
        return new_booking
