from django.shortcuts import render


def create_product_card(request):
    return render(request, 'goods/new_product_card.html')

def market(request):
    return render(request, 'goods/market.html')