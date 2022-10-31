from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'AutoMarket'
admin.site.index_title = 'Admin panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('market/', include('goods.urls')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

