from django.http.response import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
import random, string

from .models import *

def create_url(request, url):
    user = request.user if request.user.is_authenticated else None
    letters = string.ascii_lowercase

    try:
        u = Url(url=url, shorten=''.join(random.choice(letters) for i in range(10)), user=user)
        u.save()
    except:
        #retry if shorten generate gives already exists
        u = Url(url=url, shorten=''.join(random.choice(letters) for i in range(10)), user=user)
        u.save()

def index(request):
    results = {}

    if request.method == "POST":
        create_url(request, request.POST["url"])
    return render(request, "index.html", results)

def login(request):
    results = {}
    return render(request, "login.html", results)

def shorten(request,shorten):
    try:
        u = Url.objects.get(shorten=shorten)
        url = u.url
        u.visits +=1
        u.save()
        return HttpResponseRedirect(url)
    except:
        return HttpResponse("<h1>Nothing Found</h1><h2>404</h2>")
