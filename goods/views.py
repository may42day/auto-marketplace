from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from cart.forms import AddToCartForm
from django.views.generic import ListView, DeleteView, DetailView

class MarketPage(ListView):
    model = Category
    template_name = 'goods/market.html'
    context_object_name = 'categories'

class ProductCard(DetailView):
    model = Product
    template_name = 'goods/product_card.html'
    pk_url_kwarg = 'product_id'


@login_required
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

order_param_dict = {
    'NEW':'-created',
    'OLD':'created',
    'CHEAP':'price',
    'EXPENSIVE':'-price',
}
def category(request, slug_category:str):
    current_category = get_object_or_404(Category, slug=slug_category)

    filters_form = SearchFiltersForm(request.GET)
    if request.GET:
        new_param = request.GET['search_filter']
        order_param = order_param_dict[new_param]
        if 'stock_availability' in request.GET:
            stock = 0
        else:
            stock = -1
        products = Product.objects.filter(category=current_category.id, amount__gt=stock).order_by(order_param)
    else:
        products = Product.objects.filter(category=current_category.id).order_by('-created')
    add_to_cart_form = AddToCartForm()
    return render(request, 'goods/category.html', context={
        'current_category':current_category,
        'products':products,
        'cart_form': add_to_cart_form,
        'filters_form': filters_form,
    })

def subcategory(request, slug_category:str, slug_subcategory:str):
    current_subcategory = get_object_or_404(Subcategory, slug=slug_subcategory)
    current_category = get_object_or_404(Category, slug=slug_category)
    filters_form = SearchFiltersForm(request.GET)
    if request.GET:
        new_param = request.GET['search_filter']
        order_param = order_param_dict[new_param]
        if 'stock_availability' in request.GET:
            stock = 0
        else:
            stock = -1
        products = Product.objects.filter(subcategory=current_subcategory.id, amount__gt=stock).order_by(order_param)
    else:
        products = Product.objects.filter(subcategory=current_subcategory.id).order_by('-created')
    return render(request, 'goods/subcategory.html', context={
        'current_subcategory':current_subcategory,
        'current_category':current_category,
        'products':products,
        'filters_form': filters_form,
    })


@login_required
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