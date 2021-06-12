from .invoice import Invoice
from ..models import INVOICE
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

    def get_invoice(self,id):
        try:
            invoice = INVOICE.objects.get(id = id)
            return invoice
        except ObjectDoesNotExist:
            raise Exception(f'Trip: {id} does not exist!')
    
    def get_invoices(self,user):
        if user.is_superuser:
            return INVOICE.objects.all()
        else:
            return INVOICE.objects.filter(booking__customer = user)
    
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

# <h2><a href="{% url 'fixed-trip-detail' trip.id %}">{{ trip.id }}</a></h2>