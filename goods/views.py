from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import *
from cart.forms import AddToCartForm
from django.views.generic import View, ListView, DeleteView, DetailView

class MarketPage(ListView):
    model = Category
    template_name = 'goods/market.html'
    context_object_name = 'categories'

class ProductCard(DetailView):
    model = Product
    template_name = 'goods/product_card.html'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = AddToCartForm()
        if 'currency' in self.request.COOKIES:
            context['currency'] = self.request.COOKIES.get('currency')
        else:
            context['currency'] = 'EURO'
        return context

@login_required
def create_product_card(request):
    if request.method == 'POST':
        card_form = NewCardForm(request.POST, request.FILES)
        if card_form.is_valid():
            product = card_form.save(commit=False)
            product.user = request.user
            currency_rate = float(CurrencyRate.objects.latest().Euro_to_Usd)
            price = float(request.POST['price'])
            currency = request.POST['currency']
            if currency == 'USD':
                product.price_usd = price
                product.price_euro = price / currency_rate
            else:
                product.price_usd = price * currency_rate
                product.price_euro = price
            product.average_rating = 0
            product.feedback_counter = 0
            product.save()
            return HttpResponseRedirect(f'{product.get_absolute_url()}')
    else:
        card_form = NewCardForm()
    return render(request, 'goods/new_product_card.html', context={
        'card_form':card_form,
    })

order_param_dict = {
    'NEW':'-created',
    'OLD':'created',
    'CHEAP':'price_euro',
    'EXPENSIVE':'-price_euro',
    'RATING':'-average_rating',
}
def category(request, slug_category:str, slug_subcategory=None):
    current_category = get_object_or_404(Category, slug=slug_category)

    if 'currency' in request.COOKIES:
        currency = request.COOKIES.get('currency')
    else:
        currency = 'EURO'

    if request.GET:
        currency = request.GET['currency']
        new_param = request.GET['search_filter']
        order_param = order_param_dict[new_param]
        if 'on_stock' in request.GET:
            products = Product.objects.filter(category=current_category.id, amount__gt=0, on_moderation=False).order_by(order_param)
        else:
            products = Product.objects.filter(category=current_category.id, amount__gt=-1, on_moderation=False).order_by(order_param)
    else:
        products = Product.objects.filter(category=current_category.id, on_moderation=False).order_by('-created')

    add_to_cart_form = AddToCartForm()

    current_subcategory = None
    if slug_subcategory:
        current_subcategory = get_object_or_404(Subcategory, slug=slug_subcategory)
        products = products.filter(subcategory=current_subcategory)

    new_request = request.GET.copy()
    new_request['currency'] = currency
    filters_form = SearchFiltersForm(new_request)

    products_list = products
    paginator = Paginator(products_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    response = render(request, 'goods/category.html', context={
        'current_category':current_category,
        'products': products,
        'cart_form': add_to_cart_form,
        'filters_form': filters_form,
        'current_subcategory':current_subcategory,
        'currency':currency,
        'page_obj': page_obj,
    })

    if request.GET:
        response.set_cookie('currency', currency)
    return response

@login_required
def products_on_moderation(request):
    products = Product.objects.filter(on_moderation=True)
    return render(request, 'goods/ad_moderation.html', context={
        'products': products,
    })


def search(request):
    search = request.GET.get('search', '')
    if search or request.GET:
        if 'currency' in request.GET:
            currency = request.GET['currency']
        else:
            currency = 'EURO'
        if 'search_filter' in request.GET:
            new_param = request.GET['search_filter']
            order_param = order_param_dict[new_param]
        else:
            order_param = '-created'
        add_to_cart_form = AddToCartForm()
        filters_form = SearchFiltersForm(request.GET)
        if 'on_stock' in request.GET:
            products = Product.objects.filter(amount__gt=0, on_moderation=False).order_by(order_param)
        else:
            products = Product.objects.filter(amount__gt=-1, on_moderation=False).order_by(order_param)

        products_list = products
        paginator = Paginator(products_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'goods/search.html', context={
            'page_obj':page_obj,
            'currency': currency,
            'filters_form':filters_form,
            'add_to_cart_form':add_to_cart_form,
        })
    return HttpResponseRedirect('/')

class RemoveProductOnModeration(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('goods:moderation')


class ApproveProductModeration(View):
    model = Product

    def post(self, request, pk):
        self.model.objects.filter(pk=pk).update(on_moderation=False)
        return HttpResponseRedirect(reverse_lazy('goods:moderation'))
