from django.db import models
from ..models import CAR
class Car:
    def __new__(cls,reg_no,make,model,seats,color,image,fare):
        new_car = CAR(
            reg_no = reg_no,
            make = make,
            model = model,
            seats = seats,
            color = color,
            fare = fare,
            image = image
        )
        return new_car
