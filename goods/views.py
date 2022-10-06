from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import NewCardForm

def create_product_card(request):
    if request.method == 'POST':
        card_form = NewCardForm(request.POST)
        if NewCardForm.is_valid():
            # user = user_form.save()
            # user.set_password(user_form.cleaned_data['password'])
            # user.is_active = True
            # user.profile.user_type = profile_form.cleaned_data['user_type']
            # user.save()
            return HttpResponseRedirect('/')
    else:
        card_form = NewCardForm()
    return render(request, 'goods/new_product_card.html', context={
        'card_form':card_form,
    })

def market(request):
    categories = Category.objects.all()
    return render(request, 'goods/market.html', context={
        'categories':categories
    })


def category(request, slug_category:str):
    category = get_object_or_404(Category, slug=slug_category)
    products = Product.objects.filter(category=category.id)
    return render(request, 'goods/category.html', context={
        'category':category,
        'products':products,
    })