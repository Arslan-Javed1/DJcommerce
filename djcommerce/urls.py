
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
