from django.http import HttpResponse


def index(request):
    about_link = '<a href="/rango/about/">About</a>'

    return HttpResponse("Rango says hey there partner!" +
                        " Do you know the 'about' page yet?" +
                        " If not have a look under: " +
                        about_link)


def about(request):
    index_link = '<a href="/rango/">Main page</a>'

    return HttpResponse("Rango says here is the about page. </br>" +
                        index_link)
