from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.market, name='market'),
    path('create', views.create_product_card, name='create-card'),
    path('moderation', views.products_on_moderation, name='moderation'),
    path('<slug:slug_category>', views.category, name='category-detail'),
    path('<slug:slug_category>/<int:product_id>', views.product_card, name='product-card'),

]