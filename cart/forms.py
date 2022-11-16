from django import forms
from django.forms import NumberInput
from django.core.validators import MinValueValidator, MaxValueValidator

AMOUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]

# class AddToCartForm(forms.Form):
#     amount = forms.TypedChoiceField(
#         choices=AMOUNT_CHOICES,
#         coerce=int
#     )
#     update = forms.BooleanField(
#         required=False,
#         initial=False,
#         widget=forms.HiddenInput
#     )

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
