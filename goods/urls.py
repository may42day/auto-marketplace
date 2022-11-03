from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MarketPage.as_view(), name='market'),
    path('search', search, name='search'),
    path('create', create_product_card, name='create-card'),
    path('moderation', products_on_moderation, name='moderation'),
    path('<slug:slug_category>', category, name='category-detail'),
    path('<slug:slug_category>/<int:product_id>', ProductCard.as_view(), name='product-card'),

]