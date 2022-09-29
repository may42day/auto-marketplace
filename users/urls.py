from django.contrib import admin
from django.urls import path, include
from .views import start_page, sign_up

urlpatterns = [
    path('', start_page),
    path('sign_up', sign_up, name='sign_up')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]