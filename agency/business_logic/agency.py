from .employee_list import EmployeeList
from .hotel_list import HotelList
from django.utils import timezone

class Agency:
    def __init__(self):
        self.employees = EmployeeList()
        self.hotels = HotelList()
    
    def add_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.add_employee(CNIC,first_name,last_name,email,contact_number,address)

    def update_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.update_employee(CNIC,first_name,last_name,email,contact_number,address)

    def delete_employee(self,CNIC):
        return self.employees.delete_employee(CNIC)

    def add_hotel(self,name,city,address,image,charges):
        self.hotels.add_hotel(name,city,address,image,charges)