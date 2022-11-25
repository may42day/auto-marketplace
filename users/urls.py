from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import *
from .forms import NewLoginForm

urlpatterns = [
    path('', index, name='index'),
    path('my_products', seller_products, name='my_products'),
    path('sign_up', sign_up, name='sign_up'),
    path('login', LoginView.as_view(authentication_form=NewLoginForm), name="login_new"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
