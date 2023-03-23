from django.shortcuts import render

from .models import Category


def index(request):
    queryset = Category.objects.filter(submenu=None)

    data = {
        'data': queryset
    }
    return render(request, 'menu/index.html', data)


def menu(request, title):
    queryset = Category.objects.filter(title=title)

    data = {
        'data': queryset
    }
    return render(request, 'menu/index.html', data)
