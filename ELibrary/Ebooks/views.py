from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from .models import Book
from .book_form import BookForm, BookName


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")


def index(request):
    return HttpResponse("Hello, world. You're in virtual world of learning skills.")


def thanks(request):
    return HttpResponse("Thanks for submitting form")


def about(request):
    b = Book(title="OOP", book_type="Computer Science", author="Robert Lafore", pub_date="1999-10-10")
    b.save()
    return HttpResponse("It is online library where you can find any type of book you want")


def add_book(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        # print(form.Title)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            title = form.cleaned_data["Title"]
            author = form.cleaned_data["author"]
            book_type = form.cleaned_data["book_type"]
            pub_date = form.cleaned_data["pub_date"]

            new_book = Book(title=title, book_type=book_type, author=author, pub_date=pub_date)
            new_book.save()
            return HttpResponse("Thanks for saving new book data")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, "Ebooks/book.html", {"form": form})


def get_name(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BookName(request.POST)

        if form.is_valid():
            return HttpResponse("Your Book Name is " + form.cleaned_data["Name"])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookName()

    return render(request, "Ebooks/BookName.html", {"form": form})

