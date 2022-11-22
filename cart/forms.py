from django import forms
from django.forms import NumberInput, TextInput, Textarea
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import *
import re
import datetime


AMOUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]


class AddToCartForm(forms.Form):
    amount = forms.IntegerField(
        initial=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        widget=NumberInput(attrs={
            'class':'form-control form-control-sm',
            'style': 'width:7ch;'
        })
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['amount'].disabled = True

payment_widgets = {
    'name': TextInput(attrs={
        'placeholder': 'Cardholder\'s Name',
        'class': 'form-select form-select-lg',
        'size': 17,
    }),
    'card_number': TextInput(attrs={
        'placeholder': '1234 5678 9012 3457',
        'class': 'form-select form-select-lg',
        'size': 17,
        'minlength': 19,
        'maxlength': 19,
    }),
    'expiration': TextInput(attrs={
        'placeholder': 'MM/YYYY',
        'class': 'form-select form-select-lg',
        'size': 7,
        'minlength': 7,
        'maxlength': 7,
    }),
    'cvv': TextInput(attrs={
        'placeholder': '999',
        'class': 'form-select form-select-lg',
        'size': 1,
        'minlength': 3,
        'maxlength': 3,
        'type': 'password',

    }),


}

class PaymentForm(forms.Form):
    name = forms.CharField(widget=payment_widgets['name'])
    card_number = forms.IntegerField(widget=payment_widgets['card_number'])
    expiration = forms.CharField(widget=payment_widgets['expiration'])
    cvv = forms.IntegerField(widget=payment_widgets['cvv'])

    def clean_expiration(self):
        data = self.cleaned_data
        expiration = data['expiration']
        if re.search('^((0[1-9])|(1[0-2]))/([0-9]{4})$', expiration):
            today = datetime.datetime.today()
            date = datetime.datetime.strptime(expiration, '%m/%Y')
            if today > date or date > today + datetime.timedelta(days=5500):
                raise forms.ValidationError('Invalid date')
            return expiration
        raise forms.ValidationError('Invalid input (try MM/YYYY)')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address', 'postal_code', 'phone_number', 'comment')
        widgets = {
            'full_name':TextInput(attrs={
                'placeholder': 'Full name',
                'class': 'form-select form-select-lg',
            }),
            'address':TextInput(attrs={
                'placeholder': 'Street address. City.',
                'class': 'form-select form-select-lg',
            }),
            'postal_code':NumberInput(attrs={
                'placeholder': '123456',
                'class': 'form-select form-select-lg',
                'minlength': 6,
                'maxlength': 6,
            }),
            'phone_number':TextInput(attrs={
                'placeholder': '+1 123 4567890',
                'class': 'form-select form-select-lg',
            }),
            'comment':Textarea(attrs={
                'placeholder': 'Comment for delivery',
                'class': 'form-select form-select-lg',
                'rows': 5,
            }),
        }





