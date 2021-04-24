from django import forms
from .models import EMPLOYEE


class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = EMPLOYEE
        fields = '__all__'

class SearchEmployeeForm(forms.Form):
    CNIC = forms.CharField(label="CNIC", max_length=15)

class EmployeeUpdateForm(forms.ModelForm):
    CNIC =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = EMPLOYEE
        fields = '__all__'
