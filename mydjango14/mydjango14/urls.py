from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catube.views import index, video_datail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catube/", index),
    path("catube/<int:pk>/", video_datail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
