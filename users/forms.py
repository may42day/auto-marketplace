from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select

from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }),)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={
                'placeholder': 'Repeat password',
                'class': 'form-control',
            }),)
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'example@email.com',
                'class': 'form-control',
            }),
        }

    def clean_repeated_password(self):
        data = self.cleaned_data
        if data['password'] != data['repeated_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return data['repeated_password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)
        widgets = {
            'user_type': Select(attrs={
                'placeholder': 'Full name',
                'class': 'form-select',
            }),
        }


class NewLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control rounded-left',
             'placeholder': 'Username',

             })
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control rounded-left',
             'placeholder': 'Password',
             })