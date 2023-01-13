from django.shortcuts import render


def home(request):
    """ Отображение главной страницы сайта"""
    return render(request, "mymanager/home.html", {})
