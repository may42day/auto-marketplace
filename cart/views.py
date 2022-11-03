from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import AddToCartForm
from goods.models import Product


@require_POST
def add_to_shopping_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add_to_cart(
            product=product,
            amount=data['amount'],
            update_amount=data['amount'],
        )
    return redirect('cart:cart_detail')


@login_required
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    for product in cart:
        product['update_amount_form'] = AddToCartForm(initial={
            'amount': product['amount'],
            'update': True
        })
    return render(request, 'cart/ShoppingCart.html', context={
        'cart':cart
    })