from .trip import Trip
from .fixed_trip import FixedTrip
from ..models import TRIP,FIXED_TRIP
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

class TripList:
    def __init__(self):
        pass

    def add_custom_trip(self,source,destination,start_date,end_date):
        now = timezone.localtime(timezone.now())
        now = now.replace(hour=0,minute=0,second=0,microsecond=0)
        if start_date < now:
            raise Exception("Invalid dates! Start Date must be greater than today's date")
        if start_date >= end_date:
            raise Exception("Invalid dates! Start Date must be less than End Date!")
        source = source
        destination = destination
        start_date = start_date
        end_date = end_date
        new_trip = Trip(source,destination,start_date,end_date)
        new_trip.save()
        return new_trip
    
    def add_fixed_trip(self,source,destination,start_date,end_date,allocated_hotel,available_seats,price):
        now = timezone.localtime(timezone.now())
        now = now.replace(hour=0,minute=0,second=0,microsecond=0)
        if start_date < now:
            raise Exception("Invalid dates! Start Date must be greater than today's date")
        if start_date >= end_date:
            raise Exception("Invalid dates! Start Date must be less than End Date!")
        source = source
        destination = destination
        start_date = start_date
        end_date = end_date
        allocated_hotel = allocated_hotel
        available_seats = available_seats
        price = price
        new_trip = FixedTrip(source,destination,start_date,end_date,allocated_hotel,available_seats,price)
        new_trip.save()
        return new_trip

    def get_trip(self,id):
        try:
            trip = TRIP.objects.get(id = id)
            return trip
        except ObjectDoesNotExist:
            raise Exception(f'Trip: {id} does not exist!')
