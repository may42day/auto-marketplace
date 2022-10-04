from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def create_product_card(request):
    return render(request, 'goods/new_product_card.html')

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