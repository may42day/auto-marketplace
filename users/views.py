from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserSignUpForm, ProfileForm
from goods.models import Product
from django.urls import reverse


def index(request):
    return render(request, "users/index.html")


def sign_up(request):
    if request.method == "POST":
        user_form = UserSignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data["password"])
            user.is_active = True
            user.profile.user_type = profile_form.cleaned_data["user_type"]
            user.save()
            return redirect(reverse("login_new"))
    else:
        user_form = UserSignUpForm()
        profile_form = ProfileForm()
    return render(
        request,
        "users/sign_up.html",
        context={
            "user_form": user_form,
            "profile_form": profile_form,
        },
    )


@login_required
def seller_products(request):
    products = Product.objects.filter(user=request.user)
    return render(
        request,
        "users/SellerProducts.html",
        context={
            "products": products,
        },
    )
