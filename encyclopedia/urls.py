from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.page, name="page"),
    path("search/<str:query>", views.results, name="results"),
    path("newpage", views.new_page, name="new_page"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("/random", views.random_page, name="random_page")
]
