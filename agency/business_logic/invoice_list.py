from .invoice import Invoice
from .fixed_invoice import FixedInvoice
from ..models import FIXED_INVOICE, INVOICE
from django.core.exceptions import ObjectDoesNotExist

class InvoiceList:
    def __init__(self):
        pass

    def add_invoice(self,booking):
        allocated_car = booking.allocated_car
        allocated_hotel = booking.allocated_hotel
        start_date = booking.trip.start_date
        end_date = booking.trip.end_date
        days_booked = (end_date - start_date).days + 1
        total_price = days_booked * allocated_car.fare.car_fare
        if allocated_hotel != None:
            total_price += days_booked * allocated_hotel.charges.hotel_fare
        new_invoice = Invoice(booking, total_price)
        new_invoice.save()
        return new_invoice
    
    def add_fixed_invoice(self, booking):
        total_price = booking.trip.price
        new_invoice = FixedInvoice(booking, total_price)
        new_invoice.save()
        return new_invoice

    def get_invoice(self,id):
        try:
            invoice = INVOICE.objects.get(id = id)
            return invoice
        except ObjectDoesNotExist:
            raise Exception(f'Trip: {id} does not exist!')
    
    def get_fixed_invoice(self,id):
        try:
            invoice = FIXED_INVOICE.objects.get(id = id)
            return invoice
        except ObjectDoesNotExist:
            raise Exception(f'Trip: {id} does not exist!')

    def get_invoices(self,user):
        if user.is_superuser:
            return INVOICE.objects.all()
        else:
            return INVOICE.objects.filter(booking__customer = user)

    def get_invoices_paid(self,user):
        if user.is_superuser:
            return INVOICE.objects.filter(status= True)
        else:
            return INVOICE.objects.filter(booking__customer = user, status =True)
    
    def get_invoices_unpaid(self,user):
        if user.is_superuser:
            return INVOICE.objects.filter(status= False)
        else:
            return INVOICE.objects.filter(booking__customer = user, status = False)
    
    def get_fixed_invoices_paid(self,user):
        if user.is_superuser:
            return FIXED_INVOICE.objects.filter(status= True)
        else:
            return FIXED_INVOICE.objects.filter(booking__customer = user, status =True)
    
    def get_fixed_invoices_unpaid(self,user):
        if user.is_superuser:
            return FIXED_INVOICE.objects.filter(status= False)
        else:
            return FIXED_INVOICE.objects.filter(booking__customer = user, status = False)
    
    def get_fixed_invoices(self,user):
        if user.is_superuser:
            return FIXED_INVOICE.objects.all()
        else:
            return FIXED_INVOICE.objects.filter(booking__customer = user)
    
    def make_payment(self, payment_date, paid_amount, invoice_pk):
        invoice = self.get_invoice(invoice_pk)
        booking_date = invoice.booking.booking_date
        if payment_date >= booking_date and payment_date <= invoice.booking.trip.start_date:
            invoice.status = True
        else:
            raise Exception("Invalid Date!\nMust be within booking date and trip start date")
        if paid_amount >= invoice.total_charges:
            invoice.paid_amount = paid_amount
            invoice.balance = paid_amount - invoice.total_charges
            invoice.save()
        else:
            raise Exception("Paid amount should be greater or equal to charges")
    
    def make_payment_fixed_trip(self, payment_date, paid_amount, invoice_pk):
        invoice = self.get_fixed_invoice(invoice_pk)
        booking_date = invoice.booking.booking_date
        if payment_date >= booking_date and payment_date <= invoice.booking.trip.start_date:
            invoice.status = True
        else:
            raise Exception("Invalid Date!\nMust be within booking date and trip start date")
        if paid_amount >= invoice.total_charges:
            invoice.paid_amount = paid_amount
            invoice.balance = paid_amount - invoice.total_charges
            invoice.save()
        else:
            raise Exception("Paid amount should be greater or equal to charges")
    

# <h2><a href="{% url 'fixed-trip-detail' trip.id %}">{{ trip.id }}</a></h2>