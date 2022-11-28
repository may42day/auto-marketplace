from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MarketPage.as_view(), name='market'),
    path('search', search, name='search'),
    path('create', create_product_card, name='create-card'),
    path('moderation', products_on_moderation, name='moderation'),
    path('moderation/remove/<int:pk>', RemoveProductOnModeration.as_view(), name='moderation-remove'),
    path('moderation/approve/<int:pk>', ApproveProductModeration.as_view(), name='moderation-approve'),
    path('<slug:slug_category>', category, name='category-detail'),
    path('<slug:slug_category>/<int:product_id>', ProductCard.as_view(), name='product-card'),
    path('<slug:slug_category>/<slug:slug_subcategory>', category, name='category-detail'),
]