from .trip import Trip
from ..models import TRIP
from django.core.exceptions import ObjectDoesNotExist

class TripList:
    def __init__(self):
        pass

    def add_custom_trip(self,source,destination,start_date,end_date):
        source = source
        destination = destination
        start_date = start_date
        end_date = end_date
        new_trip = Trip(source,destination,start_date,end_date,True)
        new_trip.save()
        return new_trip
    
    def get_trip(self,id):
        try:
            trip = TRIP.objects.get(id = id)
            return trip
        except ObjectDoesNotExist:
            raise Exception(f'Trip: {id} does not exist!')
