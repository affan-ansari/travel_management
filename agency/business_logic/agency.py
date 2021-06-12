from agency.business_logic.booking_list import BookingList
from agency.business_logic.car_list import CarList
from .employee_list import EmployeeList
from .trip_list import TripList
from .hotel_list import HotelList
from .invoice_list import InvoiceList
from django.utils import timezone

class Agency:
    def __init__(self):
        self.employees = EmployeeList()
        self.trips = TripList()
        self.cars = CarList()
        self.hotels = HotelList()
        self.bookings = BookingList()
        self.invoices = InvoiceList()
    
    def add_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.add_employee(CNIC,first_name,last_name,email,contact_number,address)

    def update_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        self.employees.update_employee(CNIC,first_name,last_name,email,contact_number,address)

    def delete_employee(self,CNIC):
        return self.employees.delete_employee(CNIC)
        
    def add_custom_trip(self,source,destination,start_date,end_date):
        return self.trips.add_custom_trip(source,destination,start_date,end_date)
    
    def add_fixed_trip(self,source,destination,start_date,end_date,allocated_hotel,available_seats,price):
        return self.trips.add_fixed_trip(source,destination,start_date,end_date,allocated_hotel,available_seats,price)

    def add_hotel(self,name,city,address,image,charges):
        self.hotels.add_hotel(name,city,address,image,charges)
    
    def delete_hotel(self,hotel_id):
        self.hotels.delete_hotel(hotel_id)
    
    def add_booking(self,trip,allocated_car,allocated_hotel,customer):
        return self.bookings.add_booking(trip,allocated_car,allocated_hotel,customer)
    
    def add_fixed_booking(self,trip, customer):
        return self.bookings.add_fixed_booking(trip, customer)
    
    def add_invoice(self, booking):
        return self.invoices.add_invoice(booking)
    
    def add_fixed_invoice(self, booking):
        return self.invoices.add_fixed_invoice(booking)
    
    def make_payment(self, payment_date, paid_amount, invoice_pk):
        self.invoices.make_payment(payment_date, paid_amount, invoice_pk)
    
    def make_payment_fixed_trip(self, payment_date, paid_amount, invoice_pk):
        self.invoices.make_payment_fixed_trip(payment_date, paid_amount, invoice_pk)
