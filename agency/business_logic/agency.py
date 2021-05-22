from agency.business_logic.car_list import CarList
from .employee_list import EmployeeList
from .trip_list import TripList
from django.utils import timezone

class Agency:
    def __init__(self):
        self.employees = EmployeeList()
        self.trips = TripList()
        self.cars = CarList()
    
    def add_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.add_employee(CNIC,first_name,last_name,email,contact_number,address)

    def update_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.update_employee(CNIC,first_name,last_name,email,contact_number,address)

    def delete_employee(self,CNIC):
        return self.employees.delete_employee(CNIC)
        
    def add_custom_trip(self,source,destination,start_date,end_date):
        return self.trips.add_custom_trip(source,destination,start_date,end_date)
        
