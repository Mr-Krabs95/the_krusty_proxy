"""Определяет схемы URL для приложения users."""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')),
    # страница регистрации
    path('register/', views.register, name='register'),
]
