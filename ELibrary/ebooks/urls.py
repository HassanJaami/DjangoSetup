from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path("add_book/", AddBookView.as_view()),
    path("about/", MyView.as_view()),
    path("create/", BookCreateView.as_view()),
    path("list/", BookListView.as_view()),
    path ("detail/<pk>/", BookDetail.as_view()),
    path("update/<pk>/", BookUpdate.as_view()),
    path("delete/<pk>/", BookDelete.as_view()),
]
