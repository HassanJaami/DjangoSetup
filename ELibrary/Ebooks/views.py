from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in virtual world of learning skills.")
def about(request):
    return HttpResponse("It is online library where you can find any type of book you want")
