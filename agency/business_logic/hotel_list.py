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
    
    def delete_hotel(self,id):
        try:
            searched_hotel = self.get_hotel(id)
            # searched_hotel.delete()
            if searched_hotel.available == False:
                return False
            else:
                searched_hotel.available = False
                searched_hotel.save()
                return True
        except ObjectDoesNotExist:
            return False
    
    def get_hotels(self):
        hotels = HOTEL.objects.filter(available=True)
        return hotels
    
    def get_hotel(self,id):
        try:
            searched_hotel = HOTEL.objects.get(id=id)
            if searched_hotel.available == False:
                raise Exception(f'{id} was deleted!')
            else:
                return searched_hotel
        except ObjectDoesNotExist:
            raise Exception(f'{id} does not exist!')