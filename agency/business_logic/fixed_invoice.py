from ..models import FIXED_INVOICE
class FixedInvoice:
    def __new__(cls,booking, total_charges):
        new_invoice = FIXED_INVOICE(
            booking = booking,
            total_charges = total_charges,
        )
        return new_invoice
    #Please visit models.py to see Class.