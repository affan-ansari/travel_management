from django import forms
from django.db.models import fields
from django.forms.forms import Form
from .models import EMPLOYEE, TRIP,HOTEL, FIXED_TRIP

class AddHotelForm(forms.ModelForm):
    class Meta:
        model = HOTEL
        fields = '__all__'
        exclude = ['available']

class HotelUpdateForm(forms.ModelForm):
    class Meta:
        model = HOTEL
        fields = '__all__'
        exclude = ['available']


class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = EMPLOYEE
        fields = '__all__'
        exclude = ['available']

class SearchEmployeeForm(forms.Form):
    CNIC = forms.CharField(label="CNIC", max_length=15)


class EmployeeUpdateForm(forms.ModelForm):
    CNIC =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = EMPLOYEE
        fields = '__all__'
        exclude = ['available']

class BookCustomTripForm(forms.ModelForm):
    class Meta:
        model = TRIP
        fields = '__all__'
        exclude = ['is_custom']

class BookFixedTripForm(forms.ModelForm):
    class Meta:
        model = FIXED_TRIP
        fields = '__all__'
        exclude = ['available']

class PaymentForm(forms.Form):
    payment_date = forms.DateTimeField(label="Payment Date")
    paid_amount = forms.IntegerField(label="Paid Amount")