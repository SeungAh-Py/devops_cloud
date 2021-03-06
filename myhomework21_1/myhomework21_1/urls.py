from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
    path('shop/', include('shop.urls')),
]

urlpatterns += static(settings.MEDIA_URL, base_dir=settings.MEDIA_ROOT)
