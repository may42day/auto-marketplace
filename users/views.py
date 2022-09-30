from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserSignUpForm, ProfileForm

def start_page(request):
    return render(request, 'users/start_page.html')


def sign_up(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.is_active = True
            user.profile.user_type = profile_form.cleaned_data['user_type']
            user.save()

            # profile_form = ProfileForm(request.POST, instance=user)
            # profile_form.save()

            return HttpResponseRedirect('/')
    else:
        user_form = UserSignUpForm()
        profile_form = ProfileForm()
    return render(request, 'users/sign_up.html', context={
        'user_form':user_form,
        'profile_form':profile_form,
    })