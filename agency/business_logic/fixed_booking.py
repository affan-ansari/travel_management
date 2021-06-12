from django.db import models
from ..models import FIXED_BOOKING
from django.utils import timezone
class FixedBooking:
    def __new__(cls,trip,customer):
        now = timezone.localtime(timezone.now())
        now = now.replace(hour=0,minute=0,second=0,microsecond=0)
        new_booking = FIXED_BOOKING(
            trip = trip,
            customer = customer,
            booking_date = now
        )
        return new_booking
