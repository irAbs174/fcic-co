from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import (
    path,
    include
)

urlpatterns = [
    path('', include('index.urls')),
    path('sms', include('index.urls')),
    path('unique/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

