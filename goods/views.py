from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ShoppingCart
from .forms import NewCardForm
from cart.forms import AddToCartForm

def create_product_card(request):
    if request.method == 'POST':
        card_form = NewCardForm(request.POST, request.FILES)
        if card_form.is_valid():
            product = card_form.save(commit=False)
            product.owner = request.user
            product.save()

            return HttpResponseRedirect(f'{product.get_url()}')
    else:
        card_form = NewCardForm()
    return render(request, 'goods/new_product_card.html', context={
        'card_form':card_form,
    })

def product_card(request, slug_category:str, product_id:int):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'goods/product_card.html', context={
        'product':product,
    })
def market(request):
    categories = Category.objects.all()
    return render(request, 'goods/market.html', context={
        'categories':categories
    })


def category(request, slug_category:str):
    category = get_object_or_404(Category, slug=slug_category)
    products = Product.objects.filter(category=category.id)
    add_to_cart_form = AddToCartForm()
    return render(request, 'goods/category.html', context={
        'category':category,
        'products':products,
        'cart_form': add_to_cart_form,
    })


def products_on_moderation(request):
    products = Product.objects.filter(on_moderation=True)
    return render(request, 'goods/ad_moderation.html', context={
        'products': products,
    })
