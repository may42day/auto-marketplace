from django import forms
from django.core.validators import MinValueValidator
from django.forms import TextInput, Select, FileInput, Textarea

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

card_widgets = {
    'category': Select(attrs={
        'class': 'form-select',
    }),
    'subcategory': Select(attrs={
        'class': 'form-select',

    }),
    'name': TextInput(attrs={
        'placeholder': 'Product name',
        'class': 'form-control',
    }),
    'amount': TextInput(attrs={
        'placeholder': 'amount',
        'class': 'form-control',
    }),
    'price': TextInput(attrs={
        'placeholder': 'price',
        'class': 'form-control',
    }),
    'currency': Select(attrs={
        'class': 'form-select',
    }),
    'part_number': TextInput(attrs={
        'placeholder': 'Part number',
        'class': 'form-control',
    }),
    'discription': Textarea(attrs={
        'placeholder': 'Discription',
        'class': 'form-control',
        'rows': 5,
    }),
    'picture': FileInput(attrs={
        'class': 'form-control',
    }),
}

class NewCardForm(forms.ModelForm):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, widget=card_widgets['currency'])
    price = forms.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2, widget=card_widgets['price'])
    field_order = ('category', 'subcategory', 'name', 'amount', 'price',
                   'currency', 'part_number', 'discription', 'picture')
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'name', 'part_number', 'discription', 'amount', 'picture')
        widgets = card_widgets

    def __init__(self, *args, **kwargs):
        super(NewCardForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


class SearchFiltersForm(forms.Form):
    search_filter = forms.ChoiceField(choices=SEARCH_FILTERS)
    on_stock = forms.BooleanField(required=False)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)



