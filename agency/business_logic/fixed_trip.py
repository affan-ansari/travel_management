from ..models import FIXED_TRIP
class FixedTrip:
    def __new__(cls, source,destination,start_date,end_date,allocated_hotel,available_seats,price):
        new_trip = FIXED_TRIP(
            source = source,
            destination = destination,
            start_date = start_date,
            end_date = end_date,
            allocated_hotel = allocated_hotel,
            available_seats = available_seats,
            price = price
        )
        return new_trip
    #Please visit models.py to see Class.