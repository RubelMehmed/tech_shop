
from django.contrib import admin
from django.urls import path, include

from . import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', include('admin_material.urls')),
    path('admin/', admin.site.urls),
    path('', include('itshop.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
