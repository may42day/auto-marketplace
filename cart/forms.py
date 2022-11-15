from django import forms

AMOUNT_CHOICES = [(i, str(i)) for i in range(1, 21)]

class AddToCartForm(forms.Form):
    amount = forms.TypedChoiceField(
        choices=AMOUNT_CHOICES,
        coerce=int
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )