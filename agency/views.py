from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import EMPLOYEE
from .business_logic.agency import Agency
from . import forms

controller = Agency()

class EmployeeDetailView(DetailView):
     model = EMPLOYEE

@login_required
@user_passes_test(lambda u: u.is_superuser)
def EmployeesView(request):
    employees = controller.employees.get_employees(request.user)
    context = {'employees':employees}
    return render(request, 'agency/employee_list.html',context)

# Create your views here.
# Function Views
def home(request):
    context = {
        'cars': ['C1','C2','C3']
    }
    return render(request, 'agency/home.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def register_driver(request):
    if request.method == 'POST':
        form = forms.RegisterDriverForm(request.POST)
        if form.is_valid():
            CNIC = form.cleaned_data.get("CNIC")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            contact_number = form.cleaned_data.get("contact_number")
            address = form.cleaned_data.get("address")
            #hourly_rate = form.cleaned_data.get("hourly_rate")

            controller.add_employee(CNIC,first_name,last_name,email,contact_number,address)
            messages.success(request, f'Driver added successfully!')
            return redirect('agency-register-employee')
    else:
        form = forms.RegisterDriverForm()
    return render(request,'agency/register_employee.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def search_employee(request):
    if request.method == 'POST':
        search_form = forms.SearchEmployeeForm(request.POST)
        if search_form.is_valid():
            CNIC = search_form.cleaned_data["CNIC"]
            try:
                searched_employee = controller.employees.get_employee(CNIC)
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
    searched_employee = controller.employees.get_employee(pk)
    if request.method == 'POST':
        update_form = forms.EmployeeUpdateForm(request.POST, instance=searched_employee)
        if update_form.is_valid():
            CNIC = update_form.cleaned_data.get("CNIC")
            first_name = update_form.cleaned_data.get("first_name")
            last_name = update_form.cleaned_data.get("last_name")
            email = update_form.cleaned_data.get("email")
            contact_number = update_form.cleaned_data.get("contact_number")
            address = update_form.cleaned_data.get("address")

            controller.update_employee(CNIC,first_name,last_name,email,contact_number,address)
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
            is_deleted = controller.delete_employee(CNIC)
            if is_deleted == True:
                messages.success(request, f'Employee deleted successfully!')
            else:
                messages.info(request, f'Employee does not exist!')
            return redirect ('agency-delete-employee')
    else:
        form = forms.SearchEmployeeForm()
    return render(request,'agency/delete_employee.html',{'form': form})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_employee(request):
    return render(request, 'agency/manage_employee.html')


@login_required
@user_passes_test(lambda u: u.is_superuser == False)
def book_custom_trip(request):
    if request.method == 'POST':
        form = forms.BookCustomTripForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data.get("source")
            destination = form.cleaned_data.get("destination")
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")

            trip = controller.add_custom_trip(source,destination,start_date,end_date)
            messages.success(request, f'Trip added successfully!')
            return redirect('agency-select-trip-car',trip.id)
    else:
        form = forms.BookCustomTripForm()
    return render(request,'agency/book_trip.html',{'form': form})

def car_list(request,pk):
    if request.method == 'POST':
        pass
    else:
        cars = controller.cars.get_cars()
        trip = controller.trips.get_trip(pk)
        context = {
            'cars': cars,
            'trip': trip
        }
        return render(request, 'agency/car_list.html', context)



def test_func(self):
    if self.request.user.is_superuser():
        return True
    else:
        return False