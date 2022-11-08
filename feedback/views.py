from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@require_POST
def add_feedback(request, product_id):
    pass
    # cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    # form = AddToCartForm(request.POST)
    # if form.is_valid():
    #     data = form.cleaned_data
    #     cart.add_to_cart(
    #         product=product,
    #         amount=data['amount'],
    #         update_amount=data['amount'],
    #     )
    # return redirect('cart:cart_detail')


@login_required
def remove_feedback(request, product_id, feedback_id):
    pass
    # cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    # cart.remove(product)
    # return redirect('cart:cart_detail')

