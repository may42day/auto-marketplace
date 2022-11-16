from django import forms
from django.core.validators import MinValueValidator

from .models import Product

CURRENCY_CHOICES = [
    ('EURO', 'Euro'),
    ('USD', 'Dollars'),
]

SEARCH_FILTERS = [
    ('NEW', 'the newest'),
    ('OLD', 'the oldest'),
    ('CHEAP', 'cheap first'),
    ('EXPENSIVE', 'expensive first'),
    ('RATING', 'by rating')
]

class NewCardForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)
    price = forms.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2)
    field_order = ('category', 'subcategory', 'name', 'amount', 'price', 'currency', 'part_number', 'discription', 'picture')
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'name', 'part_number', 'discription', 'amount', 'picture')

    def __init__(self, *args, **kwargs):
        super(NewCardForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


class SearchFiltersForm(forms.Form):
    search_filter = forms.ChoiceField(choices=SEARCH_FILTERS)
    on_stock = forms.BooleanField(required=False)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)



