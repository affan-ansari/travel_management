from ..models import EMPLOYEE
class Employee:
    def __new__(cls, CNIC,first_name,last_name,email,contact_number,address):
        new_employee = EMPLOYEE(
            CNIC=CNIC,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_number=contact_number,
            address=address,
            available=True
            #hourly_rate=hourly_rate
        )
        return new_employee
    #Please visit models.py to see Class.