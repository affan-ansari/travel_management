from .hotel import Hotel
from ..models import HOTEL
from django.core.exceptions import ObjectDoesNotExist

class HotelList:
    def __init__(self):
        pass

    def add_hotel(self,name,city,address,image,charges):
        name = name.title()
        new_hotel = Hotel(name,city,address,image,charges) # Returns HOTEL model class object
        new_hotel.save()
    
    def get_hotels(self,user):
        hotels = HOTEL.objects.all()
        return hotels
    
    def get_hotel(self,id):
        try:
            searched_hotel = HOTEL.objects.get(id=id)
            return searched_hotel
        except ObjectDoesNotExist:
            raise Exception(f'{id} does not exist!')