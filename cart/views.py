from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import *
from goods.models import Product
from .models import *


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

    if 'currency' in request.COOKIES:
        currency = request.COOKIES.get('currency')
    else:
        currency = 'EURO'

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        products = []
        for product in cart:
            product_name = product['product'].name
            amount = product['product'].amount
            if currency == 'EURO':
                price = product['product'].price_euro
            else:
                price = product['product'].price_usd
            products.append([product_name, amount, price])

        #if payment_form.is_valid() and products:
        if products:
            total_price = cart.get_total_price_euro()
            Order.objects.create(user=request.user, total_sum=total_price, order_info=products)
            for product in cart:
                product['product'].amount -= product['amount']

            return HttpResponseRedirect('/')
    else:
        payment_form = PaymentForm()

    return render(request, 'cart/ShoppingCart.html', context={
        'cart':cart,
        'currency': currency,
        'payment_form': payment_form,
    })


@method_decorator(login_required, name='dispatch')
class OrdersHistory(ListView):
    model = Order
    template_name = 'cart/OrdersHistory.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@login_required()
def order_info(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    if order.user == request.user:
        order_form = OrderForm(request.POST)
        if request.POST:
            pass

        return render(request, 'cart/Order.html', context={
            'order': order,
            'order_form': order_form,

        })
    return redirect('/')
