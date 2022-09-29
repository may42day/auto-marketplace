from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_repeated_password(self):
        data = self.cleaned_data
        if data['password'] != data['repeated_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return data['repeated_password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)