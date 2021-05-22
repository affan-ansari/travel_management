from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import EMPLOYEE,HOTEL
from .business_logic.agency import Agency
from . import forms

controller = Agency()

class EmployeeDetailView(DetailView):
     model = EMPLOYEE

class HotelDetailView(DetailView):
     model = HOTEL


class HotelUpdateView(LoginRequiredMixin, UpdateView):
    model = HOTEL
    fields = '__all__'




@login_required
@user_passes_test(lambda u: u.is_superuser)
def EmployeesView(request):
    employees = controller.employees.get_employees(request.user)
    context = {'employees':employees}
    return render(request, 'agency/employee_list.html',context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def HotelsView(request):
    hotels = controller.hotels.get_hotels(request.user)
    context = {'hotels':hotels}
    return render(request, 'agency/hotel_list.html',context)

# Create your views here.
# Function Views
def home(request):
    context = {
        'cars': ['C1','C2','C3']
    }
    return render(request, 'agency/home.html', context)

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

            controller.add_employee(CNIC,first_name,last_name,email,contact_number,address)
            messages.success(request, f'Employee added successfully!')
            return redirect('agency-register-employee')
    else:
        form = forms.RegisterEmployeeForm()
    return render(request,'agency/register_employee.html',{'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_hotel(request):
    if request.method == 'POST':
        form = forms.AddHotelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            city = form.cleaned_data.get("city")
            address = form.cleaned_data.get("address")
            image = form.cleaned_data.get("image")
            charges = form.cleaned_data.get("charges")
            controller.add_hotel(name,city,address,image,charges)
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


