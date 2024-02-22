from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in virtual world of learning skills.")
# Create your views here.
