from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.page, name="page"),
    path("search/<str:query>", views.results, name="results"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/<str:title>", views.edit, name="edit")
]
