from ..models import HOTEL
class Hotel:
    def __new__(cls,name,city,address,image,charges):
        new_hotel= HOTEL(
            name = name,
            city = city,
            address = address,
            image = image,
            charges = charges
        )
        return new_hotel