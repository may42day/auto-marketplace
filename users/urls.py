from django.urls import path, include
from .views import index, sign_up, seller_products

urlpatterns = [
    path('', index, name='index'),
    path('my_products', seller_products, name='my_products'),
    path('sign_up', sign_up, name='sign_up'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]