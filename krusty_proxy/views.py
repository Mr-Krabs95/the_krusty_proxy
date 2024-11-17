from django.shortcuts import render

def index(request):
    """Домашняя страница приложения krusty_proxy."""
    return render(request, 'krusty_proxy/index.html')
