from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html', {'password': 'secretpass'})


def eggs(request):
    return HttpResponse("<h1>Eggs are awesome</h1>")


def password(request):
    return render(request, 'generator/password.html', {'password': 'secretpass'})