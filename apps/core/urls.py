# apps/core/urls.py
from django.urls import path
from apps.core import views  # Импорт твоих вьюшек

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница приложения core
    # тут можно добавить другие маршруты core, например:
    # path('about/', views.about, name='about'),
]
