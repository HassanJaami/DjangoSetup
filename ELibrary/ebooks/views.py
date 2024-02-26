from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book
from .book_form import BookForm, BookName


class BookDelete(DeleteView):
    model = Book
    success_url = "/ebooks/list/"


class BookUpdate(UpdateView):
    model = Book
    fields = ["title"]
    template_name_suffix = "_update_form"
    success_url ="/ebooks/list/"


class BookDetail(DetailView):
    model = Book


class BookListView(ListView):
    # queryset = Book.objects.order_by("-title")
    model = Book
    # context_object_name = "book_list"


class BookCreateView(CreateView):
    model = Book
    fields = ["title"]

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Have a good day!")
    #
    # def get_queryset(self):
    #     return Book.objects.all()


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("result")


class AddBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, "ebooks/book.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data["Title"]
            author = form.cleaned_data["author"]
            book_type = form.cleaned_data["book_type"]
            pub_date = form.cleaned_data["pub_date"]

            new_book = Book(title=title, book_type=book_type, author=author, pub_date=pub_date)
            new_book.save()
            return HttpResponse("Thanks for saving new book data")


