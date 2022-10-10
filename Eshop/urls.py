from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'AutoShop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('market/', include('goods.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

