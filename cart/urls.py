from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>', add_to_shopping_cart, name='add_to_cart'),
    path('remove/<int:product_id>', remove_from_cart, name='remove_from_cart'),
    path('orders-history', OrdersHistory.as_view(), name='orders-history'),
    path('orders-history/<int:order_pk>', order_info, name='order'),
    path('orders-history/<int:pk>/remove/', RemoveOrder.as_view(), name='remove-order'),
]