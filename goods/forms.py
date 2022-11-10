from django import forms
from .models import Product

class NewCardForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'name', 'part_number', 'discription', 'amount', 'price', 'currency', 'picture')

    def __int__(self, *args, **kwargs):
        super(NewCardForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


SEARCH_FILTERS = [
    ('NEW', 'the newest'),
    ('OLD', 'the oldest'),
    ('CHEAP', 'cheap first'),
    ('EXPENSIVE', 'expensive first'),
    ('RATING', 'by rating')
]
class SearchFiltersForm(forms.ModelForm):
    search_filter = forms.ChoiceField(choices=SEARCH_FILTERS)
    on_stock = forms.BooleanField(required=False)
    class Meta:
        model = Product
        fields = ('currency',)



