from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db import IntegrityError
from django.forms.models import model_to_dict
import random, string

from .models import *

host = "http://localhost:8000/"
  
def newUrl(request):
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
    
    return JsonResponse({"urlShorten": host + u.shorten})


def index(request, isJs=0):
    results = {}

    if request.user.is_authenticated:
        urls = Url.objects.filter(user = request.user).order_by('-id').values()
    else:
        #create cookie if user not login and dont have cookie already
        if not request.COOKIES.get('UserNotSignIn'):
            user_cookie = UserNotSignIn()
            user_cookie.save()
            response = HttpResponseRedirect('/')
            response.set_cookie('UserNotSignIn', int(user_cookie.cookie), max_age=9000000000)
            return response

        try:
            urls = Url.objects.filter(userNotSignIn = UserNotSignIn.objects.get(cookie=int(request.COOKIES.get('UserNotSignIn')))).order_by('-id').values()
        except:
            urls = []

    results["urls"] = list(urls)
    results["host"] = host

    if isJs != 0:
        return JsonResponse(data={'status': 'success', 'results': results}, status=200, safe=True)

    return render(request, "index.html", results)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["email"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(request, username=username, password=password)
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request, "register.html")

def shorten(request,shorten):
    try:
        u = Url.objects.get(shorten=shorten)
        url = u.url
        u.visits +=1
        u.save()
        return HttpResponseRedirect(url)
    except:
        return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('UserNotSignIn')
    return response