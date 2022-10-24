from django.urls import path, include
from .views import MarketPage, create_product_card, products_on_moderation, category, ProductCard

urlpatterns = [
    path('', MarketPage.as_view(), name='market'),
    path('create', create_product_card, name='create-card'),
    path('moderation', products_on_moderation, name='moderation'),
    path('<slug:slug_category>', category, name='category-detail'),
    path('<slug:slug_category>/<int:product_id>', ProductCard.as_view(), name='product-card'),

]