from django.shortcuts import render
from django.http import HttpResponse
import string
import random


def home(request):
    return render(request, 'generator/home.html')


def eggs(request):
    return HttpResponse("<h1>Eggs are awesome</h1>")


def password(request):
    generated_password = ''
    characters = list(string.ascii_lowercase)
    length = 10
    for x in range(length):
        generated_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': generated_password})