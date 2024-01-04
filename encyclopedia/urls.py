from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newpage/", views.new_page, name="new_page"),
    path("<str:title>/", views.page, name="page"),
    path("randompage", views.random_page, name="random_page"),
    path("search/<str:query>/", views.results, name="results"),
    path("edit/<str:title>/", views.edit, name="edit"),
]
