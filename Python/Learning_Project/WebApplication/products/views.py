from django.http import HttpResponse
from django.shortcuts import render

# /products -> index


def index(request):
    return HttpResponse("Hello World")

def NewHello(request):
    return HttpResponse("Hello new")

