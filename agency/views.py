from agency.business_logic.trip import Trip
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import EMPLOYEE,HOTEL, INVOICE
from .business_logic.agency import Agency
from . import forms
from .filters import TripFilter

agency = Agency()

class EmployeeDetailView(DetailView):
    model = EMPLOYEE

class HotelDetailView(DetailView):
    model = HOTEL

class InvoiceDetailView(DetailView):
    model = INVOICE


class HotelUpdateView(LoginRequiredMixin, UpdateView):
    model = HOTEL
    fields = ['name','city', 'address', 'image','charges']
    




@login_required
@user_passes_test(lambda u: u.is_superuser)
def EmployeesView(request):
    employees = agency.employees.get_employees(request.user)
    context = {'employees':employees}
    return render(request, 'agency/employee_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def HotelsView(request):
    hotels = agency.hotels.get_hotels()
    context = {'hotels':hotels}
    return render(request, 'agency/hotel_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def TripsView(request):
    trips = agency.trips.get_fixed_trips()
    context = {'trips':trips}
    return render(request, 'agency/trip_list.html',context)

@login_required
def InvoiceView(request):
    invoices = agency.invoices.get_invoices(request.user)
    context = {'invoices':invoices}
    return render(request, 'agency/invoice_list.html',context)

@login_required
def InvoiceView_paid(request):
    invoices = agency.invoices.get_invoices_paid(request.user)
    context = {'invoices':invoices}
    return render(request, 'agency/invoice_list.html',context)

@login_required
def InvoiceView_unpaid(request):
    invoices = agency.invoices.get_invoices_unpaid(request.user)
    context = {'invoices':invoices}
    return render(request, 'agency/invoice_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def make_payment(request, pk):
    invoice = agency.invoices.get_invoice(pk)
    if request.method == 'POST':
        form = forms.PaymentForm(request.POST)
        if form.is_valid():
            payment_date = form.cleaned_data.get("payment_date")
            paid_amount = form.cleaned_data.get("paid_amount")
            try:
                agency.make_payment(payment_date,paid_amount,invoice.id)
                messages.success(request, "Payment Successfull")
                return redirect('invoice-detail',invoice.id)
            except Exception as exc:
                messages.warning(request, f'{exc}')
                return redirect('invoice-detail',invoice.id)
        else:
            return redirect('agency-make-payment',invoice.id)
    else:
        form = forms.PaymentForm()
        return render(request,'agency/make_payment.html',{'form': form, 'invoice': invoice})


def home(request):
    return render(request, 'agency/home.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_employee(request):
    if request.method == 'POST':
        form = forms.RegisterEmployeeForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data.get("CNIC")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            contact_number = form.cleaned_data.get("contact_number")
            address = form.cleaned_data.get("address")
            #hourly_rate = form.cleaned_data.get("hourly_rate")

            agency.add_employee(CNIC,first_name,last_name,email,contact_number,address)
            messages.success(request, f'Employee added successfully!')
            return redirect('agency-register-employee')
    else:
        form = forms.RegisterEmployeeForm()
    return render(request,'agency/register_employee.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_hotel(request):
    if request.method == 'POST':
        form = forms.AddHotelForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            city = form.cleaned_data.get("city")
            address = form.cleaned_data.get("address")
            image = form.cleaned_data.get("image")
            charges = form.cleaned_data.get("charges")
            agency.add_hotel(name,city,address,image,charges)
            messages.success(request, f'Hotel added successfully!')
            return redirect('agency-add-hotel')
    else:
        form = forms.AddHotelForm()
    return render(request,'agency/add_hotel.html',{'form': form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def search_employee(request):
    if request.method == 'POST':
        search_form = forms.SearchEmployeeForm(request.POST)
        if search_form.is_valid():
            CNIC = search_form.cleaned_data["CNIC"]
            try:
                searched_employee = agency.employees.get_employee(CNIC)
                messages.success(request, f'Employee found!')
                return HttpResponseRedirect("employee/{CNIC}/".format(CNIC= searched_employee.CNIC))
            except Exception as exc:
                messages.warning(request, f'{exc}')
                return redirect('agency-search-employee')
    else:
        search_form = forms.SearchEmployeeForm()
        return render(request,'agency/search_employee.html',{'search_form': search_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def update_employee(request,pk):
    searched_employee = agency.employees.get_employee(pk)
    if request.method == 'POST':
        update_form = forms.EmployeeUpdateForm(request.POST, instance=searched_employee)
        if update_form.is_valid():
            CNIC = update_form.cleaned_data.get("CNIC")
            first_name = update_form.cleaned_data.get("first_name")
            last_name = update_form.cleaned_data.get("last_name")
            email = update_form.cleaned_data.get("email")
            contact_number = update_form.cleaned_data.get("contact_number")
            address = update_form.cleaned_data.get("address")

            agency.update_employee(CNIC,first_name,last_name,email,contact_number,address)
            messages.success(request,f'Employee Updated Succuessfully')
            return redirect('agency-home')
    else:
        update_form = forms.EmployeeUpdateForm(instance=searched_employee)
        context = {'update_form': update_form}
        return render(request,'agency/update_employee.html',context )

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_employee(request):
    if request.method == 'POST':
        form = forms.SearchEmployeeForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data["CNIC"]
            is_deleted = agency.delete_employee(CNIC)
            if is_deleted == True:
                messages.success(request, f'Employee deleted successfully!')
            else:
                messages.info(request, f'Employee does not exist!')
            return redirect ('agency-delete-employee')
    else:
        form = forms.SearchEmployeeForm()
    return render(request,'agency/delete_employee.html',{'form': form})

def delete_hotel(request,pk):
    hotel = agency.hotels.get_hotel(pk)
    if request.method == 'POST':
        try:
            agency.delete_hotel(pk)
            messages.success(request, f'Hotel deleted successfully!')
            return redirect('agency-hotel-list')
        except Exception as exc:
            messages.warning(request,f'{exc}')
            return redirect('agency-hotel-list')
    else:
        return render(request, 'agency/delete_hotel.html',{'hotel': hotel})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def employee_panel(request):
    return render(request, 'agency/employee_panel.html')


@login_required
@user_passes_test(lambda u: u.is_superuser == False)
def book_custom_trip(request):
    messages.info(request, f'Date Format: YYYY-MM-DD')
    if request.method == 'POST':
        form = forms.BookCustomTripForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data.get("source")
            destination = form.cleaned_data.get("destination")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            try:
                trip = agency.add_custom_trip(source,destination,start_date,end_date)
            except Exception as exc:
                messages.warning(request,f'{exc}')
                return redirect('agency-book-custom-trip')
            
            messages.success(request, f'Trip added successfully!')
            return redirect('agency-select-trip-car',trip.id)
    else:
        form = forms.BookCustomTripForm()
    return render(request,'agency/book_trip.html',{'form': form})

def select_car(request,pk):
    cars = agency.cars.get_cars()
    trip = agency.trips.get_trip(pk)
    context = {
        'cars': cars,
        'trip': trip
    }
    return render(request, 'agency/select_car.html', context)

def select_hotel(request,trip_pk,car_pk):
    hotels = agency.hotels.get_hotels()
    context = {
        'trip_pk': trip_pk,
        'car_pk': car_pk,
        'hotels': hotels
    }
    return render(request, 'agency/select_hotel.html', context)

def create_custom_booking(request,trip_pk,car_pk,hotel_pk):
    selected_trip = agency.trips.get_trip(trip_pk)
    selected_car = agency.cars.get_car(car_pk)
    selected_hotel = None
    if hotel_pk != '-1':
        selected_hotel = agency.hotels.get_hotel(hotel_pk)
    if request.method == 'POST':
        try:
            new_booking = agency.add_booking(selected_trip,selected_car,selected_hotel,request.user)
            new_invoice = agency.add_invoice(new_booking)
            messages.success(request, f'Trip Booked successfully!')
            return redirect('invoice-detail', new_invoice.id) # REDIRECT TO INVOICE DETAIL
        except Exception as exc:
            messages.warning(request,f'{exc}')
            return redirect('agency-home')
    else:
        context = {
            'car': selected_car,
            'trip': selected_trip,
            'hotel': selected_hotel,
        }
        return render(request,'agency/create_booking.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_fixed_trip(request):
    messages.info(request, f'Date Format: YYYY-MM-DD')
    if request.method == 'POST':
        form = forms.BookFixedTripForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data.get("source")
            destination = form.cleaned_data.get("destination")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            allocated_hotel = form.cleaned_data.get("allocated_hotel")
            available_seats = form.cleaned_data.get("available_seats")
            price = form.cleaned_data.get("price")
            try:
                trip = agency.add_fixed_trip(source,destination,start_date,end_date,allocated_hotel,available_seats,price)
            except Exception as exc:
                messages.warning(request,f'{exc}')
                return redirect('agency-fixed-trip')
            
            messages.success(request, f'Trip added successfully!')
            return redirect('agency-fixed-trip')
    else:
        form = forms.BookFixedTripForm()
    return render(request,'agency/create_fixed_trip.html',{'form': form})

def browse_fixed_trips(request):
        trips =  agency.trips.get_fixed_trips()
        if request.method == 'POST':
            trip_filter = TripFilter(request.POST,queryset = trips) # GETTING DATA FROM FORM
            filtered_trips = trip_filter.qs
            context = {
                'trips': filtered_trips
            }
            return render(request,'agency/browse_trips.html',context)
        else:
            trip_filter = TripFilter()
            context = {
                'trip_filter': trip_filter,
                'trips': trips
            }
            return render(request,'agency/browse_trips.html',context)


def browse_fixed_trips_home(request):
    trips =  agency.trips.get_fixed_trips()
        
    trip_filter = TripFilter()
    context = {
        'trips': trips
    }
    return render(request,'agency/browse_trips.html',context)