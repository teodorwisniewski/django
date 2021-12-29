from django.shortcuts import render
from django.http import HttpResponse

import random
import string


def strona_glowna(request):
    return render(request, "gen_repetition/home.html")


def _get_list_of_chars(request):
    characters = list(string.ascii_lowercase)
    if request.GET.get("uppercase"):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get("numbers"):
        characters.extend([str(i) for i in range(10)])
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()-"))
    return characters


def password(request):
    generated_pass = ''
    length = int(request.GET.get('length', 10))
    characters = _get_list_of_chars(request)
    for i in range(length):
        generated_pass += random.choice(characters)
    return render(request, 'gen_repetition/password.html', {"password": generated_pass})


def about(request):
    return render(request, 'gen_repetition/about.html')