from django.urls import path

from . import views
from .views import MyView

urlpatterns = [
    path("wellcome", views.index, name="index"),
    # path("about", views.about, name="about"),
    path("add_book", views.add_book, name="get_book"),
    path("get_name", views.get_name, name="get_name"),
    path("about/", MyView.as_view()),

]