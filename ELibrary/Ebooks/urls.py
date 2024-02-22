from django.urls import path

from . import views

urlpatterns = [
    path("wellcome", views.index, name="index"),
    path("about", views.about, name="about")
]