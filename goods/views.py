from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ShoppingCart
from .forms import NewCardForm
from cart.forms import AddToCartForm
from django.views.generic import ListView, DeleteView


class MarketPage(ListView):
    model = Category
    template_name = 'goods/market.html'
    context_object_name = 'categories'

class ProductCard(DeleteView):
    model = Product
    template_name = 'goods/product_card.html'
    pk_url_kwarg = 'product_id'

def create_product_card(request):
    if request.method == 'POST':
        card_form = NewCardForm(request.POST, request.FILES)
        if card_form.is_valid():
            product = card_form.save(commit=False)
            product.user = request.user
            product.save()

            return HttpResponseRedirect(f'{product.get_url()}')
    else:
        card_form = NewCardForm()
    return render(request, 'goods/new_product_card.html', context={
        'card_form':card_form,
    })


def category(request, slug_category:str):
    categories = Category.objects.all()
    current_category = get_object_or_404(Category, slug=slug_category)
    products = Product.objects.filter(category=current_category.id)
    add_to_cart_form = AddToCartForm()
    return render(request, 'goods/category.html', context={
        'categories':categories,
        'current_category':current_category,
        'products':products,
        'cart_form': add_to_cart_form,
    })


def products_on_moderation(request):
    products = Product.objects.filter(on_moderation=True)
    return render(request, 'goods/ad_moderation.html', context={
        'products': products,
    })


def search(request):
    search = request.GET.get('search', '')
    if search:
        products = Product.objects.filter(name__icontains=search).order_by('-created')
        return render(request, 'goods/search.html', context={
            'products':products,
        })
    return HttpResponseRedirect('/')