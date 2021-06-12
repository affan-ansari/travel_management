import django_filters
from django_filters import NumberFilter,ChoiceFilter
from .models import FIXED_TRIP

DEST_CITIES = (
        ('MURREE', 'MURREE'),
        ('NATHIA GALI', 'NATHIA GALI'),
        ('NARAN KAGHAN', 'NARAN KAGHAN'),
        ('KASHMIR', 'KASHMIR'),
        ('SAWAT', 'SAWAT'),
    )


class TripFilter(django_filters.FilterSet):
    price = NumberFilter(field_name="price", lookup_expr='lte',label='Max Fare')
    destination = ChoiceFilter(choices=DEST_CITIES)
    class Meta:
        model = FIXED_TRIP
        fields = ['destination', 'price']