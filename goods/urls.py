from django.urls import path, include
from .views import create_product_card, market

urlpatterns = [
    path('create', create_product_card, name='create-card'),
    path('', market, name='market'),
]