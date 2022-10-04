from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create_product_card, name='create-card'),
    path('', views.market, name='market'),
    path('<slug:slug_category>', views.category, name='category-detail'),
]