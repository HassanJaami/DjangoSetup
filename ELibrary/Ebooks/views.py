from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    return HttpResponse("Hello, world. You're in virtual world of learning skills.")


def about(request):
    b = Book(title="OOP", book_type="Computer Science", author="Robert Lafore", pub_date="1999-10-10")
    b.save()
    return HttpResponse("It is online library where you can find any type of book you want")

