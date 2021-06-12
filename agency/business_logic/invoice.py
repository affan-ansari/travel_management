from ..models import INVOICE
class Invoice:
    def __new__(cls,booking, total_charges):
        new_invoice = INVOICE(
            booking = booking,
            total_charges = total_charges,
        )
        return new_invoice
    #Please visit models.py to see Class.