from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, "rango/index.html", context=context_dict)


def about(request):
    index_link = '<a href="/rango/">Main page</a>'

    return HttpResponse("Rango says here is the about page. </br>" +
                        index_link)
