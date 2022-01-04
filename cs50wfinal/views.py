from django.http.response import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
import random, string

from .models import *

host = "http://localhost:8000/"
  


def index(request):
    results = {}

    if request.method == "POST":
        url = request.POST["url"]
        letters = string.ascii_lowercase

        if request.user.is_authenticated:
            user = request.user 
            u = Url(url=url, shorten=''.join(random.choice(letters) for i in range(10)), user=user)   
            u.save()
        else:
            if request.COOKIES.get('UserNotSignIn'):
                u = Url(url=url, shorten=''.join(random.choice(letters) for i in range(10)), userNotSignIn=UserNotSignIn.objects.get(cookie=int(request.COOKIES.get('UserNotSignIn'))))   
                u.save() 
            else:
                user_cookie = UserNotSignIn()
                user_cookie.save()
                u = Url(url=url, shorten=''.join(random.choice(letters) for i in range(10)), userNotSignIn=user_cookie)   
                u.save()

                response = HttpResponseRedirect('/')
                response.set_cookie('UserNotSignIn', int(user_cookie.cookie), max_age=9000000000)
                return response

    if request.user.is_authenticated:
        urls = Url.objects.filter(user = request.user)
    else:
        try:
            urls = Url.objects.filter(userNotSignIn = UserNotSignIn.objects.get(cookie=int(request.COOKIES.get('UserNotSignIn'))))
        except:
            urls = []

    results["urls"] = list(urls)
    results["host"] = host

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
