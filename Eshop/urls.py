from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'AutoShop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('market/', include('goods.urls')),
]

