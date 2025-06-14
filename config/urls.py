# config/urls.py
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),  # <- добавляем это
    path('admin/', admin.site.urls),
    # другие маршруты
]