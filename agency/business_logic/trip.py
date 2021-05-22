from ..models import TRIP
class Trip:
    def __new__(cls, source,destination,start_date,end_date,is_custom):
        new_trip = TRIP(
            source = source,
            destination = destination,
            start_date = start_date,
            end_date = end_date,
            is_custom = is_custom
        )
        return new_trip
    #Please visit models.py to see Class.