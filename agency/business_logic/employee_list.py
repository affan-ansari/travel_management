from .employee import Employee
from ..models import EMPLOYEE
from django.core.exceptions import ObjectDoesNotExist

class EmployeeList:
    def __init__(self):
        pass

    def add_employee(self, CNIC,first_name,last_name,email,contact_number,address):
        first_name = first_name.title()
        last_name = last_name.title()
        new_employee = Employee(CNIC,first_name,last_name,email,contact_number,address) # Returns DRIVER model class object
        new_employee.save()

    def delete_employee(self,CNIC):
        try:
            searched_employee = EMPLOYEE.objects.get(CNIC=CNIC)
            if searched_employee.available == False:
                return False
            else:
                searched_employee.available = False
                searched_employee.save()
                return True
        except ObjectDoesNotExist:
            return False

    def update_employee(self,CNIC,first_name,last_name,email,contact_number,address):
        update_employee = self.get_employee(CNIC)
        update_employee.CNIC = CNIC
        update_employee.first_name = first_name.title()
        update_employee.last_name = last_name.title()
        update_employee.email = email
        update_employee.contact_number = contact_number
        update_employee.address = address
        update_employee.save()

    def get_employee(self,CNIC):
        try:
            searched_employee = EMPLOYEE.objects.get(CNIC=CNIC)
            if searched_employee.available == False:
                raise Exception(f'{CNIC} does not exist!')
            else:
                return searched_employee
        except ObjectDoesNotExist:
            raise Exception(f'{CNIC} does not exist!')

    
    def get_employees(self,user):
        if user.is_superuser:
            employees = EMPLOYEE.objects.filter(available=True)
            return employees
