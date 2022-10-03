from django.urls import path, include
from .views import start_page, sign_up

urlpatterns = [
    path('', start_page, name='start-page'),
    path('sign_up', sign_up, name='sign_up')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]