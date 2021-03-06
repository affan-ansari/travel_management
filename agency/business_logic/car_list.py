# from agency.business_logic.car_model import Car_Model
from .car import Car
from ..models import CAR
from django.core.exceptions import ObjectDoesNotExist

class CarList:
    def __init__(self):
        pass

    def add_car(self,reg_no,make,model,seats,color,image,fare):
        reg_no = reg_no.upper()
        color = color.capitalize()
        new_car = Car(reg_no,make,model,seats,color,image,fare)
        new_car.save()

    def get_cars(self):
        cars = CAR.objects.filter(available=True)
        return cars
    
    def get_car(self,reg_no):
        try:
            searched_car = CAR.objects.get(reg_no=reg_no)
            if searched_car.available == False:
                raise Exception(f'{reg_no} was deleted!')
            else:
                return searched_car
        except ObjectDoesNotExist:
            raise Exception(f'{reg_no} does not exist!')

