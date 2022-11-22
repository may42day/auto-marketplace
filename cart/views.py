from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView
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

    payment_form = PaymentForm(request.POST)
    error_message = ''
    if request.method == 'POST' and payment_form.is_valid():
        if len(cart) > 0:
            order = Order.objects.create(
                user=request.user,
                status='PLACE',
                currency=currency)

            for item in cart:
                if item['product'].amount < item['amount']:
                    amount = item['product'].amount
                else:
                    amount = item['amount']
                item['product'].amount -= amount
                item['product'].save()

                if currency == 'Euro':
                    price = item['price_euro']
                else:
                    price = item['price_usd']

                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    amount=amount,
                    price=price,
                )


            cart.clear()
            return redirect(reverse('cart:order', kwargs={'order_pk':order.pk}))
        error_message = 'Cart is empty or product is not available'

    return render(request, 'cart/ShoppingCart.html', context={
        'cart':cart,
        'currency': currency,
        'payment_form': payment_form,
        'error_message': error_message,
    })



class OrdersHistory(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart/OrdersHistory.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@login_required()
def order_info(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    if order.user == request.user:
        items = order.items.all()
        data = request.POST
        order_form = OrderForm(data)

        if request.POST and order_form.is_valid() and order.status == 'PLACE':
            order.full_name = data['full_name']
            order.address = data['address']
            order.postal_code = data['postal_code']
            order.phone_number = data['phone_number']
            if 'comment' in data:
                order.comment = data['comment']
            order.status = 'OPEN'
            order.save()

        return render(request, 'cart/Order.html', context={
            'order': order,
            'items': items,
            'order_form': order_form,

        })
    return redirect('/')


class RemoveOrder(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('cart:orders-history')


