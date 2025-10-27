# config/urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
]