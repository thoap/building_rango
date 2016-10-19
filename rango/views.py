from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, "rango/index.html", context=context_dict)


def about(request):
    name = random.choice(["Jerry Seinfeld", "George Costanza", "Kramer",
                          "your cat", "Elaine Bennet"])

    name_dict = {"tutcreator": name}

    return render(request, "rango/about.html", context=name_dict)
