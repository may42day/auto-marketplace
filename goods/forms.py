from django import forms
from .models import Product

class NewCardForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'part_number', 'discription', 'amount', 'price', 'currency', 'picture')

    def __int__(self, *args, **kwargs):
        super(NewCardForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False

