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
    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        upper_chars = list(string.ascii_uppercase)
        characters.extend(upper_chars)
    if request.GET.get('special'):
        special_chars = ["<",">","-","/","@","!","~","#","&","?","`",
                         ",",":",";","(",")","[","]","*","^",".","?","+","%"]
        characters.extend(special_chars)
    if request.GET.get('numbers'):
        numbers = [str(el) for el in range(10)]
        characters.extend(numbers)
    for x in range(length):
        generated_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': generated_password})