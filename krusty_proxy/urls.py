""" Определляет схемы URL для krusty_proxy. """

from django.urls import path
from . import views

app_name = 'krusty_proxy'
urlpatterns = [
    # домашняя страница
    path('', views.index, name='index'),
]
