from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    results = {}
    return render(request, "index.html", results)